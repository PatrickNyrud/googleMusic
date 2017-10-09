def test():
	var = test2()
	print var

def test2():
	return test3()

def test3():
	return "y"


test()