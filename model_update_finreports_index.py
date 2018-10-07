from sqlalchemy import create_engine
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql import select
import pandas as pd
import model
import datetime

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)


report_type_for_index = {
	'w_all_add': '所有企业，简单相加', 
	'w_all_equal': '所有企业，等权重，等于简单相加/企业总数，跟标准权重具有可比性', 
	'w_all_std': '所有企业，标准权重',
	'w_general_add': '一般工商企业，简单相加', 
	'w_general_equal': '一般工商企业，等权重，等于简单相加/企业总数', 
	'w_general_std': '一般工商企业，标准权重'
}

start_date = '20180101'
end_date = '20180831'
index_code_list = ['399300.SZ']
index_code = index_code_list[0]

# excute sql
sql_index_weight = "SELECT trade_date, index_code, con_code, weight, month(trade_date) as month FROM index_weight \
					WHERE trade_date >= '%s' and trade_date <= '%s' and month(trade_date) in (3, 6, 9, 12) and index_code = '%s'" \
					% (start_date, end_date, index_code) 

df_iw = pd.read_sql_query(sql_index_weight, engine)

# only keep the biggest trade_date in each month
df_iw = df_iw.groupby(['index_code', 'month']).apply(lambda x: x[ x.trade_date == x.trade_date.max() ])
df_iw.reset_index(drop=True, inplace=True)
# print(df_iw)

# excute sql
sql_balance_sheet = "SELECT * FROM balance_sheet where end_date >= '%s' and end_date <= '%s' and report_type = 1" % (start_date, end_date)

df_bs = pd.read_sql_query(sql_balance_sheet, engine)

# drop duplicate value of ts_code, end_date
df_bs.drop_duplicates(['ts_code', 'end_date'], inplace=True)	# 去除可能key重复的行
df_bs.drop(columns=['ann_date', 'f_ann_date', 'report_type'], inplace=True)	# 去除不需要的列
df_bs.reset_index(drop=True, inplace=True)
df_bs = df_bs.where(df_bs.notnull(), 0.0)	# 将Nan和None替换成0.0
df_bs['month'] = df_bs['end_date'].map(lambda x: datetime.datetime.strptime(x, '%Y%m%d').month)	# 增加一列，end_date所在的月份
# print(df_bs)

# inner join df_bs and df_iw on bs.ts_code = iw.con_code and month(bs.end_date) = month(iw.trade_date)
df_merge = pd.merge(df_iw, df_bs, how='inner', left_on=['con_code', 'month'], right_on=['ts_code', 'month'])
# print(df_merge)


# 增加weight列，包括w_all_add, w_all_equal, w_all_std, w_general_add, w_general_equal, w_general_std。这些列名将作为comp_type的字段值存入财报表中。
df_merge['w_all_add'] = 1.00	# 简单相加的方式获得指数财务报表，所有权重都为1.00
df_merge['w_all_equal'] = df_merge.groupby(['index_code', 'end_date'])['w_all_add'].transform(lambda x: x/x.sum())	# 权重为：简单相加权重1.00 ÷ 企业数量
df_merge['w_all_std'] = df_merge['weight']/100	# 标准权重，因为数据库中的weight字段单位是%，所以这里除以100

# 一般工商企业，comp_type = '1'
df_merge.loc[df_merge['comp_type'] == '1' , 'w_general_add'] = 1.00

df_merge.loc[df_merge['comp_type'] == '1' , 'w_general_equal'] =  \
df_merge.loc[df_merge['comp_type'] == '1'].groupby(['index_code', 'end_date'])['w_general_add'].apply(lambda x: x/x.sum()) 

# w_general_std = w_all_std，权重和不为1，做归一处理
df_merge.loc[df_merge['comp_type'] == '1' , 'w_general_std'] = \
df_merge.loc[df_merge['comp_type'] == '1'].groupby(['index_code', 'end_date'])['w_all_std'].apply(lambda x: x/x.sum())


# weighting, groupby and sum
df_merge = df_merge.where(df_merge.notnull(), 0.0)	# 将Nan和None替换成0.0
df_merge.drop(columns=['trade_date', 'con_code', 'month', 'ts_code', 'weight', 'comp_type'], inplace=True)	# 去除不需要的列
df_merge.to_excel('a.xlsx')

df_merge.set_index(['index_code', 'end_date'], inplace=True)
w = df_merge[list(report_type_for_index.keys())]
df_merge.drop(columns=list(report_type_for_index.keys()), inplace=True)

grouped = pd.DataFrame()
for col in list(report_type_for_index.keys()):
	data = df_merge.multiply(w[col], axis='index')
	g = data.groupby(['index_code', 'end_date']).sum()
	g.insert(0, 'report_type', col)	# 增加一列report_type，在表格的第一列
	g.reset_index(inplace=True)
	# print(g)
	grouped = pd.concat([grouped, g], ignore_index=True)


# 增加key的列，修改key的列名：index_code, end_date, report_type, comp_type
grouped.rename(columns={'index_code': 'ts_code'}, inplace=True)	# 修改列名
grouped.insert(1, 'ann_date', datetime.datetime.today().strftime('%Y%m%d'))
grouped.insert(2, 'f_ann_date', datetime.datetime.today().strftime('%Y%m%d'))
grouped.insert(5, 'comp_type', 'index')

print(grouped)
grouped.to_excel('aa.xlsx')

values = list(grouped.to_dict(orient='index').values())

# save to database table
# get a connection to database
conn = engine.connect()
# first, delete all rows
delete = model.BalanceSheet.__table__.delete().where(
	and_(model.BalanceSheet.__table__.c.end_date >= start_date, 
		 model.BalanceSheet.__table__.c.end_date <= end_date, 
		 model.BalanceSheet.__table__.c.ts_code.in_(index_code_list) ) )
conn.execute(delete)
# second, insert all rows
ins = model.BalanceSheet.__table__.insert()
conn.execute(ins, values)
# close connection
conn.close()

















