"""Password stars"""

MINIMUM_LENGTH = 5


def main():
    """Print a user password using stars"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(MINIMUM_LENGTH):
    """Get user input longer than minimum length"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password has to be a minimum of {MINIMUM_LENGTH} characters.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print stars the same length as the password"""
    print("*" * len(password), end="")


main()
