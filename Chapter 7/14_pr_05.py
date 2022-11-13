n = int(input("Enter number: "))

# print("The sum of n natural numbers is:", n*(n+1)/2)
if n < 0:
    print("Please enter a positive number:")
else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print("The sum of n natural numbers is:", sum)
