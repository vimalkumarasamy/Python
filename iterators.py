my_list = [4, 7, 0, 3]

# get an iterator using iter()
#my_iter = iter(my_list)
my_iter=my_list.__iter__()

print(my_iter)
## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
#next(my_iter)

##This is how for loop is implemented, using __iter__ and __next__

iterable=[4,7,0,3]

for element in iterable:
    # do something with element
    print (element)
##Is actually implemented as.

# create an iterator object from that iterable
iter_obj = iter(iterable)
# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break