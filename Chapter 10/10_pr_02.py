class Calculator():
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The value of {self.number} sqaure is {self.number ** 2}")

    def squarRoot(self):
        print(f"The square root of {self.number} is {self.number ** (0.5)}")

    def cube(self):
        print(f"The value of {self.number} sqaure is {self.number ** 3}")

a = Calculator(3)
a.square()
a.squarRoot()
a.cube()