from sqlalchemy import create_engine
from sqlalchemy.sql.expression import and_
from sqlalchemy.sql import select
import pandas as pd
import model
import tushare as ts
from mystoredata import save_list_to_txt, read_list_from_txt
import datetime

ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
pro = ts.pro_api()

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)


index_code_dict = {'399300.SZ': '沪深300', 
				   '000905.SH': '中证500',
				   '000852.SH': '中证1000',
				   '000903.SH': '中证100', 
				   '000904.SH': '中证200', 
				   '000906.SH': '中证800', 
				   '000001.SH': '上证综指',
				   '399001.SZ': '深证成指',
				   '399005.SZ': '中小板指',
				   '399006.SZ': '创业板指'
}

def update_all_index_weight(start_date, end_date):
	date_range = pd.date_range(start_date, end_date).tolist()

	for index_code in index_code_dict:
		data = pd.DataFrame()
		for trade_date in date_range:
			df = pd.DataFrame()
			trade_date = trade_date.strftime('%Y%m%d')	# type conversion: datetime.datetime to string
			try:
				df = pro.index_weight(index_code=index_code, trade_date=trade_date)
			except:
				print('error when get data: ', index_code, trade_date)
			
			if len(df) == 0:
				continue
			data = data.append(df, ignore_index=True)
			print(index_code, trade_date, len(data), 'rows data')

		if len(data) == 0:
			print(index_code, trade_date, len(data), 'rows data')
			continue

		# save to database
		data_dict = data.to_dict(orient='index')
		values = list(data_dict.values())

		# get a connection to database
		conn = engine.connect()
		# first, delete all rows
		delete = model.IndexWeight.__table__.delete().where(
			and_(model.IndexWeight.__table__.c.trade_date >= start_date, 
				 model.IndexWeight.__table__.c.trade_date <= end_date,
				 model.IndexWeight.__table__.c.index_code == index_code) )

		conn.execute(delete)

		# second, insert all rows
		ins = model.IndexWeight.__table__.insert()
		conn.execute(ins, values)
		conn.close()

		print('update success！')


# 测试
# start_date = '20180101'
# end_date = '20180331'
# update_all_index_weight(start_date, end_date)


# df = pro.index_basic(market='SZSE')
# df.to_excel('深证指数.xlsx')

# df = pro.index_basic(market='SSE')
# df.to_excel('上证指数.xlsx')




