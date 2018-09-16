from sqlalchemy import create_engine
from sqlalchemy.sql.expression import and_
import pandas as pd
import model
import tushare as ts
from time import sleep
from mystoredata import save_list_to_txt, read_list_from_txt

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)

ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
pro = ts.pro_api()


def creat_all_tables_not_exist():
	# create tables which donot exist, so you should delet manually the already existing table if you want to re-create it
	model.Base.metadata.create_all(engine)


def update_security_basic_info():
	# 方式1：查询tushare获取批量数据，批量删除数据库重复的记录，批量插入新数据
	data = pro.stock_basic(fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_status,list_date,delist_date,is_hs')
	# data.to_excel('tushare.xlsx')
	# todo: 去重，ts_code为主键

	if data.shape[0] == 0:
		print("get nothing from tushare, data.shape=", data.shape)
		return
	else:
		print("get %s rows from tushare, data.shape=" % data.shape[0], data.shape)

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete_all = model.SecurityBasicInfo.__table__.delete()
	conn.execute(ins_delete_all)
	# second, insert all rows
	ins = model.SecurityBasicInfo.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()


def update_balance_sheet(start_date, end_date, ts_code_list, step_number):
	if len(ts_code_list) == 0:
		print('ts_code_list is null')
		return

	data = pd.DataFrame()
	except_ts_code_list = []
	null_ts_code_list = []

	# get balance sheet data for each ts_code
	for ts_code in ts_code_list:
		try:
			d = pro.balancesheet(ts_code=ts_code, start_date=start_date, end_date=end_date, report_type='1')
		except:
			except_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare failed')
			continue

		if len(d) == 0:
			null_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare return 0 rows')
			continue
		
		print(ts_code, ' from tushare succeed')
		data = pd.concat([data, d], ignore_index=True)
		print("get total: %s rows" % len(data))
		sleep(0.1)	# 0.1 second

	if len(except_ts_code_list) > 0:
		print('except number: %s, except_ts_code_list: %s' % (len(except_ts_code_list), except_ts_code_list))
		save_list_to_txt(except_ts_code_list, 'except_ts_code_list_d_%s_%s_step%s.txt'%(start_date, end_date, step_number))

	if len(null_ts_code_list) > 0:
		print('null number: %s, null_ts_code_list: %s' % (len(null_ts_code_list), null_ts_code_list))
		save_list_to_txt(null_ts_code_list, 'null_ts_code_list_d_%s_%s_step%s.txt'%(start_date, end_date, step_number))
	
	if data.shape[0] == 0:
		print("get nothing from tushare, data.shape=", data.shape)
		return
	else:
		print("get %s rows from tushare, data.shape=" % data.shape[0], data.shape)

	# 去重，ts_code, ann_date, f_ann_date, end_date, report_type为主键
	# 将nan换成None
	data.drop_duplicates(['ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'], inplace=True)
	# print(data.loc[:, "htm_invest"])
	data = data.where(data.notnull(), None)
	# print(data.loc[:, "htm_invest"])

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.BalanceSheet.__table__.delete().where(
		and_(model.BalanceSheet.__table__.c.ann_date >= start_date, 
			 model.BalanceSheet.__table__.c.ann_date <= end_date, 
			 model.BalanceSheet.__table__.c.ts_code.in_(ts_code_list) ) )
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.BalanceSheet.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()


def update_bs_all(start_date, end_date, step=100, already_list_file='already_list.txt'):

	basics_df = pro.stock_basic(fields='ts_code,symbol,name')
	ts_code_list = basics_df.to_dict(orient='list')['ts_code']

	already_list = read_list_from_txt(already_list_file)

	ts_code_list = list(set(ts_code_list) - set(already_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		update_balance_sheet(start_date, end_date, sub_ts_code_list, i/step+1)
		already_list += sub_ts_code_list
		save_list_to_txt(already_list, 'already_list.txt')


def update_bs_from_file(start_date, end_date, ts_code_file):
	ts_code_list = read_list_from_txt(ts_code_file)
	update_balance_sheet(start_date, end_date, ts_code_list, step_number=1)


def update_income_statement(start_date, end_date, is_all_ts_code=True, ts_code_file=None):
	ts_code_list = []
	# get ts_code_list
	if is_all_ts_code == True:
		basics_df = pro.stock_basic(fields='ts_code,symbol,name')
		ts_code_list = basics_df.to_dict(orient='list')['ts_code']
	elif ts_code_file != None:
		ts_code_list = read_list_from_txt(ts_code_file)
		print("read_list_from_txt: ", ts_code_list)
	else: 
		print('ts_code_file is None')
		return

	# get balance sheet data for each ts_code
	data = pd.DataFrame()
	except_ts_code_list = []
	null_ts_code_list = []

	for ts_code in ts_code_list[0:3]:
		try:
			d = pro.income(ts_code=ts_code, start_date=start_date, end_date=end_date, report_type='1')
		except:
			except_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare failed')
			continue

		if len(d) == 0:
			null_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare return 0 rows')
			continue
		
		print(ts_code, ' from tushare succeed')
		data = pd.concat([data, d], ignore_index=True)
		print("get total: %s rows" % len(data))
		sleep(0.1)	# 0.1 second

	if len(except_ts_code_list) > 0:
		print('except number: %s, except_ts_code_list: %s' % (len(except_ts_code_list), except_ts_code_list))
		save_list_to_txt(except_ts_code_list, 'except_ts_code_list_is_%s_%s.txt'%(start_date, end_date))

	if len(null_ts_code_list) > 0:
		print('null number: %s, null_ts_code_list: %s' % (len(null_ts_code_list), null_ts_code_list))
		save_list_to_txt(null_ts_code_list, 'null_ts_code_list_is_%s_%s.txt'%(start_date, end_date))
	
	if data.shape[0] == 0:
		print("get nothing from tushare, data.shape=", data.shape)
		return
	else:
		print("get %s rows from tushare, data.shape=" % data.shape[0], data.shape)

	# 去重，ts_code, ann_date, f_ann_date, end_date, report_type为主键
	# 将nan换成None
	data.drop_duplicates(['ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'], inplace=True)
	# print(data.loc[:, "htm_invest"])
	data = data.where(data.notnull(), None)
	# print(data.loc[:, "htm_invest"])

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.IncomeStatement.__table__.delete().where(
		and_(model.IncomeStatement.__table__.c.ann_date >= start_date, 
			model.IncomeStatement.__table__.c.ann_date <= end_date))
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.IncomeStatement.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()



# 数据库结构维护：

# 1. 创建程序中定义而数据库中未创建的表，但不会删除程序中未定义而数据库中已有的表
# creat_all_tables_not_exist()

# 2. 基于Alembic
# 创建程序中定义而数据库中未创建的表，同时删除程序中未定义而数据库中已有的表。删除的表中的数据也会消失，无法恢复。
# 增加程序中定义的列，同时删除程序中未定义的列。删除的列数据也会消失，无法恢复。
# alembic revision --autogenerate -m 'comment'
# alembic upgrade head
# alembic downgrade -1	
# 注意，downgrade只能恢复upgrade之前的tables name和table columns，已经删除的数据不能恢复，所以要保证每次upgrade正确，不能指望downgrade恢复


########################################################


# 数据更新：

# 更新基础数据表security_basic_info
# update_security_basic_info()


# 更新资产负债表balance_sheet
# update_bs_all('20170101', '20180801')
# update_bs_from_file('20170101', '20180801', ts_code_file='except_ts_code_list_d_20170101_20180801_step1.0.txt')


# update_income_statement('20170101', '20180801', is_all_ts_code=True)

# 正在更新：20170101-20180801，balance_sheet






