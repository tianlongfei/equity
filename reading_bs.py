from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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


# fig, ((ax11, ax12, ax13),(ax21, ax22, ax23),(ax31, ax32, ax33)) = plt.subplots(3, 3)
plt.rcParams['figure.constrained_layout.use'] = True
fig = plt.figure(figsize=(100, 100))
gs = gridspec.GridSpec(3, 3, figure=fig)

ax11 = fig.add_subplot(gs[0, 0])
n, bins, patches = ax11.hist(cash_all, num_bins, range=(min_r, max_r), density=True)
ax11.set_title('cash_all distribution, %s' % end_date)
ax11.set_ylabel('density')
ax11.set(xlim=[min_r, max_r])

# n, bins, patches = ax2.hist(cash_all, num_bins, range=(min_r, max_r), density=True, cumulative=True)
# ax2.set_xlabel('cash_all')
# ax2.set_ylabel('acumulative')
# ax2.set(xlim=[0, 1])
# ax2.plot(np.linspace(0.8, 0.8, 10))


ax12 = fig.add_subplot(gs[0, 1])
n, bins, patches = ax12.hist(wc_net, num_bins, range=(-1.0, max_r), density=True)
ax12.set_title('wc_net distribution, %s' % end_date)
ax12.set_ylabel('density')
ax12.set(xlim=[-1, 1])

ax13 = fig.add_subplot(gs[0, 2])
n, bins, patches = ax13.hist(ppe, num_bins, range=(min_r, max_r), density=True)
ax13.set_title('ppe distribution, %s' % end_date)
ax13.set_ylabel('density')
ax13.set(xlim=[min_r, max_r])

ax21 = fig.add_subplot(gs[1, 0])
n, bins, patches = ax21.hist(intangible_goodwill, num_bins, range=(min_r, max_r), density=True)
ax21.set_title('intangible_goodwill distribution, %s' % end_date)
ax21.set_ylabel('density')
ax21.set(xlim=[min_r, max_r])

ax22 = fig.add_subplot(gs[1, 1])
n, bins, patches = ax22.hist(invest_available_for_sale, num_bins, range=(min_r, max_r), density=True)
ax22.set_title('invest_available_for_sale distribution, %s' % end_date)
ax22.set_ylabel('density')
ax22.set(xlim=[min_r, max_r])

ax23 = fig.add_subplot(gs[1, 2])
n, bins, patches = ax23.hist(invest_equity_investee, num_bins, range=(min_r, max_r), density=True)
ax23.set_title('invest_equity_investee distribution, %s' % end_date)
ax23.set_ylabel('density')
ax23.set(xlim=[min_r, max_r])

ax31 = fig.add_subplot(gs[2, 0])
n, bins, patches = ax31.hist(liability_interest_bearing, num_bins, range=(min_r, max_r), density=True)
ax31.set_title('liability_interest_bearing distribution, %s' % end_date)
ax31.set_ylabel('density')
ax31.set(xlim=[min_r, max_r])

plt.savefig('test.png', dpi=100)
plt.show()

