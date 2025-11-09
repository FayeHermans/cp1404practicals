"""
Prac 07 - Project Management
Est time: 55 min
Start time: 2:17PM
Finish time:
Actual time:
"""
from project import Project
import datetime

MENU = ("- (L)oad projects\n"
"- (S)ave projects\n"
"- (D)isplay projects\n"
"- (F)ilter projects by date\n"
"- (A)dd new project\n"
"- (U)pdate project\n"
"- (Q)uit\n"
">>> ")


def main():
    projects = []
    filename = 'projects.txt'
    projects = process_file(filename, 'r', projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            # load project
            pass
        elif choice == "S":
            # save project
            pass
        elif choice == "D":
            # display projects
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice.")
        choice = input(MENU).upper()




def process_file(filename, action, list):
    in_file = open(filename, action)
    in_file.readline()
    for line in in_file:
        # print(repr(line))  # check line formatting
        parts = line.strip().split('\t')
        # print(parts)  # check formatting
        date_string = parts[1]  # e.g., "30/9/2022"
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
        list.append(project)
    in_file.close()
    return list


main()
