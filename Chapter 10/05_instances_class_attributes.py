class Employee:
    company = "Google"
    salary = 100  # class attribute


honey = Employee()
rajni = Employee()

'''
Creating instance attributes - salary for both objects
honey.salary = 300
rajni.salary = 400

'''
honey.salary = 45

print(honey.salary)
print(rajni.salary)
