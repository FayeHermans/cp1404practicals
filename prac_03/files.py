"""
CP1404: Practical 03
"""

# 1
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file) # I googled why this warning is here and can't figure out how to get rid of it, help please
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3
with open("numbers.txt", "r") as in_file:
    number01 = int(in_file.readline())
    number02 = int(in_file.readline())
print(number01 + number02)
