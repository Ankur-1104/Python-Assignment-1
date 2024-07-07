#Write a Python program that takes two numbers as input and performs division, handling the 
#case where the divisor is zero. 

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
if (b==0):
    print("Can't be divisible by zero")
else :
    c = a/b
print(f"The division of your number is : {c}")
