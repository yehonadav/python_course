class Calculator:
    answer = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("First number 'a': " + str(self.a))
        print("Second number 'b': " + str(self.b))
        print("Result: " + str(self.answer))

    def add(self):
        Calculator.answer = self.a + self.b

    def sub(self):
        Calculator.answer = self.a - self.b


# create a Calculator2 class that inherits from Calculator
# change the last result to a list of results
# add multiplication method
# create 3 calculators and make some calculations
# view the different results
class Calculator2(Calculator):
    results = []

    def display(self):
        print("First number 'a': " + str(self.a))
        print("Second number 'b': " + str(self.b))
        print("Results: " + str(self.results))

    def add(self):
        Calculator2.results.append(self.a + self.b)

    def sub(self):
        Calculator2.results.append(self.a - self.b)

    def mul(self):
        Calculator2.results.append(self.a * self.b)

c1 = Calculator2(9,9)
c2 = Calculator2(12, 56)
c3 = Calculator2(67, 122)
c1.add()
c2.sub()
c3.mul()
c3.display()