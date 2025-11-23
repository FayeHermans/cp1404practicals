"""CP1404 Prac 09"""

class Band:

    def __init__(self, name: str):
        self.band_name = name
        self.members = []

    def __str__(self):
        member_str = ','.join(str(member) for member in self.members)
        return f"{self.band_name} ({member_str})"


    def add(self, musician):
        return self.members.append(musician)

    def play(self):
        for member in self.members:
            print(member.play())