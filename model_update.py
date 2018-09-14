from sqlalchemy import create_engine
import model
import tushare as ts
from jqdatasdk import auth, query, get_fundamentals, get_all_securities
from jqdatasdk import balance, income, cash_flow


# engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=True)

# ts.set_token('678fe21fd6c9fb6a50b36d86ed86f36f5d95f70ad0444bb12719eeeb')
# pro = ts.pro_api()
# data = pro.stock_basic(fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_status,list_date,delist_date,is_hs')
# data.to_excel('tushare.xlsx')

auth('18510684718', 'tiandaochouqin88')
q = query(balance).filter(balance.code == '000333.XSHE')
df = get_fundamentals(q, '2018-10-15')
df.to_excel('jq.xlsx')
print(df)

# df = get_all_securities(types=['stock'], date=None)
# df.to_excel('secutiries.xlsx')