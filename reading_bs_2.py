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

# 如果有ax11.set_title()，不加tight_layout()标题会挤到一起，如果加了图像会左右反转。
# 这时候，如果加了plt.style.use('seaborn')，图像左右反转的问题解决，但图像的区域将会按照坐标轴的比例来，以至于高度大于宽度，看上去很窄。
# 如果将ax11.set_title()一系列标题语句去除，图像将会正常。同时，在seaborn风格时，图像大小也会自适应subplot的整个区域。
# 可能是title或者xlabel的字体太大，应该进行一些frontsize的设置。应该是title或者xlabel的长度超过subplot的宽度的时候。
# 另外，要设置保存图像的长宽大小。
# 
# histogram的图返回值的意义，numpy计算histogram的方法。

# all styles available
# plt.style.use('bmh')
# plt.style.use('classic')
# plt.style.use('dark_background')
# plt.style.use('fast')
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
# plt.style.use('grayscale')
# plt.style.use('seaborn-bright')
# plt.style.use('seaborn-colorblind')
# plt.style.use('seaborn-dark-palette')
# plt.style.use('seaborn-dark')
# plt.style.use('seaborn-darkgrid')
# plt.style.use('seaborn-deep')
# plt.style.use('seaborn-muted')
# plt.style.use('seaborn-notebook')
# plt.style.use('seaborn-paper')
# plt.style.use('seaborn-pastel')
# plt.style.use('seaborn-poster')
# plt.style.use('seaborn-talk')
# plt.style.use('seaborn-ticks')
# plt.style.use('seaborn-white')
# plt.style.use('seaborn-whitegrid')
plt.style.use('seaborn')
# plt.style.use('Solarize_Light2')
# plt.style.use('tableau-colorblind10')
# plt.style.use('_classic_test')

plt.close('all')
fig, ((ax11, ax12, ax13), (ax21, ax22, ax23), (ax31, ax32, ax33)) = plt.subplots(3, 3, figsize=(13,7))

n, bins, patches = ax11.hist(cash_all, num_bins, range=(min_r, min(max_r, cash_all.max())), density=True)
# ax11.set_title('cash_all/invested_capital, %s' % end_date)
# ax11.set_xlabel('cash_all/invested_capital, %s' % end_date)
ax11.set_ylabel('density')

# n, bins, patches = ax2.hist(cash_all, num_bins, range=(min_r, max_r), density=True, cumulative=True)
# ax2.set_xlabel('cash_all')
# ax2.set_ylabel('acumulative')
# ax2.set(xlim=[0, 1])
# ax2.plot(np.linspace(0.8, 0.8, 10))


n, bins, patches = ax12.hist(wc_net, num_bins, range=(-1.0, min(max_r, wc_net.max())), density=True)
# ax12.set_title('wc_net/invested_capital, %s' % end_date)
# ax12.set_xlabel('wc_net/invested_capital, %s' % end_date)
ax12.set_ylabel('density')

n, bins, patches = ax13.hist(ppe, num_bins, range=(min_r, min(max_r, ppe.max())), density=True)
# ax13.set_title('ppe/invested_capital, %s' % end_date)
# ax13.set_xlabel('ppe/invested_capital, %s' % end_date)
ax13.set_ylabel('density')

n, bins, patches = ax21.hist(intangible_goodwill, num_bins, range=(min_r, min(max_r, intangible_goodwill.max())), density=True)
# ax21.set_title('intangible_goodwill/invested_capital, %s' % end_date)
# ax21.set_xlabel('intangible_goodwill/invested_capital, %s' % end_date)
ax21.set_ylabel('density')

n, bins, patches = ax22.hist(invest_available_for_sale, num_bins, range=(min_r, min(max_r, invest_available_for_sale.max())), density=True)
# ax22.set_title('invest_available_for_sale/invested_capital, %s' % end_date)
# ax22.set_xlabel('invest_available_for_sale/invested_capital, %s' % end_date)
ax22.set_ylabel('density')

n, bins, patches = ax23.hist(invest_equity_investee, num_bins, range=(min_r, min(max_r, invest_equity_investee.max())), density=True)
# ax23.set_title('invest_equity_investee/invested_capital, %s' % end_date)
# ax23.set_xlabel('invest_equity_investee/invested_capital, %s' % end_date)
ax23.set_ylabel('density')

n, bins, patches = ax31.hist(liability_interest_bearing, num_bins, range=(min_r, min(max_r, liability_interest_bearing.max())), density=True)
# ax31.set_title('liability_interest_bearing/invested_capital, %s' % end_date)
# ax31.set_xlabel('liability_interest_bearing/invested_capital, %s' % end_date)
ax31.set_ylabel('density')

plt.tight_layout()

plt.savefig('test.png')
plt.show()














