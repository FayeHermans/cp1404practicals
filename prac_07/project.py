import datetime

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = float(completion_percentage)

    def __str__(self):
       return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"


    def __lt__(self, other):
        return self.priority < other.priority