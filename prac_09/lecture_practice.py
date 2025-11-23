"""CP1404 Week 09"""
from datetime import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        date_string = datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string})"

    def get_age(self):
        return int((datetime.now() - self.date_of_birth).days / 365)


if __name__ == '__main__':
    p1 = Person("Jane", datetime(1999, 2, 14))
    print(p1)
    print(p1.get_age())
