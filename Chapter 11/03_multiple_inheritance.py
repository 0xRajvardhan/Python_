# Multiple inheritance refers to when a derived class has multiple base classes
class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Rohit"


p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)
