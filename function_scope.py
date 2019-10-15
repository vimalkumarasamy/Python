my_var='I am the first version'



def test2():
	print(my_var)

def test():
	test2()
	global my_var
	my_var='I have been changed'
	test2()


print(my_var)
test()