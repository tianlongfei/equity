import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
				   'size': list('SSMMMLL'),
				   'weight': [8, 10, 11, 1, 20, 12, 12],
				   'height': [8, 10, 11, 1, 20, 12, 12],
				   'adult' : [False] * 5 + [True] * 2})
print(df)

# 列相乘
# a = df[['weight', 'height']].multiply(df['height'], axis='index')
# print(a)

# aggregate
# gpd = df.groupby('animal')
# gpd = gpd.agg({'weight': 'sum', 'size': 'count'})	# dict {column name: aggregate function}
# print(gpd)

# transform: 对group后的每一组的每一列的每个值操作，最后返回group之前的df的结构
# g = df.groupby('animal')['weight']
# df['weight_salarize'] = g.transform(lambda x: x/x.sum())
# print(df)

# apply可以替代transform和aggregate，但不自动检查列是否适合函数(比如对str类型的行进行sum)，不合适会报错，但后两者可以自动去掉不合适函数的行


# df_1 = df.groupby('animal').apply(lambda subf: subf[:])
# print(df_1)

# for name, gp in df.groupby('animal'):
# 	print(gp)


comp_type_for_index = {
	'w_all_add': '所有企业，简单相加', 
	'w_all_equal': '所有企业，等权重，等于简单相加/企业总数，跟标准权重具有可比性', 
	'w_all_std': '所有企业，标准权重',
	'w_general_add': '一般工商企业，简单相加', 
	'w_general_equal': '一般工商企业，等权重，等于简单相加/企业总数', 
	'w_general_std': '一般工商企业，标准权重'
}

print(list(comp_type_for_index.keys()))


# pandas 基本功
# DataFrame增加一列，等于另外两列的和，另外列的函数，另一列符合某些条件时赋值

'matplotlib'
'整体风格，style'
# print(plt.style.available)
# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']

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
# plt.style.use('seaborn')
# plt.style.use('Solarize_Light2')
# plt.style.use('tableau-colorblind10')
# plt.style.use('_classic_test')

'各部分颜色，color，density=True后，坐标加起来不等于1，返回值'


'透明度，alpha'
# 从0-1的数字


# np.random.seed(19680801)

# dt = 0.01
# t = np.arange(0, 30, dt)
# nse1 = np.random.randn(len(t))                 # white noise 1
# nse2 = np.random.randn(len(t))                 # white noise 2

# # Two signals with a coherent part at 10Hz and a random part
# s1 = np.sin(2 * np.pi * 10 * t) + nse1
# s2 = np.sin(2 * np.pi * 10 * t) + nse2

# fig, axs = plt.subplots(2, 2)
# axs[0][0].plot(t, s1, t, s2)
# axs[0][0].set_xlim(0, 2)
# axs[0][0].set_xlabel('time, this is a test of title length, when the title is too long, what will happen', 
# 	fontsize='medium', wrap=True, bbox=dict(facecolor='g', edgecolor='blue', alpha=0.65 ))
# axs[0][0].set_ylabel('s1 and s2')
# axs[0][0].grid(True)

# cxy, f = axs[0][1].cohere(s1, s2, 256, 1. / dt)
# axs[0][1].set_ylabel('coherence')

# fig.tight_layout()
# plt.show()




