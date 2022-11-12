num = int(input("Enter a number:\n"))

for i in range(1, 11):
    # print(num, "x", i, '=', i*num)

    # using f string
    print(f"{num}X{i}={num*i}")
