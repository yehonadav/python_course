def main():
    number=input("enter your string:")
    return True if number==number[::-1] else False


if __name__ == "__main__":
    print(main())
