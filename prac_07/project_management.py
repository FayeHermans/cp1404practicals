"""
Prac 07 - Project Management
Est time: 55 min
Start time: 2:17PM
Break: 3:12PM - 3:44PM
Finish time:
Actual time:
"""
from operator import itemgetter

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
    projects = load_file(filename, projects)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {filename}")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "L":
            # load project from user input filename
            user_filename = input("Enter filename to load files: ")
            projects = load_file(user_filename, projects)
        elif choice == "S":
            # save project
            save_filename = input("Enter filename to save to: ")
            save_file(save_filename, projects)
        elif choice == "D":
            # display projects
            incomplete = []
            complete = []
            for project in projects:
                if project.completion_percentage == 100:
                    complete.append(project)
                else:
                    incomplete.append(project)
            incomplete.sort()
            complete.sort()
            print("Incomplete projects:")
            for project in incomplete:
                print(f"\t {project}")
            print("Completed projects: ")
            for project in complete:
                print(f"\t {project}")
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date_from = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            to_do_projects = [p for p in projects if p.start_date >= date_from]
            to_do_projects.sort(key=lambda p: p.start_date)
            for project in to_do_projects:
                print(project)

        elif choice == "A":
            print("Let's add a new project")
            projects = add_project(projects)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])
            new_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_priority != "":
                projects[project_choice].priority = int(new_priority)
            if new_percentage != "":
                projects[project_choice].completion_percentage = int(new_percentage)
        else:
            print("Invalid choice.")
        choice = input(MENU).upper()
    save_choice = input(f"Would you like to save to {filename}")
    if save_choice == "yes":
        save_file(filename, projects)
    print("Thank you for using custom-built project management software.")


def load_file(filename, projects):
    in_file = open(filename, 'r')
    in_file.readline()
    for line in in_file:
        # print(repr(line))  # check line formatting
        parts = line.strip().split('\t')
        # print(parts)  # check formatting
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    in_file.close()
    return projects


def save_file(filename, projects):
    out_file = open(filename, 'w')
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}")
    out_file.close()


def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimation = input("Cost estimate: $")
    completion_percentage = input("completion_percentage: ")
    project = Project(name, start_date, priority, cost_estimation, completion_percentage)
    projects.append(project)
    return projects


main()
