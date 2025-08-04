# 10. Exception Handling
# Write a program that handles division by zero.
# Create a program to handle invalid inputs while calculating square roots.
# Develop a custom exception for age verification in a voting system

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
import math
try:
    number = float(input("Enter a number for square root: "))
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    result = math.sqrt(number)
    print("Square root:", result)
except ValueError as e:
    print("Error:", e)
class AgeVerificationError(Exception):
    pass
def verify_age(age):
    if age < 18:
        raise AgeVerificationError("Too young to vote.")
    else:
        print("Eligible to vote.")
try:
    age = int(input("Enter your age: "))
    verify_age(age)
except AgeVerificationError as e:
    print("Error:", e)
except ValueError:
    print("Invalid Input")

