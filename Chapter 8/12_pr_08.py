def table(m):
    if m == False:
        for i in range(10):
            print(1,"x",i+1,"=",1*(i+1))
    else:
        for i in range(10):
            print(m,"x",i+1,"=",m*(i+1))

number = int(input())
print(table(number))


# need to understand this 