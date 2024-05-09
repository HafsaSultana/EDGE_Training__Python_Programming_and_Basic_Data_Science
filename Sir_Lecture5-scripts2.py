#####################################
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)

########################################

message = 'Hello, world!'  # Single quotes
name = "Alice"  # Double quotes
multiline_text = """This is a string
that spans multiple lines."""  # Triple quotes

print(multiline_text)

first_letter = message[0]  # 'H'
last_letter = message[-1]  # '!'
print(first_letter, last_letter)

message = "PythonClass"
substring = message[1:6]  # "world" (extracts characters from index 6 to 10)
print(substring)
substring = message[1:8:2]  # "world" (extracts characters from index 6 to 10)
print(substring)

########################################################

message = "Hello World"
uppercase_message = message.upper()
replaced_message = message.replace("world", "Python")
print(uppercase_message, replaced_message)
replaced_message = message.replace("World", "Python")
print(replaced_message)

name = "Bob"
age = 30
formatted_text = f"Hello, {name}! You are {age} years old."
print(formatted_text)  # Output: Hello, Bob! You are 30 years old.

####################################################################

name = "atanu shome" 
print(name.title())
print(name.upper())
print(name.lower())

message = "   Hello, World!    "

# Remove all leading/trailing whitespaces
stripped_message = message.strip()
print(stripped_message)  # Output: Hello, World!

# Remove leading whitespaces
left_stripped_message = message.lstrip()
print(left_stripped_message)  # Output:Hello, World!    

# Remove trailing whitespaces
right_stripped_message = message.rstrip()
print(right_stripped_message)  #   Hello, World!

#########################################
message = "Hi, this is a test string."

# Replace all occurrences of "is" with "was"
replaced_message = message.replace("is", "was")
print(replaced_message)  # Output: Hi, this was a test string.

# Replace only the first occurrence
replaced_message = message.replace("is", "was", 1)
print(replaced_message)  # Output: Hi, this was a test string.


##########################################
message = "Hello, brave new world!"

# Find the index of the first occurrence of "world"
world_index = message.find("world")
print(world_index)  # Output: 7

# Find the index of the last occurrence of "world" (if it appears multiple times)
last_world_index = message.rfind("world")
print(last_world_index)  # Output: 7

########################################################

message = "Hello, how are you today?"

# Split the string into words using spaces as separator
words = message.split(" ")
print(words)  # Output: ['Hello,', 'how', 'are', 'you', 'today?']

message2 = "I am Atanu $ I'm taking your class"
words = message2.split("$")
print(words)  # Output: ['Hello,', 'how', 'are', 'you', 'today?']

# Join the words back into a string with underscores
joined_message = "_".join(words)
print(joined_message)  # Output: Hello,_how,_are,_you,_today?

##########################################################################


def join_split_words(words_list, delimiter):

	connected = delimiter.join(words_list)
	print(connected)
	disconnected = connected.split(delimiter)
	return disconnected

words_list = ["Hello", "World", "Python"]
delimiter = ","
result = join_split_words(words_list, delimiter)
print(result)

formatted_text_output = f"okay lets try formating {result[0]}, can you see {result[1]}"
print(formatted_text_output)
##########################################################################





