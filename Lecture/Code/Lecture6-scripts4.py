def greet(name):
    """Greets the user by name.

    Args:
        name: The name of the person to greet (str).

    Returns:
        A string containing the greeting message.
    """
    message = f"Hello, {name}!"
    return message

name = greet("Atanu")
print(name)


##################### Pass by Reference #######################
def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg=arg+1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)

###############################################################

def testfunction(arg):
   
   global var
   var +=1

var=10
print ("Variable before passing:", var)
testfunction(var)
print ("value after function call", var)



####################################################

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)

###########################################################

def list_mod(my_list):

    current_item = my_list.pop()
    print(current_item.title())

one_list = ['john', 'marry', 'rock']
print("Before",one_list)
list_mod(one_list)
print("After",one_list)

###########################################################

def list_mod(my_list):

    current_item = my_list.pop()
    print(current_item.title())

one_list = ['john', 'marry', 'rock']
print("Before",one_list)
list_mod(one_list[:])
print("After",one_list)


####################################################

def func(
    param1, param2="okay",
    param3="Default", param4=""):

    print("This one works too")

func("Atanu")







