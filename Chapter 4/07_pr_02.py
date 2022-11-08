m1 = int(input("Enter marks of first student: "))
m2 = int(input("Enter marks of second student: "))
m3 = int(input("Enter marks of third marks of student: "))
m4 = int(input("Enter marks of fourth student: "))
m5 = int(input("Enter marks of fifth student: "))
m6 = int(input("Enter marks of sixth student: "))

marksOfStudent = [m1, m2, m3, m4, m5, m6]
# because tuple is non mutable

marksOfStudent.sort()
print(marksOfStudent)
