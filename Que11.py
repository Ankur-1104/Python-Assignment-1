#Write a Python function that takes a name and an optional age parameter and prints a greeting. 
#If the age is not provided, it should default to 25.

name = input("Please enter your name: ")
age_input = input("Please enter your age (press Enter to skip): ")
age = int(age_input) if age_input else 25
print(f"Hello, {name}! You are {age} years old.")
