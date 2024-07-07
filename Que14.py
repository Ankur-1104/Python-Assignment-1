#Write a Python program to print a right-angled triangle of '*' with a given number of rows.

num_rows = int(input("Enter the number of rows: "))
for i in range(1, num_rows + 1):
    print('*' * i)
