def change_inputs(i_type, f_type, s_type, l_type, t_type): 
	'''
	notice that the variable names inside the function do no have to match the names of the variables names outside the function.
	Inside the function the following assignments take place
	i_type = int_type  # a copy is made, so changes made to the variable inside the function does not affect the variable outside the function. 
	f_type = float_type # a copy is made, so changes made to the variable inside the function does not affect the variable outside the function. 
	s_type = str_type # a copy is made, so changes made to the variable inside the function does not affect the variable outside the function. 
	l_type = list_type # the variable l_type now points to list_type, so changes made to l_type will show up in list_type
	t_type = tuple_type # Remember, tuple are immutable, so you cannot change them anyways
	'''

	print('-'*80, '\n')
	print('Values inside function before change')
	print('i_type: ', i_type)
	print('f_type: ', f_type)
	print('s_type: ', s_type)
	print('l_type: ', l_type)
	print('t_type: ', t_type)



	i_type = 4
	f_type = 6.28
	s_type = 'World!'
	l_type[1] = 4
	# t_type[1] = 4 # this is illegal. you cannot do this. Lists are mutable and tuple are immutable 

	print('-'*80, '\n')
	print('Values inside function after change')
	print('i_type: ', i_type)
	print('f_type: ', f_type)
	print('s_type: ', s_type)
	print('l_type: ', l_type)
	print('t_type: ', t_type)




## variable assignments
int_type = 2
float_type = 3.14
str_type = 'Hello!'
list_type = [1, 2, 3]
tuple_type = (11, 22, 33)


## print variables
print('-'*80, '\n')
print('Values before function call')
print('int_type: ', int_type)
print('float_type: ', float_type)
print('str_type: ', str_type)
print('list_type: ', list_type)
print('tuple_type: ', tuple_type)




## call function 
change_inputs(int_type, float_type, str_type, list_type, tuple_type)


print('-'*80, '\n')
print('Values after function call')
print('int_type: ', int_type)
print('float_type: ', float_type)
print('str_type: ', str_type)
print('list_type: ', list_type, ' --> this has changed!')
print('tuple_type: ', tuple_type)


'''
The instruction for problem #6 says that you need to modify the list and NOT return it because the changes will be preserved. 
'''