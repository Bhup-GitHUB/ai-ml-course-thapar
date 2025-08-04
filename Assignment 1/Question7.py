# 7. Strings
# Count the number of vowels in a string.
# Reverse a string without using slicing.
# Find the frequency of each character in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str
string = input("Enter a string to reverse: ")
print("Reversed string:", reverse_string(string))
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
string = input("Enter a string: ")
print("Character frequency:", char_frequency(string))