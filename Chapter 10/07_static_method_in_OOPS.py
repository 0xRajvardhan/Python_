class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(
            f"Salary is for this employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod  # with use of this you can run it without self
    def greet():
        print("Good morning, Sir")


honey = Employee()
honey.salary = 100000

# Employee.greet(honey) this runs with self
honey.greet()  # now this will run without self

# Employee.getSalary(honey)
honey.getSalary("Thanks!")
