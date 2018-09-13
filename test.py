import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 
				   'B': ['x', 'y', 'z', 'w', 'v']}, index=list('abcde'))
print(df)
x = df['A']	# 检索列
x = df[['A','B']] # 检索列
x = df['a':'a']	# 检索行
x = df[0:3]	# 检索行
print(x)

