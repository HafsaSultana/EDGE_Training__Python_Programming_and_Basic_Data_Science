list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

#Access

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#Update
list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1].title())

bicycles.append("Duranta")
print(bicycles)

bicycles.insert(3, "Racer")
print(bicycles)

#############################################################

# Define a sample list
my_list = [10, 20, 30, 40, 50, 30]

# Value to search and delete
value_to_delete = 30

# Search for the value in the list
if value_to_delete in my_list:
    # Delete the value from the list
    my_list.remove(value_to_delete)
    print(f"Value {value_to_delete} found and deleted from the list.")
    print("Updated list:", my_list)
else:
    print(f"Value {value_to_delete} not found in the list.")

###################################################################

# Define a sample list
my_list = [10, 20, 30, 40, 30, 50, 30]

# Value to delete
value_to_delete = 30

# Delete all occurrences of the value from the list
while value_to_delete in my_list:
    my_list.remove(value_to_delete)

if len(my_list) == 0:
    print(f"All occurrences of {value_to_delete} have been deleted from the list.")
else:
    print(f"All occurrences of {value_to_delete} have been deleted from the list.")
    print("Updated list:", my_list)


###################################################################


fruits = ["apple", "banana", "cherry"]
sublist = fruits[1:3]  # ["banana", "cherry"] (extracts elements at index 1 and 2, excluding index 3)

print(sublist)

removed_fruit = fruits.pop(2)  # removed_fruit is "cherry" and fruits becomes ["apple", "orange", "mango"]
print(removed_fruit)

###################################################################

my_list = [66, 33, 22, 44, 88, 77, 99, 11]
my_list2 = sorted(my_list)
print(my_list2)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)
print(len(my_list))

########################################################################

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]
vegetables = ["potato", "tomato"]
fruits.extend(vegetables)
print(fruits)  # Output: ["apple", "orange", "banana", "cherry", "potato", "tomato"]


numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]

# Sorting by length of strings
strings = ["aa", "bbbbb", "ccc"]
strings.sort(key=len)
print(strings)  # Output: ["aa", "ccc", "bbbbb"]

occurrences = fruits.count("apple")
print(occurrences)  # Output: 1

new_fruits = fruits.copy()
new_fruits.append("mango")

print(fruits)  # Output: ["apple", "banana", "cherry"] (original list is not modified)
print(new_fruits)  # Output: ["apple", "banana", "cherry", "mango"]
is_mango_in_fruits = "mango" in fruits
print(is_mango_in_fruits)  # Output: False
numbers = [5, 1, 8, 2]
smallest = min(numbers)
print(smallest)  # Output: 1
numbers = [5, 1, 8, 2]
largest = max(numbers)
print(largest)  # Output: 8

########################################################

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


##############################################################

for value in range(1, 5):
	print(value)


print("Append to list")
list = []
for value in range(1, 5): 
	list.append(value)
print(list)


#########################################################
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'atanu', 'jacob']
print("Here are the first three players on my team:")

for player in players[2:5]:
      print(player.title())







