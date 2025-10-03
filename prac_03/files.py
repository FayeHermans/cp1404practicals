"""
CP1404: Practical 03
"""

# 1
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file) # I googled why this warning is here and can't figure out how to get rid of it, help please
out_file.close()

# 2
