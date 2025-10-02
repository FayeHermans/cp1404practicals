"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If user enters anything other than an integer.
2. When will a ZeroDivisionError occur?
If user enters 0 as denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Could add error checking so the user needs to enter a new value when 0 is detected.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")