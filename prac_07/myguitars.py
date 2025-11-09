"""
Prac 07 - myguitars
Read guitars from file and store them in a list.
"""
from guitar import Guitar
from prac_03.capitalist_conrad import out_file


def main():
    """Read file and save in list."""
    myguitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        # print(repr(line)) # check line formatting
        parts = line.strip().split(',')
        # print(parts) # check parts formatting
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        myguitars.append(guitar)
    in_file.close()
    add_guitar(myguitars)

    myguitars.sort()
    export_list('guitars.csv', myguitars)

    for myguitar in myguitars:
        print(myguitar)

def add_guitar(myguitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_add = Guitar(name, year, cost)
        myguitars.append(guitar_add)
        print(f"{guitar_add} added")
        name = input("Name: ")
    return myguitars

def export_list(filename,myguitars):
    out_file = open(filename, 'w')
    for guitar in myguitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()

main()