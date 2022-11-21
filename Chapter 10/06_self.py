class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is for this employee working in {self.company} is {self.salary}")

honey = Employee()
honey.salary = 100000
# honey.getSalary()
Employee.getSalary(honey)
