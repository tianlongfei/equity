
def save_list_to_txt(thelist, thefile):
	f = open(thefile, 'w')
	f.write(','.join(map(str, thelist)))
	f.close()


def read_list_from_txt(thefile):
	f = open(thefile, 'r')
	s = f.read()
	f.close()
	thelist = s.split(',')
	return thelist

