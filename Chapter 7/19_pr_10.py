table = int(input("Enter the table: "))

limit = int(input("Enter the ending : "))

for i in range(limit,0,-1):
    print(i,"*",table,"=",i*table)