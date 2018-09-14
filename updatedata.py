import pandas as pd
import tushare as ts
from sqlalchemy import create_engine

ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
pro = ts.pro_api()

basics_df = pro.stock_basic(
	list_status='L', 
	fields='ts_code, symbol, name, exchange_id, curr_type, list_status, list_date, delist_date, is_hs'
	)


# basics_df.to_excel('basics.xlsx', sheet_name='basics')

# engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)
# basics_df.to_sql('security_basics_info', engine, if_exists='replace', index=True, index_label='id', chunksize=500)

bs_df = pd.DataFrame()
for ts_code in basics_df['ts_code'].head(2):
	bs = pro.balancesheet(ts_code=ts_code, start_date='20150101', end_date='20180930')
	bs_df = pd.concat([bs_df, bs], ignore_index=True)

print(bs_df)
engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)
bs_df.to_sql('balancesheet', engine, if_exists='replace', index=True, index_label='id', chunksize=500)




