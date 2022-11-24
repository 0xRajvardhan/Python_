class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

# Single inheritance refers to a derived class having only one base class 
class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLang(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print(f"{self.language} is a language")

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(p.company)