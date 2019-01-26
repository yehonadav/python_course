# python_course

Net4U
=====
 
Exercises: 
---------

1.  Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year they were born in. 
 
2.  Ask the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message. 

solutions
----------
 
1. 
```
    import datetime 
    name = input("Enter your name: ") 
    age = int(input("Enter your age: ")) 
    birth = datetime.datetime.utcnow().year - age 
    print("{}; you were born in {}".format(name, birth))
```
 
2. 
```
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
```
