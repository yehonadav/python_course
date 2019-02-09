class Calculator:
    answer = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("First number: " + str(self.a))
        print("Second number: " + str(self.b))
        print("Result: " + str(self.answer))

    def add(self):
        Calculator.answer = self.a + self.b

    def sub(self):
        Calculator.answer = self.a - self.b
