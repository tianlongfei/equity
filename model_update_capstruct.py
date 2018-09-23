import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql.expression import and_
from model import SecurityBasicInfo, BalanceSheet, CategoryBalanceSheet
import model
import tushare as ts
from mystoredata import save_list_to_txt, read_list_from_txt


ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
pro = ts.pro_api()

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)


ts_code_list = ['000333.SZ', '000002.SZ']
start_date = '20180101'
end_date = '20181231'


def cal_cap_struct_general(ts_code_list, start_date, end_date):
	ts_code_str = '"' + '","'.join(map(str, ts_code_list)) + '"'	# list to string with ""
	sql = "select * from balance_sheet where ts_code in (%s) and end_date >= '%s' and end_date <= '%s' and report_type = 1 and comp_type=1" % (ts_code_str, start_date, end_date)
	bs = pd.read_sql_query(sql, engine)
	bs.drop_duplicates(['ts_code', 'end_date'], inplace=True)	# 去除可能的重复数据
	bs.drop(columns=['ann_date', 'f_ann_date', 'report_type', 'comp_type'], inplace=True)	# 去除不需要的行
	bs.set_index(['ts_code', 'end_date'], inplace=True)
	bs = bs.where(bs.notnull(), 0.0)	# 将Nan和None替换成0.0
	# print(bs)
	bs = bs.stack()
	bs = pd.DataFrame(bs)
	bs.index.names = ['ts_code', 'end_date', 'bs_item_name']
	bs.columns = ['value']
	bs.reset_index(inplace=True)
	# print(bs)

	cat = pd.read_sql_query('SELECT cid, name, category1_wc FROM category_bs', engine)
	# print(cat)

	bs = pd.merge(bs, cat, how='inner', left_on='bs_item_name', right_on='name')
	# print(bs)

	gp = bs.groupby(['ts_code', 'end_date', 'category1_wc'])['value'].sum()	# a Series, not a DataFrame
	# print(gp)

	cap_struct_detail = gp.unstack()
	cap_struct_detail.reset_index(inplace=True)
	# print(cap_struct_detail)

	# start to calculate aggregated capital structure
	gp = pd.DataFrame(gp)
	gp.reset_index(inplace=True)
	# print(gp)
	# todo: 将category1_wc列中含有_minus的行的value列的值改为负数
	gp.loc[gp['category1_wc'].str.contains('_minus'), 'value'] *= -1.0
	# print(gp)

	# todo：定义全局变量agg_category，merge/jion，groupby
	cat_agg = pd.read_sql_query('SELECT cid, category1_wc, category1_wc_agg FROM category_bs_agg', engine)
	# print(cat_agg)

	gp = pd.merge(gp, cat_agg, how='inner', left_on='category1_wc', right_on='category1_wc')
	# print(gp)
	gp = gp.groupby(['ts_code', 'end_date', 'category1_wc_agg'])['value'].sum()
	# print(gp)
	cap_struct_agg = gp.unstack()
	cap_struct_agg.reset_index(inplace=True)
	# print(cap_struct_agg)
	cap_struct_agg.drop(columns=['-'], inplace=True)	# drop 名称为"-"的column
	cap_struct_agg.eval('invested_capital = liability_interest_bearing + equity_net', inplace=True)
	cap_struct_agg.to_excel('test.xlsx')
	return cap_struct_detail, cap_struct_agg

	# todo: join and groupby category1_wc, insert into database table	done
	# table name: cap_struct_general_detail, cap_struct_general_agg		done
	# table columns: ts_code, end_date, cash, wc+, wc-, ...		done
	# 只计算一般工商业企业，这个标准一方面可以用tushare的balancesheet自带的分类，另外也可以考虑在基础信息表中存储
	# 与model_update_category.py合为一个文件
	# 添加到model_main.py


def update_db(data_df, db_table_class, ts_code_list, start_date, end_date):
	data_dict = data_df.to_dict(orient='index')
	values = list(data_dict.values())

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	delete = db_table_class.__table__.delete().where(
		and_(db_table_class.__table__.c.end_date >= start_date, 
			 db_table_class.__table__.c.end_date <= end_date, 
			 db_table_class.__table__.c.ts_code.in_(ts_code_list) ) )
	conn.execute(delete)
	# second, insert all rows
	ins = db_table_class.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()


def update_cap_struct_general(ts_code_list, start_date, end_date):

	cap_struct_detail, cap_struct_agg = cal_cap_struct_general(ts_code_list, start_date, end_date)
	update_db(cap_struct_detail, model.CapStructGeneralDetail, ts_code_list, start_date, end_date)
	update_db(cap_struct_agg, model.CapStructGeneralAgg, ts_code_list, start_date, end_date)


def update_cap_struct_general_all(start_date, end_date, step=100):

	basics_df = pro.stock_basic(fields='ts_code,symbol,name')
	ts_code_list = basics_df.to_dict(orient='list')['ts_code']

	print('开始计算企业的资本结构detailed and aggregated，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		update_cap_struct_general(sub_ts_code_list, start_date, end_date)
		print('step %s done' % int(i/step+1))


# update_cap_struct_general(ts_code_list, start_date, end_date)
# update_cap_struct_general_all(start_date, end_date)



