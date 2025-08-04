# 3. Conditional Statements
# Write a program to check if a number is positive, negative, or zero.
# Create a program to determine if a given year is a leap year.
# Develop a simple grade calculator based on user input for marks.

def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def calculate_grade():
    marks = float(input("Enter marks (0-100): "))
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__ == "__main__":
    print("Testing number checker:")
    check_number()
    print("\nTesting leap year checker:")
    check_leap_year()
    print("\nTesting grade calculator:")
    calculate_grade()
