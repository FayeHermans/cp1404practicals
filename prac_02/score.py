"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get user score and determine status"""
    score = float(input("Enter score: "))
    status = determine_status(score)
    print(f"Your score is {status}.")
    random_score = random.randint(0, 100)
    random_status = determine_status(random_score)
    print(f"The status for score {random_score} is {random_status}")


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


main()
