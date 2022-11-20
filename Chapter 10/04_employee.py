class Employee:
    company = "Google"
    salary = 100

honey = Employee()
rajni = Employee()
# Changing instance variable 
honey.salary = 300
rajni.salary = 400

print(honey.company)
print(rajni.company)

Employee.company = "Youtube" # Changing class attribute
print(honey.company)
print(rajni.company)
print(honey.salary)
print(rajni.salary)