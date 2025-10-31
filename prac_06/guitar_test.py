"""
Prac 06: Guitar
Expected time: 15min
Start time: 7:08pm
Finish time:
"""
from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 10)

print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
print(f"{another_guitar.name} get_age() - Expected 12. Got {another_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
