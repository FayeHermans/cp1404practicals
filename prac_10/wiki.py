"""CP1404 Prac 10"""

import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    """Wikipedia search program"""
    user_input = input("Enter page title: ")
    while user_input != "":
        try:
            page = wikipedia.page(user_input)
            print(page.title)
            print(page.summary)
            print(page.url)
            print("\n")
        except PageError:
            print(f"Page id {user_input} does not match any pages. Try another id!\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(e.options)
            print("\n")

        user_input = input("Enter page title: ")
    print("Thanks you.")

main()