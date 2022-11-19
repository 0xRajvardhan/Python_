def sum_of_natural_num(n):
    if n == 0:
        return 0
    return n + sum_of_natural_num(n-1)

n = int(input("Enter n: "))
print(sum_of_natural_num(n))