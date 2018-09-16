import pandas as pd
import tushare as ts
from sqlalchemy import create_engine

ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
pro = ts.pro_api()

basics_df = pro.stock_basic(fields='ts_code,symbol,name')

bs_df = pd.DataFrame()
for ts_code in basics_df['ts_code'].head(2):
	bs = pro.balancesheet(ts_code=ts_code, start_date='20150101', end_date='20180930', report_type='1')
	bs_df = pd.concat([bs_df, bs], ignore_index=True)

print(bs_df)



# 评估聚框JoinQuant数据准确性：用美的2018年H1报告的BalanceSheet数据
# from jqdatasdk import auth, query, get_fundamentals, get_all_securities
# from jqdatasdk import balance, income, cash_flow
# auth('18510684718', 'tiandaochouqin88')
# q = query(balance).filter(balance.code == '000333.XSHE')
# df = get_fundamentals(q, '2018-10-15')
# df.to_excel('jq.xlsx')
# print(df)
# df = get_all_securities(types=['stock'], date=None)
# df.to_excel('secutiries.xlsx')
