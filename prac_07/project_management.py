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
            to_do_projects = []
            for project in sorted(projects, key=itemgetter(1)):
                project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y")
                if project_date >= date_from:
                    to_do_projects.append(project)
                    print(project.start_date)
            #TODO fix typeError ????????

            print(item for project in to_do_projects)

        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice.")
        choice = input(MENU).upper()
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
        print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.cpmpletion_percentage}")





main()
