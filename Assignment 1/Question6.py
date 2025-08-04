# 6. Lists
# Write a program to find the largest and smallest elements in a list.
# Reverse a list without using built-in functions.
# Remove duplicates from a list and display the result.

numbers = [5, 2, 8, 1, 9]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print("Reversed list:", reversed_list)
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("Unique list:", unique_list)