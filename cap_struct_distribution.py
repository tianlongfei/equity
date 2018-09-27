from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def get_array(df, col_name):
	col = df[col_name]
	col = col.dropna()	# drop nan value
	col = col.values	# type conversion: pandas.Series -> numpy.array
	return col


def draw_hist(ax, data, num_bins, min_r, max_r, xlabel):
	n, bins, patches = ax.hist(data, num_bins, weights=np.ones(len(data))/len(data), range=(min_r, max_r))
	ax.set_xlabel(xlabel)
	ax.set_ylabel('density')
	ax.set_xlim(min_r, max_r)

	ax_twin = ax.twinx()
	n, bins, patches = ax_twin.hist(data, num_bins, range=(min_r, max_r), histtype='step', density=True, cumulative=True, color='r', alpha=0.8)
	ax_twin.set_ylabel('acumulative')


end_date = '20180331'

sql = "select ts_code, end_date, cash_all, wc_net, ppe, intangible_goodwill, invest_available_for_sale, \
invest_equity_investee, liability_interest_bearing, equity_net, invested_capital \
from cap_struct_general_agg where end_date = '%s'" % (end_date)

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)
cap_struct = pd.read_sql_query(sql, engine)

# 计算 ratio
cap_struct.set_index(['ts_code', 'end_date'], inplace=True)
cap_struct = cap_struct.div(cap_struct.invested_capital, axis='index')
cols = cap_struct.columns

num_bins = 100
min_r = 0.0
max_r = 1.0

# plt.style.use('bmh')
plt.close('all')
fig = plt.figure(figsize=(13.66, 6.36))	# 大小：1366*636
gs = gridspec.GridSpec(3, 3)

for i in range(0,3):
	for j in range(0,3):
		if i*3+j > len(cols)-3:
			break

		col_name = cols[ i*3+j ]
		data = get_array(cap_struct, col_name)

		xlabel = '%s/IC, %s' % (col_name, end_date)
		if col_name == 'wc_net':
			min_r = -1.0
		else:
			min_r = 0.0

		ax = fig.add_subplot(gs[i, j])
		draw_hist(ax, data, num_bins, min_r, max_r, xlabel)

gs.tight_layout(fig)

plt.savefig('test.png')
plt.show()

