from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建基类
Base = declarative_base()
# 创建具体表格的类
class SecurityBasicInfo(Base):
	__tablename__ = 'security_basic_info':

	id = Column(Integer(8), primary_key=True)
	ts_code = Column(String(20))
	symbol = Column(String(20))
	name = Column(String(20))
	exchange_id = Column(String(20))
	curr_type = Column(String(20))
	list_status = Column(String(20))
	list_date = Column(String(20))
	delist_date = Column(String(20))
	is_hs = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
