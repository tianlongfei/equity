from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)
Base = declarative_base()

class SecurityBasicInfo(Base):
	__tablename__ = 'security_basic_info'

	ts_code = Column(String(20), primary_key=True)
	symbol = Column(String(20))
	name = Column(String(20))
	exchange_id = Column(String(20))
	curr_type = Column(String(20))
	list_status = Column(String(20))
	list_date = Column(String(20))
	delist_date = Column(String(20))
	is_hs = Column(String(20))

	def __info__(self):
		return 'SecurityBasicInfo(%s, %s, %s)' % (self.ts_code, self.symbol, self.name)

Base.metadata.create_all(engine)

a = SecurityBasicInfo(ts_code='000333.SZ', symbol='000333', name='美的集团')
print(a.__info__())


