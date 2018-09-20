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
