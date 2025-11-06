"""
Week 7 Practice
"""

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

Faye = person('Faye', 28)
Brody = person('Brody', 27)
print(Faye == Brody)
