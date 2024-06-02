import array as arr

a = arr.array('i', [1, 2, 3]) # array of integers
b = arr.array('d', [2.5, 3.2, 3.3]) # array of floats

print(a)
print(b)
print(a[0])

import array as art 

n = art.array('i', [11, 6, 33, 55, 23, 99, 65]) 

print(n.typecode)
print(n.itemsize)

n.reverse()
print(n)

########################################################################
