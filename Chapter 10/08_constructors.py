class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employees is created !")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"Salary of this employee is {self.salary}")
        print(f"The subunit is {self.subunit}")


    def getSalary(self, signature):
        print(
            f"Salary is for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning, Sir")
    
    @staticmethod
    def time():
        print("The time is 9AM in the morning")


honey = Employee("Honey", 100000, "Youtube")
honey.getDetails()
