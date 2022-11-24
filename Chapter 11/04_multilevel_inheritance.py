class Person:
    country = "INDIA"
    
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am breathing so I am grateful for being alive")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

p = Person()
print(p.country)
e = Employee()
pr = Programmer()
p.takeBreath()
e.takeBreath()