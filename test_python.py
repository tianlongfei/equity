

# def test():
# 	a = 1
# 	b = 1
# 	if a > 0:
# 		b = 2
# 		print(b)
# 	print(b)

# test()



thelist = ['a', 1, 'c', 2]
print(','.join(map(str, thelist)))

f = open('thelist.txt', 'w')
f.write(','.join(map(str, thelist)))
f.close()

f = open('thelist.txt', 'r')
s = f.read()
thelist = s.split(',')
f.close()
print(thelist)

