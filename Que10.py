#Write a Python function that takes a list of numbers and returns the maximum value in the list. 

def find_maximum(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
max_value = find_maximum(numbers)
print(f"The maximum value in the list is: {max_value}")
