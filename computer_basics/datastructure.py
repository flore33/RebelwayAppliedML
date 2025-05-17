import array as arr


my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)
print(type(my_list))

my_array = arr.array('f', [1,2,3,4,5])
print(my_array)
print(type(my_array))

#containers
a = [[1,2,3,4,8], [5,6,7,8,]]
#array of arrays 
#nested containers, containers don't have to be quals

#tensor
tensor = [[[1,2,3,4], [5,6,7,8]], [[9,10,11,12], [13,14,15,16]]]
#tensor is a nested container, 3 dimensions
#tensor is a 3d array
#tensor is a 3d array of 2x2x4

c = set([1,2,3,4,5,6,7,8,9,10])
print(c)
print(type(c))

#set is a collection of unique elements

#dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
print(type(d))

#dictionary is a collection of key-value pairs
