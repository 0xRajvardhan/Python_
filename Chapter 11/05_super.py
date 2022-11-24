class Person:
    country = "INDIA"
    def __init__(self):
        print("Initialising the person...\n")
    def takeBreath(self):
        print("I am breathing...\n")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initialising the employee...\n")
    def getSalary(self):
        print(f"Salary is {self.salary}\n")

    def takeBreath(self):
        super(). takeBreath()
        print("I am breathing so I am grateful for being alive\n")

class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__()
        print("Initialising the programmer...\n")
    def getSalary(self):
        print(f"No salary to programmers\n")
    def takeBreath(self):
        super(). takeBreath()
        print("I am a programmer so I am breating++")

p = Person()
# p.takeBreath()

e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()
