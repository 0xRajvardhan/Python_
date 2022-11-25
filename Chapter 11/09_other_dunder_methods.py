class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print(f"Lets add {self.num} and {num2.num}")
        return self.num + num2.num

    def __mul__(self, num2):
        print(f"Lets multiply {self.num} and {num2.num}")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number: {self.num}"

    def __len__(self):
        return 1

n = Number(9)
print(n)
print(len(n))

