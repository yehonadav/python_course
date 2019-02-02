import math


class QuadError(Exception):
    pass


def calculate_quadratic_equation(a, b, c):
    if a == 0:
        raise QuadError("Not Quadratic")
    if b*b-4*a*c < 0:
        raise QuadError("No Real Roots")
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x1, x2


if __name__ == "__main__":
    # 5x² + 7x = 15
    results = calculate_quadratic_equation(5, 7, -15)
    print(results)

    # 6x² + 11x - 35 = 0
    results = calculate_quadratic_equation(6, 11, -35)
    print(results)

    # 2x² - 4x - 2 = 0
    results = calculate_quadratic_equation(2, -4, -2)
    print(results)

    # 2x² - 64 = 0
    results = calculate_quadratic_equation(2, 0, -64)
    print(results)

    # -12x² + 13x = 0
    results = calculate_quadratic_equation(-12, 13, 0)
    print(results)

    try:
        # 6x² + 11x - 35 = 0
        results = calculate_quadratic_equation(6, 11, 35)
        print(results)
    except QuadError as e:
        print(e, 'try another equation')
        # 11x + 50 = 0
        results = calculate_quadratic_equation(0, 11, 50)
        print(results)
