# finding factorial of n
num = int(input('Enter number:\t'))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of the number is {factorial}")