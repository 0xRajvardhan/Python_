class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print(f"Lets add {self.num} and {num2.num}")
        return self.num + num2.num

    def __mul__(self, num2):
        print(f"Lets multiply {self.num} and {num2.num}")
        return self.num * num2.num


n1 = Number(4)
n2 = Number(6)

sum = n1 + n2
print(sum)

mul = n1 * n2
print(mul)
