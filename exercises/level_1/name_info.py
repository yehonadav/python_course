import datetime


if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    birth = datetime.datetime.utcnow().year - age
    print("{}; you were born in {}".format(name, birth))
