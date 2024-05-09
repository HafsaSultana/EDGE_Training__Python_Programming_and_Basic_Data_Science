# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:32:53 2024

@author: atanu-office-pc
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

my_list = ["apple", "banana", "cherry"]
my_tuple = tuple(my_list)
print(my_tuple)

#################################################

my_tuple = ("apple", "banana", "cherry")
first_fruit = my_tuple[0]  # first_fruit will be "apple"
print("Single Element",first_fruit)
for fruit in my_tuple:
  print(fruit)
  
#dimensions = (200, 50)
#dimensions[0] = 250

###############################################
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
    
######################################################
# Define the lists
fruit_names = ['banana', 'mango']
fruit_quantities = [10, 25]

# Create a new list by interleaving the fruit names and quantities
result = []
for i in range(len(fruit_names)):
    result.append(fruit_names[i])
    result.append(fruit_quantities[i])

print(result)

######################################################
print("\n\n\nDictionary\n\n")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
my_dict = dict(name="Bob", age=25)
print(my_dict)

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name = my_dict["name"]  # name will be "Alice"

my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"  # Adding a new key-value pair
my_dict["age"] = 31  # Modifying an existing value
print(my_dict)

if my_dict["age"]<31:
    print("Not too old")
elif my_dict["age"] == 31:
    print("About to be to buira")
else:
    print("Definitely Buro manush")

#####################################################

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'php',
}
print(favorite_languages['jen'])
del favorite_languages['jen']
print(favorite_languages)

var1 = favorite_languages.get("sarah")
print(var1)
var1 = favorite_languages.get("atanu", "not found")
print(var1)

################################################

for k, v in favorite_languages.items():
    stri = f"Key {k} and value is {v}"
    print(stri)

for k in favorite_languages.keys():
    print(k)
    
for k in sorted(favorite_languages.keys()):
    print(k)
    
#############################################
    
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

for k, v in pizza.items():
    print(f"Key is {k} and value is {v}")

#################################################

a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

print ("a:", a, "b:", b, "list:", list)

if ( a in list ):
   print ("a is present in the given list")
else:
   print ("a is not present in the given list")

if ( b not in list ):
   print ("b is not present in the given list")
else:
   print ("b is present in the given list")

c=b/a
print ("c:", c, "list:", list)
if ( c in list ):
   print ("c is available in the given list")
else:
    print ("c is not available in the given list")
    
    















