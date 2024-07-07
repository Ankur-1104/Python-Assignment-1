#Write a Python program that imports a custom module you created with a function that returns 
#the factorial of a number.

#File1(fact.py)

def fact(n):
    x = 1
    for i in range (1, n+1):
        x = x * i 
    return x
        

