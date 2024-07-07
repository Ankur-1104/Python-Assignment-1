#Write a Python program to swap the values of two variables without using a third variable. 

a =int(input("Enter your first number :"))
b =int(input("Enter your second number :"))
print(f"Before swapping the number first number ={a}, second number = {b}")
a = a+b
b = a-b
a = a-b
print(f"After swapping the number first number = {a}, second number = {b}")
