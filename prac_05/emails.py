"""
CP1404 Practical 05
emails
Estimate: 15 min
Actual: 13 min
"""


def main():
    """Create dictionary with user emails and names."""
    email_to_name = {}
    user_email = input("Enter your email: ")
    while user_email != "":
        name = get_name_from_email(user_email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Enter your email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get the name from user email address."""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
