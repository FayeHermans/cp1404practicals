"""
Prac 07 - myguitars
Read guitars from file and store them in a list.
"""
from guitar import Guitar


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

    myguitars.sort()

    for myguitar in myguitars:
        print(myguitar)





main()