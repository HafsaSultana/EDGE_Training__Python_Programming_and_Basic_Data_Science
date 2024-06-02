marks = 80 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)

##################################################

day = "Tuesday"

if day == "Saturday" or day == "Sunday":
  print("Enjoy your weekend!")
else:
  print("Go to work!")

###################################################
print("Or we can do this")

day = "Tuesday"
is_weekend = day == "Saturday" or day == "Sunday"

if not is_weekend:
  print("Go to work!")
else:
  print("Enjoy your weekend!")


###################################################



#Multiple else if 

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B") 
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

################################################
# import random

# secret_number = random.randint(1, 10)


# guess = int(input("Guess a number between 1 and 10: "))

# if guess == secret_number:
#   print("You guessed it right!")
# elif guess < secret_number:
#   print("Too low, try again!")
# else:
#   print("Too high, try again!")

###################################################

num1 = 10
num2 = 20
if num1 > num2:
    print("num1 is greater")
else:
    if num1 == num2:
        print("num1 and num2 are equal")
    else:
        print("num2 is greater")


#######################################################
def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))















