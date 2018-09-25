from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)


end_date = '20180331'

# ts_code_list = ['000333.SZ', '000002.SZ']
# ts_code_str = '"' + '","'.join(map(str, ts_code_list)) + '"'	# list to string with ""

# sql = "select ts_code, end_date, cash_all, wc_net, ppe, intangible_goodwill, invest_available_for_sale, \
# invest_equity_investee, liability_interest_bearing, equity_net, invested_capital \
# from cap_struct_general_agg where ts_code in (%s) and end_date = '%s'" % (ts_code_str, end_date)

sql = "select ts_code, end_date, cash_all, wc_net, ppe, intangible_goodwill, invest_available_for_sale, \
invest_equity_investee, liability_interest_bearing, equity_net, invested_capital \
from cap_struct_general_agg where end_date = '%s'" % (end_date)


cap_struct = pd.read_sql_query(sql, engine)
# 计算 ratio
cap_struct.set_index(['ts_code', 'end_date'], inplace=True)
print(cap_struct)
cap_struct = cap_struct.div(cap_struct.invested_capital, axis='index')
print(cap_struct)

# 将DataFrame的某一列取出来，转换为numpy.array类型
x = cap_struct['cash_all']
print(len(x))
x = x.dropna()
print(len(x))
x = x.values	# type conversion: pandas.Series -> numpy.array
num_bins = 100

fig, (ax1, ax2) = plt.subplots(2, 1)
n, bins, patches = ax1.hist(x, num_bins, range=(0,1), density=True)
ax1.set_xlabel('cash_all')
ax1.set_ylabel('distribution')
ax1.set_title('cash_all distribution, %s' % end_date)

n, bins, patches = ax2.hist(x, num_bins, range=(0,1), density=True, cumulative=True)
ax2.set_xlabel('cash_all')
ax2.set_ylabel('distribution')
ax2.set_title('cash_all distribution cumulative, %s' % end_date)
ax2.set(xlim=[0, 1.1])
ax2.plot(np.linspace(0.8, 0.8, 10))

plt.show()





