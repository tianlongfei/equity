
# thelist = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]
# n = 20

# for i in range(0, len(thelist), n):
# 	print(i)
# 	print(thelist[i:i+n])



# # import time #导入 time类

# def func(a,b):
# 	start=time.clock()
# 	while True:
# 		end=time.clock()
# 		if int(end-start)==10:
# 			print('Warning: Timeout!!')
# 			break
# 	a=a+b
# 	print(a)

# func(1,2)


import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
print(__file__)
print(path.dirname( path.abspath(__file__) ))
print(path.dirname( path.dirname( path.abspath(__file__) ) ) )

# def test():
# 	a = 1
# 	b = 1
# 	if a > 0:
# 		b = 2
# 		print(b)
# 	print(b)

# test()



# thelist = ['a', 1, 'c', 2]
# print(','.join(map(str, thelist)))

# f = open('thelist.txt', 'w')
# f.write(','.join(map(str, thelist)))
# f.close()

# f = open('thelist.txt', 'w')
# f.write(','.join(map(str, thelist)))
# f.close()

# f = open('thelist.txt', 'r')
# s = f.read()
# thelist = s.split(',')
# f.close()
# print(thelist)


# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [1, 2, 3, 4, 0]
# list3 = list(set(list1) - set(list2))
# print(list3)

