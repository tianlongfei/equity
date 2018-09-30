from sqlalchemy import create_engine
from sqlalchemy.sql.expression import and_
import pandas as pd
import model
import tushare as ts
from mystoredata import save_list_to_txt, read_list_from_txt

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)

def update_category_bs():
	# delete all data and insert
	data = pd.read_excel('resource/category.xlsx', 'balance', index_col=None)
	data = data.where(data.notnull(), None)
	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.CategoryBalanceSheet.__table__.delete()
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.CategoryBalanceSheet.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()



def update_category_bs_agg():
	# delete all data and insert
	data = pd.read_excel('resource/category.xlsx', 'agg', index_col=None)
	data = data.where(data.notnull(), None)
	data_dict = data.to_dict(orient='index')
	values = list(data_dict.values())

	# get a connection to database
	conn = engine.connect()
	# first, delete all rows
	ins_delete = model.CategoryBalanceSheetAgg.__table__.delete()
	conn.execute(ins_delete)
	# second, insert all rows
	ins = model.CategoryBalanceSheetAgg.__table__.insert()
	conn.execute(ins, values)
	# close connection
	conn.close()


