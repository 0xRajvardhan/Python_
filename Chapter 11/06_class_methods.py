class Employee:
    company = "Camel"
    salary = 100
    location = "Dubai"
    '''
    def changeSalary(self, sal):
        self.__class__.salary = sal
    this was one way to change the class attribute 
    '''
    # Another way 
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)