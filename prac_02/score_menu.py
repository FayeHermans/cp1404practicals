"""Menu style score status program"""

MENU = """Menu:
(G)et new score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            status = determine_status(score)
            print(f"Your score is {status}.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    """Get a valid score between 0 and 100"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. (0 - 100)")
        score = int(input("Enter score: "))
    return score


def determine_status(score):
    """Determine the status from user score"""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * score, end="")
    print()


main()
