"""Password stars"""

def main():
    minimum_length = 5
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password), end="")
    print()


def get_password(minimum_length):
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password has to be a minimum of {minimum_length} characters.")
        password = input("Enter password: ")
    return password


main()
