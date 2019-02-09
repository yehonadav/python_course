import random
from exercises.level_1.oop.calculator import Calculator


def test_calculator():
    # create test data
    calculators = []
    for i in range(20):
        calculators.append(
            Calculator(
                random.randint(-1000, 1000),
                random.randint(-1000, 1000)
            )
        )
    answer = None

    for calculator in calculators:
        # assert answer sharing
        assert answer == calculator.answer

        calculator.add()
        answer = calculator.answer

        # assert addition
        assert answer == calculator.a + calculator.b

    for calculator in calculators:
        # assert answer sharing
        assert answer == calculator.answer

        calculator.sub()
        answer = calculator.answer

        # assert addition
        assert answer == calculator.a - calculator.b
