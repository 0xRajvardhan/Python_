def max(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if(num2 > num3):
            return num2
        else:
            return num3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Maximum number among three entered number is:", max(num1, num2, num3))