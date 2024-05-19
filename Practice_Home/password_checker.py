# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:41:04 2024

@author: Hafsa
"""


password = input("Enter your password: ")
min_len = 7

low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


if len(password)>=min_len :
    print("Your guess is correct.")
    
    
    
 def is_valid_password(password):
  """Checks if a password meets the following criteria:
  - Minimum length of 8 characters
  - Contains at least one uppercase letter
  - Contains at least one lowercase letter
  - (Optional) Contains at least one number or special character

  Args:
      password: The password string to be validated.

  Returns:
      True if the password meets all criteria, False otherwise.
  """
  global min_length, has_uppercase, has_lowercase
  min_length = 8
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  # You can add a condition to check for numbers/special characters here
  # has_number_or_special = any(char.isdigit() or char in "!@#$%^&*" for char in password)

  # Check conditions using if-else statements
  if len(password) >= min_length and has_uppercase and has_lowercase:
    # Add a check for numbers/special characters if needed using 'and'
    # if len(password) >= min_length and has_uppercase and has_lowercase and has_number_or_special:
    return True
  else:
    return False

# Get password input from user
password = input("Enter your password: ")

# Check validity and print message
if is_valid_password(password):
  print("Valid password!")
else:
  print("Invalid password. Please ensure it meets the following criteria:")
  if len(password) < min_length:
    print(f"- Minimum length of {min_length} characters")
  if not has_uppercase:
    print("- Contains at least one uppercase letter (A-Z)")
  if not has_lowercase:
    print("- Contains at least one lowercase letter (a-z)")
  # You can add a message for missing numbers/special characters here

