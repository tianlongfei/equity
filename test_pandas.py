import pandas as pd
import numpy as np

def get_letter_type(letter):
	print(letter.lower())
	if letter.lower() in 'aeiou':
		return 'vowel'
	else:
		return 'consonant'

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 1, None, 'unknown'], 
				   'B': ['x', 'xy', 'y', 'z', 'y', 'z', 'z', 'y'], 
				   'C': np.random.randn(8)}, index=list('aaabbcfh'))
print(df)

df.loc[df['B'].str.contains('x'), 'A'] *= -1.0

print(df)

# print(df[df['B'].str.contains('x')])

print(df[df['B'].isin(['x'])])	
# groupby
# df.groupby(['B'])	# columns' list
# df.groupby(level=0)	# index level or index's name list
# gp_df = df.groupby([pd.Grouper(level=0), 'B']).sum()
# print(gp_df)


# 查找，替换，这里是查找Nan和None
# print(df.notnull())
# df = df.where(df.notnull(), other=None)
# print(df)
# df = df.where(df.notnull(), other=0.0)
# print(df)

# 检查重复，去重
# isdupulicate = df.duplicated(['A'])
# print(isdupulicate)
# print(df.drop_duplicates(['A'], inplace=True))


# 检索行，检索列，检索行列
# 检索行
# x = df['a':'b']
# x = df[['c','b']]	# wrong
# x = df.loc[['c', 'b'],] # right
# x = df[0:3]	# 检索行

# 检索列
# x = df['A']
# x = df[['A','B']]
# x = df.loc[:,['A', 'B']]
# print(x)

# 检索行列
# x = df.loc[['g', 'a'], ['A']]
# print(x)
# print(df.loc['a':'c', ['A']])


# 非常重要：DataFrame to Dict
# print(df.to_dict())
# print(df.to_dict(orient='index'))
# print(df.to_dict(orient='list'))


