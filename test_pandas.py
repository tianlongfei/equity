import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 1, None], 
				   'B': ['x', 'y', 'z', 'w', 'v', 'u', 'v']}, index=list('abcdefg'))
print(df)

print(df.notnull())
print(df.where(df.notnull(), other=None))
print(df)

# 检查重复，去重
# isdupulicate = df.duplicated(['A'])
# print(isdupulicate)
# print(df.drop_duplicates(['A'], inplace=True))


# 检索行，检索列
# x = df['A']	# 检索列
# x = df[['A','B']] # 检索列
# x = df['a':'a']	# 检索行
# x = df[0:3]	# 检索行
# print(x)


# 非常重要：DataFrame to Dict
# print(df.to_dict())
# print(df.to_dict(orient='index'))
# print(df.to_dict(orient='list'))


