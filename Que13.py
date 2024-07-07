#Write a Python program that prints a multiplication table up to (numberx10).
  
num =int(input("Enter the number which multiplication table you want :"))
for i in range (1,11):
    print(num,"X",i,"=",num*i)
