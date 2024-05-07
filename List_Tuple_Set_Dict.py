# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:07:33 2024

@author: Hafsa
"""
##List
print("####___________List_____________####:")
#initialization
l = [2,1,3,4,5,6,7,7,7,'ass']
print("Initialization = ",l)
#indexing
print("Indexing = ",l[2])
#addition
l.append("hafsa")
print("Addition = ",l)
#deletion
l.pop()
print("Deletion = ",l)
l.pop(9) # give the index
print("Deletion = ",l)

#sorting
l.sort()
print("Sorting = ",l)
#searching
print("Searching = ",l.index(7))  #return index
#reverse
l.reverse()
print("Reverse = ",l)
#count
print("Count = ",l.count(7))




##Tuple
print("####___________Tuple_____________####:")
#initialization
t = (2,1,3,4,5,6,7,7,7,'ass')
print("Initialization = ",t)
#indexing
print("Indexing = ",t[2])

#searching
print("Searching = ",t.index(7))  #return index
#count
print("Count = ",t.count(7))




## Set
print("####___________Set_____________####:")
#initialization
s = {"apple", "mango", "banana", "cherry",6,3,7,7,7,77,9}
print("Initialization = ",s)

#addition
s.add("hafsa")
print("Addition = ",s)
#deletion
s.pop()
print("Deletion = ",s)
s.pop()
print("Deletion = ",s)





##Dictionary
print("####___________Dictionary_____________####:")
#initialization
d = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.6
}
print("Initialization = ",d)
#indexing
print("Indexing = ",d['name'])
#addition
d.update({"address":"Khulna"})
print("Addition = ",d)
#deletion
d.pop("address")
print("Deletion = ",d)

#sorting
print("Sorting = ",sorted(d))
#searching
print("Searching = ",d['major'])  #return index

#count
#print("Count = ",d.count(7))


