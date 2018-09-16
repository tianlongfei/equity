from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from model import Base

# engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=True)

class Test(Base):
	__tablename__ = 'test_2'

	ts_code = Column(String(20), primary_key=True)	# TS股票代码
	symbol = Column(String(20))	# 股票代码
	name = Column(String(50))	# 股票名称
	fullname = Column(String(200)) # 股票全称 
	enname = Column(String(500))	# 英文全称
	exchange_id = Column(String(20))	# 交易所代码  
	curr_type = Column(String(20))	# 交易货币
	list_status = Column(String(20))	# 上市状态 L上市 D退市 P暂停上市
	list_date = Column(String(20))	# 上市日期
	delist_date = Column(String(20))	# 退市日期
	is_hs = Column(String(20))	# 是否沪深港通标的，N否 H沪股通 S深股通

