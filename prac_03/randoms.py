import random

print(random.randint(5, 20))  # 13
print(random.randrange(3, 10, 2))  # 7
print(random.uniform(2.5, 5.5))  # 4.522914367250642

# Line 1: The smallest number we could've seen is 5.
# Line 2: The smallest number here is 3, and the largest is 9. This line can not produce a 4 because of the step: 2.
# Line 3: The smallest number is 2.5 and the largest 5.499999999.

print(random.randint(1,100))
