# 4. Loops
# Write a program to print numbers from 1 to 100.
# Create a multiplication table generator.
# Implement a program to find the sum of all even numbers up to a given limit.

def print_numbers():
    for i in range(1, 101):
        print(i, end=" ")
    print()

def multiplication_table():
    num = int(input("number"))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

def sum_even_numbers():
    limit = int(input("Enter the limit: "))
    total = 0
    for i in range(2, limit + 1, 2):
        total += i
    print(f"Sum of all even numbers up to {limit} is {total}")

if __name__ == "__main__":
    print("Printing numbers from 1 to 100:")
    print_numbers()
    print("\nMultiplication Table Generator:")
    multiplication_table()
    print("\nSum of all even numbers up to a limit:")
    sum_even_numbers() 