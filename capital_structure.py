import pandas as pd
from model import SecurityBasicInfo, BalanceSheet, CategoryBalanceSheet
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)

# ORM way of querying
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()

# SQL Expression Language way of querying
# from sqlalchemy.sql import select
# conn = engine.connect()
# balance_sheet = BalanceSheet._table__

todo = """
根据ts_code，读取balance_sheet，存入dataframe bs
读取category_bs，存入dataframe cat
将bs，cat，join到一起，用cat的列来group

"""
ts_code_list = ['000333.SZ', '000002.SZ']


def capital_structure():
	ts_code_str = '"' + '","'.join(map(str, ts_code_list)) + '"'	# list to string with ""
	start_date = '20180101'
	end_date = '20181231'
	sql = "select * from balance_sheet where ts_code in (%s) and end_date >= '%s' and end_date <= '%s' and report_type = 1" % (ts_code_str, start_date, end_date)
	bs = pd.read_sql_query(sql, engine)
	bs.drop_duplicates(['ts_code', 'end_date'], inplace=True)	# 去除可能的重复数据
	bs.drop(columns=['ann_date', 'f_ann_date', 'report_type', 'comp_type'], inplace=True)	# 去除不需要的行
	bs.set_index(['ts_code', 'end_date'], inplace=True)
	bs = bs.where(bs.notnull(), 0.0)	# 将Nan和None替换成0.0
	print(bs)
	bs = bs.stack()
	bs = pd.DataFrame(bs)
	bs.index.names = ['ts_code', 'end_date', 'bs_item_name']
	bs.columns = ['value']
	bs.reset_index(inplace=True)
	print(bs)

	cat = pd.read_sql_query('SELECT cid, name, category1_wc FROM category_bs', engine)
	print(cat)

	df = pd.merge(bs, cat, how='inner', left_on='bs_item_name', right_on='name')
	print(df)
	df.to_excel('test.xlsx')
	gp = df.groupby(['ts_code', 'end_date', 'category1_wc'])['value'].sum()
	print(gp)

	# todo: join and groupby category1_wc, insert into database table
	# table name: cap_struct_detail, cap_struct_agg
	# table columns: ts_code, end_date, cash, wc+, wc-, ...

capital_structure()






