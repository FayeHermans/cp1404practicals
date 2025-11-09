"""
Prac 07 - Project Management
Est time: 55 min
Start time: 2:17PM
Finish time:
Actual time:
"""
from project import Project
import datetime


def main():
    projects = []
    process_file('projects.txt', 'r', projects)


def process_file(filename, action, list):
    in_file = open(filename, action)
    in_file.readline()
    for line in in_file:
        print(repr(line))  # check line formatting
        parts = line.strip().split('\t')
        print(parts)  # check formatting
        date_string = parts[1]  # e.g., "30/9/2022"
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
        list.append(project)
    in_file.close()


main()
