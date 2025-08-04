
# 5. Functions
# Create a function to calculate the factorial of a number.
# Write a function to check if a string is a palindrome.
# Develop a function to find the greatest common divisor (GCD) of two numbers.



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(num))


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")


def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("GCD:", gcd(num1, num2))