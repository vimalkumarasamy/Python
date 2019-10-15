filename = input('What is the name of the file? ')
header = False
data_array = []
with open(filename, 'r') as fp:
    for line in fp:
        if header is False:
            header = line.strip().split('\t')
            continue


        # number of elements in header should match with number of elements in line
        # so that key value pairs are matched and finally written into an array/list containing all the dictionariess
        data_array.append(dict(zip(header, line.strip().split('\t'))))

from pprint import pprint
pprint(data_array)