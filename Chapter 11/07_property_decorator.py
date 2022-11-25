class Employee:
    company = "Bharat Gas"
    salary = 5000
    salaryBonus = 600
    # totalSalary = 5500
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()

print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)


e.totalSalary = 5800
print(e.totalSalary)
print(e.salary)
print(e.salaryBonus)