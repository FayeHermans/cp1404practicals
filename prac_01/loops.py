for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 100, 10):
    print(i, end=" ")
print()

# b
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c
number_of_stars = int(input("How many stars: "))
for i in range(0, number_of_stars):
    print("*", end="")
print()

#d
row_number = 0
number_of_stars = int(input("How many rows of stars: "))
for i in range(0, number_of_stars):
    row_number = row_number + 1
    for n in range(0, row_number):
        print("*", end="")
    print()
