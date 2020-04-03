"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When we are not input a number e.g "a"
2. When will a ZeroDivisionError occur?
    When we input the denominator as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        print("You need to input a number more than 0")
        denominator=int(input())
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")