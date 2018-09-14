from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=True)
Base = declarative_base()

class User(Base):
	__tablename__ = 'test_sqlalchemy'

	id = Column(Integer(8), primary_key=True)
	name = Column(String(20))
	