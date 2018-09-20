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


def update_balance_sheet(start_date, end_date, ts_code_list):
	if len(ts_code_list) == 0:
		print('ts_code_list is null')
		return

	data = pd.DataFrame()
	except_ts_code_list = []

	# get balance sheet data for each ts_code
	for ts_code in ts_code_list:
		try:
			print('trying to get ts_code = %s' % ts_code)
			d = pro.balancesheet(ts_code=ts_code, start_date=start_date, end_date=end_date, report_type='1')
		except:
			except_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare failed')
			continue
	
		print('%s from tushare succeed, return %s rows' % (ts_code, len(d)))

		if len(d) == 0:
			continue

		data = pd.concat([data, d], ignore_index=True)
		print("get total: %s rows" % len(data))
		sleep(0.1)	# 0.1 second

	print("totally get %s rows from tushare, data.shape=" % data.shape[0], data.shape)
	print('except number: %s, except_ts_code_list: %s' % (len(except_ts_code_list), except_ts_code_list))

	if data.shape[0] == 0:
		return except_ts_code_list

	# 去重，ts_code, ann_date, f_ann_date, end_date, report_type为主键
	# 将nan换成None
	data.drop_duplicates(['ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'], inplace=True)
	# print(data.loc[:, "htm_invest"])
	data = data.where(data.notnull(), None)
	# print(data.loc[:, "htm_invest"])

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	eff_ts_code_list = list(set(ts_code_list) - set(except_ts_code_list))

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.BalanceSheet.__table__.delete().where(
		and_(model.BalanceSheet.__table__.c.ann_date >= start_date, 
			 model.BalanceSheet.__table__.c.ann_date <= end_date, 
			 model.BalanceSheet.__table__.c.ts_code.in_(eff_ts_code_list) ) )
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.BalanceSheet.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()

	return except_ts_code_list


def update_bs_all(start_date, end_date, step=50, already_list_file='p_already_list.txt', 
	except_list_file='p_except_list.txt'):

	basics_df = pro.stock_basic(fields='ts_code,symbol,name')
	ts_code_list = basics_df.to_dict(orient='list')['ts_code']

	already_list = read_list_from_txt(already_list_file)

	# 无需从except_list中读取，因为already_list中已经除去exception的ts_code，所以except_list每次从零开始，只保存本次执行过程中断前的except_list即可
	except_list = []	# 无需从except_list中读取，因为already_list中已经除去exception的ts_code，所以except_list每次从零开始，只保存本次执行过程中断前的except_list即可

	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取BalanceSheet的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_balance_sheet(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_bs_from_file(ts_code_file, start_date, end_date, step=50, already_list_file='p_from_file_already_list.txt', 
	except_list_file='p_from_file_except_list.txt'):

	ts_code_list = read_list_from_txt(ts_code_file)
	already_list = read_list_from_txt(already_list_file)
	except_list = []

	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取BalanceSheet的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_balance_sheet(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_income_statement(start_date, end_date, ts_code_list):
	if len(ts_code_list) == 0:
		print('ts_code_list is null')
		return

	data = pd.DataFrame()
	except_ts_code_list = []

	# get balance sheet data for each ts_code
	for ts_code in ts_code_list:
		try:
			print('trying to get ts_code = %s' % ts_code)
			d = pro.income(ts_code=ts_code, start_date=start_date, end_date=end_date, report_type='1')
		except:
			except_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare failed')
			continue
	
		print('%s from tushare succeed, return %s rows' % (ts_code, len(d)))

		if len(d) == 0:
			continue

		data = pd.concat([data, d], ignore_index=True)
		print("get total: %s rows" % len(data))
		sleep(0.1)	# 0.1 second

	print("get %s rows from tushare, data.shape=" % data.shape[0], data.shape)
	print('except number: %s, except_ts_code_list: %s' % (len(except_ts_code_list), except_ts_code_list))

	if data.shape[0] == 0:
		return except_ts_code_list

	# 去重，ts_code, ann_date, f_ann_date, end_date, report_type为主键
	# 将nan换成None
	data.drop_duplicates(['ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'], inplace=True)
	# print(data.loc[:, "htm_invest"])
	data = data.where(data.notnull(), None)
	# print(data.loc[:, "htm_invest"])

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	eff_ts_code_list = list(set(ts_code_list) - set(except_ts_code_list))

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.IncomeStatement.__table__.delete().where(
		and_(model.IncomeStatement.__table__.c.ann_date >= start_date, 
			 model.IncomeStatement.__table__.c.ann_date <= end_date, 
			 model.IncomeStatement.__table__.c.ts_code.in_(eff_ts_code_list) ) )
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.IncomeStatement.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()

	return except_ts_code_list


def update_is_all(start_date, end_date, step=50, already_list_file='p_already_list.txt', 
	except_list_file='p_except_list.txt'):

	basics_df = pro.stock_basic(fields='ts_code,symbol,name')
	ts_code_list = basics_df.to_dict(orient='list')['ts_code']

	already_list = read_list_from_txt(already_list_file)
	except_list = []
	
	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取IncomeStatement的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_income_statement(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_is_from_file(ts_code_file, start_date, end_date, step=50, already_list_file='p_from_file_already_list.txt', 
	except_list_file='p_from_file_except_list.txt'):

	ts_code_list = read_list_from_txt(ts_code_file)
	already_list = read_list_from_txt(already_list_file)
	except_list = []

	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取IncomeStatement的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_income_statement(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_cash_flow(start_date, end_date, ts_code_list):
	if len(ts_code_list) == 0:
		print('ts_code_list is null')
		return

	data = pd.DataFrame()
	except_ts_code_list = []

	# get balance sheet data for each ts_code
	for ts_code in ts_code_list:
		try:
			print('trying to get ts_code = %s' % ts_code)
			d = pro.cashflow(ts_code=ts_code, start_date=start_date, end_date=end_date, report_type='1')
		except:
			except_ts_code_list.append(ts_code)
			print(ts_code, ' from tushare failed')
			continue
	
		print('%s from tushare succeed, return %s rows' % (ts_code, len(d)))

		if len(d) == 0:
			continue

		data = pd.concat([data, d], ignore_index=True)
		print("get total: %s rows" % len(data))
		sleep(0.1)	# 0.1 second

	print("get %s rows from tushare, data.shape=" % data.shape[0], data.shape)
	print('except number: %s, except_ts_code_list: %s' % (len(except_ts_code_list), except_ts_code_list))

	if data.shape[0] == 0:
		return except_ts_code_list

	# 去重，ts_code, ann_date, f_ann_date, end_date, report_type为主键
	# 将nan换成None
	data.drop_duplicates(['ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'], inplace=True)
	# print(data.loc[:, "htm_invest"])
	data = data.where(data.notnull(), None)
	# print(data.loc[:, "htm_invest"])

	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())
	eff_ts_code_list = list(set(ts_code_list) - set(except_ts_code_list))

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.CashFlowSheet.__table__.delete().where(
		and_(model.CashFlowSheet.__table__.c.ann_date >= start_date, 
			 model.CashFlowSheet.__table__.c.ann_date <= end_date, 
			 model.CashFlowSheet.__table__.c.ts_code.in_(eff_ts_code_list) ) )
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.CashFlowSheet.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()

	return except_ts_code_list


def update_cf_all(start_date, end_date, step=50, already_list_file='p_already_list.txt', 
	except_list_file='p_except_list.txt'):

	basics_df = pro.stock_basic(fields='ts_code,symbol,name')
	ts_code_list = basics_df.to_dict(orient='list')['ts_code']

	already_list = read_list_from_txt(already_list_file)
	except_list = []
	
	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取CashFlowSheet的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_cash_flow(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_cf_from_file(ts_code_file, start_date, end_date, step=50, already_list_file='p_from_file_already_list.txt', 
	except_list_file='p_from_file_except_list.txt'):

	ts_code_list = read_list_from_txt(ts_code_file)
	already_list = read_list_from_txt(already_list_file)
	except_list = []

	ts_code_list = list(set(ts_code_list) - set(already_list))
	print('开始获取CashFlowSheet的数据，ts_code的数量：%s个' % len(ts_code_list))

	for i in range(0, len(ts_code_list), step):
		sub_ts_code_list = ts_code_list[i : i+step]
		e = update_cash_flow(start_date, end_date, sub_ts_code_list)

		except_list += e
		al = list(set(sub_ts_code_list) - set(e))
		already_list += al

		save_list_to_txt(already_list, already_list_file)
		save_list_to_txt(except_list, except_list_file)


def update_category():
	# model.CategoryBalanceSheet
	pass