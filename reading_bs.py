from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
plt.style.use('seaborn')

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)

# end_date = '20180331'
# ts_code_list = ['000333.SZ', '000002.SZ']
# ts_code_str = '"' + '","'.join(map(str, ts_code_list)) + '"'	# list to string with ""

# sql = "select ts_code, end_date, cash_all, wc_net, ppe, intangible_goodwill, invest_available_for_sale, \
# invest_equity_investee, liability_interest_bearing, equity_net, invested_capital \
# from cap_struct_general_agg where ts_code in (%s) and end_date = '%s'" % (ts_code_str, end_date)

end_date = '20180331'
sql = "select ts_code, end_date, cash_all, wc_net, ppe, intangible_goodwill, invest_available_for_sale, \
invest_equity_investee, liability_interest_bearing, equity_net, invested_capital \
from cap_struct_general_agg where end_date = '%s'" % (end_date)

cap_struct = pd.read_sql_query(sql, engine)

# 计算 ratio
cap_struct.set_index(['ts_code', 'end_date'], inplace=True)
cap_struct = cap_struct.div(cap_struct.invested_capital, axis='index')

# 将DataFrame的某一列取出来，转换为numpy.array类型
cash_all = cap_struct['cash_all']
cash_all = cash_all.dropna()	# drop nan value
cash_all = cash_all.values	# type conversion: pandas.Series -> numpy.array

wc_net = cap_struct['wc_net']
wc_net = wc_net.dropna()	# drop nan value
wc_net = wc_net.values	# type conversion: pandas.Series -> numpy.array

ppe = cap_struct['ppe']
ppe = ppe.dropna()	# drop nan value
ppe = ppe.values	# type conversion: pandas.Series -> numpy.array

intangible_goodwill = cap_struct['intangible_goodwill']
intangible_goodwill = intangible_goodwill.dropna()	# drop nan value
intangible_goodwill = intangible_goodwill.values	# type conversion: pandas.Series -> numpy.array

invest_available_for_sale = cap_struct['invest_available_for_sale']
invest_available_for_sale = invest_available_for_sale.dropna()	# drop nan value
invest_available_for_sale = invest_available_for_sale.values	# type conversion: pandas.Series -> numpy.array

invest_equity_investee = cap_struct['invest_equity_investee']
invest_equity_investee = invest_equity_investee.dropna()	# drop nan value
invest_equity_investee = invest_equity_investee.values	# type conversion: pandas.Series -> numpy.array

liability_interest_bearing = cap_struct['liability_interest_bearing']
liability_interest_bearing = liability_interest_bearing.dropna()	# drop nan value
liability_interest_bearing = liability_interest_bearing.values	# type conversion: pandas.Series -> numpy.array

num_bins = 100
min_r = 0.0
max_r = 1.0

plt.close('all')
# plt.rcParams['figure.constrained_layout.use'] = True
# fig = plt.figure(figsize=(100, 100))
fig = plt.figure()
gs = gridspec.GridSpec(3, 3)

ax11 = fig.add_subplot(gs[0, 0])
n, bins, patches = ax11.hist(cash_all, num_bins, range=(min_r, min(max_r, cash_all.max())), density=True)
ax11.set_title('cash_all/invested_capital, %s' % end_date)
ax11.set_ylabel('density')

# n, bins, patches = ax2.hist(cash_all, num_bins, range=(min_r, max_r), density=True, cumulative=True)
# ax2.set_xlabel('cash_all')
# ax2.set_ylabel('acumulative')
# ax2.set(xlim=[0, 1])
# ax2.plot(np.linspace(0.8, 0.8, 10))


ax12 = fig.add_subplot(gs[0, 1])
n, bins, patches = ax12.hist(wc_net, num_bins, range=(-1.0, min(max_r, wc_net.max())), density=True)
ax12.set_title('wc_net/invested_capital, %s' % end_date)
ax12.set_ylabel('density')

ax13 = fig.add_subplot(gs[0, 2])
n, bins, patches = ax13.hist(ppe, num_bins, range=(min_r, min(max_r, ppe.max())), density=True)
ax13.set_title('ppe/invested_capital, %s' % end_date)
ax13.set_ylabel('density')

ax21 = fig.add_subplot(gs[1, 0])
n, bins, patches = ax21.hist(intangible_goodwill, num_bins, range=(min_r, min(max_r, intangible_goodwill.max())), density=True)
ax21.set_title('intangible_goodwill/invested_capital, %s' % end_date)
ax21.set_ylabel('density')

ax22 = fig.add_subplot(gs[1, 1])
n, bins, patches = ax22.hist(invest_available_for_sale, num_bins, range=(min_r, min(max_r, invest_available_for_sale.max())), density=True)
ax22.set_title('invest_available_for_sale/invested_capital, %s' % end_date)
ax22.set_ylabel('density')

ax23 = fig.add_subplot(gs[1, 2])
n, bins, patches = ax23.hist(invest_equity_investee, num_bins, range=(min_r, min(max_r, invest_equity_investee.max())), density=True)
ax23.set_title('invest_equity_investee/invested_capital, %s' % end_date)
ax23.set_ylabel('density')

ax31 = fig.add_subplot(gs[2, :])
n, bins, patches = ax31.hist(liability_interest_bearing, num_bins, range=(min_r, min(max_r, liability_interest_bearing.max())), density=True)
ax31.set_title('liability_interest_bearing/invested_capital, %s' % end_date)
ax31.set_ylabel('density')

gs.tight_layout(fig, pad=0.1, h_pad=0.1, w_pad=0.1)
plt.show()


