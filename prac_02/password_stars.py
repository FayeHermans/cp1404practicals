"""Password stars"""

minimum_length = 5
password = input("Enter password: ")
while len(password) < minimum_length:
    print(f"Password has to be a minimum of {minimum_length} characters.")
    password = input("Enter password: ")
print("*" * len(password), end="")
print()

