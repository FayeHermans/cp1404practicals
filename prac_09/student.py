from prac_09.lecture_practice import Person
from datetime import datetime


class Student(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, id_number: int, course: str):
        Person.__init__(self, name, date_of_birth)
        self.name = name
        self.date_of_birth = date_of_birth
        self.id_number = id_number
        self.course = course

    def __repr__(self):
        return str(vars(self))


class Employee(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, salary: float):
        super().__init__(name, date_of_birth)
        self.salary = salary

    def __str__(self):
        return f"{super().__repr__()} ${self.salary}"


if __name__ == '__main__':
    s1 = Student("Faye", datetime(1997, 10, 5), 57442, "ENG")
    print(s1)
    print(s1.get_age())
    e1 = Employee("Brody", datetime(1998, 4, 21), 80000)
    print(e1)
