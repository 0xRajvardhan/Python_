# factorial is:
# n! = 1*2*3*4...*n
'''
n = int(input("Enter number\n"))
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

'''
# Creating a function for the same


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


print(factorial_iter(5))

# Creating a recursion function for the same


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)


print(factorial_recursive(5))
