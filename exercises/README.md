# Exercises
  
level 0: 
---------
  
just go through them    
  
level 1: 
---------

(1)  Create a program ```name_info.py``` that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year they were born in. 
  
(2)  Create a program ```odd_or_even_numbers.py``` that asks the user for a number. 
Depending on whether the number is even or odd, print out an appropriate message. 
  
  
(3)  Create a program ```list_less_than_5.py```  
use this list:  
```ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]```  
Write a program that creates a new list that has all the elements  
less than 5 from ```ages``` list and print out all the elements of the new list.  
  
  
(4)  Create a program ```divider.py```  
that asks the user for a number and then prints out  
a list of all the divisors of that number.  
(If you don’t know what a divisor is,  
it is a number that divides evenly into another number.  
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)  
   
   
(5)  Create a program ```common_list.py```  
that takes two lists:  
```  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]```  
```  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]```  
and returns a list that contains only the elements that  
are common between the lists (without duplicates).  
Make sure your program works on two lists of different sizes.  
  
  
(6)  Create a program ```palindrome.py```  
that asks the user for a string and print out  
whether this string is a palindrome or not.  
(A palindrome is a string that reads the same forwards and backwards.)  
  
  
(7)  Create a program ```bar_mitzva.py```  
use the exercises data:  
```from exercises.data import get_data```  
```data = get_data(10)```  
loop over 10 items and get the first item  
who's age is under 13 & print the item keys  
& values. if none of the items has an age  
less than 13 print a message saying all the  
people are old.  
  
  
(8)  Create a program ```fibonacci_sum.py```  
create a program to summarize the fibonacci sequence.   
  
  
(9)  Create a program ```hobbies_handler.py```  
create a hobbies function with ```name, age, hobby, *optional_hobbies & **other```  
that returns a sentence:
```my name is {name}, my age is {age}.\nI like to {hobby}{optional_hobbies}.{optional_keyword_hobbies}```   
* add ```int``` hint to age argument.  
* add type enforcement to age argument.  
* create a main program condition to call the function:  
  ```if __name__ == "__main__":```  
  and print the result in the main program.  
  
  
(10)  Create a program ```sort_data.py```  
* create a function ```sort_names_with_addresses``` that gets a data argument(exercise data)  
* the function creates a list of sorted names.  
* the function adds addresses to the name list,  
* the function finally returns a sorted list (by name) of tuples  
  with names and lists of addresses.  
output example:  
```[```  
```('Ana Romero', ['8973 Cline Mall\nWest Williamhaven, LA 13926']),```  
```('Anthony Poole', ['3412 Costa Fall Apt. 204\nEast Gerald, VT 13412'])```  
```]```  
  
  
(11)  open ```sort_data.py```  
* create another function called add_random_postal  
  that gets a ```names_with_addresses``` argument(the sorted output of previous function)  
* the function iterates over the list  
  and creates a new list with a third value  
  of every item: a string of 5 random digits.  
* the function return the result.  
  
  
(12)  open ```sort_data.py```  
* create another function called sum_postal_codes  
  that gets a data argument(the output of previous function)  
* the function iterates over the data  
  and sums up the random postal code of each item.  
* the function return the result.  
  
  
(13)  Create a program ```main_sort.py```  
* import ```from exercises.data import get_data```  
* import ```sort_names_with_addresses``` from ```exercises.level_1.sort_data```  
* import ```add_random_postal``` from ```exercises.level_1.sort_data```  
* import ```sum_postal_codes``` from ```exercises.level_1.sort_data```  
* create a main program condition:  
  ```if __name__ == "__main__":```  
* get 30 different data items  
* use sort_names_with_addresses  
* use add_random_postal  
* use sum_postal_codes  
* print the results  
  
  
(14)  Create a file ```number_generator.py```  
* import the random module  
* create a numbers function with a range argument  
* add a while range > 0 loop to the function.  
* yeild a random number(0-10,000) in the loop  
* subtract 1 from range in the loop  
* finish the loop and write a return to break the function  
* congrats! you created a generator. test it with  
```for n in numbers(200): print(n)```  
  
  
(15)  Create a file ```even_numbers.py```  
use the number generator from previous exercise(range=40)  
create a list that has only even numbers in it.  
* if list length > 10 raise an exeption stating that the list has exceeded its limit.  
* create a special MaxLengthException for the exercise.  
  
  
(16)  Create a file ```rock_paper_scissors.py```  
create a rock paper scissors game.  
* use the getpass module(doesn't run well with pycharm)  
https://stackoverflow.com/questions/40007802/getpass-getpass-function-in-python-not-working
  
  
(17)  Create a file ```guess_game.py```  
* Generate a random number between 0 and 10  
* Ask the user to guess the number,  
* then tell them whether they guessed too low,  
  too high, or exactly right.   
* Keep the game going until the user types “exit”
* Keep track of  answer + low/high/exact guesses  
  the user has taken in each round,  
  and when the game ends, print this out.  
* use functions & run the game from the main condition.  
  
(18)  Create a file ```zero_division.py```
* create a function ```create_numbers``` that returns a list of  
  random numbers with a random length between 0-9  
* create a function ```avg``` that takes the list of ```create_numbers``` and returns an average number  
* create a function ```print_average``` that takes the list of ```create_numbers``` and try to print the average  
* if ```print_average``` fail with ```ZeroDivisionError``` or ```TypeError``` it will print  
  the error and return it.  
* make a main program to call ```print_average``` until failure.  
  
(19)  Create a file ```type_error.py```
* use and import functions from ```zero_division.py```  
* create a function ```randomly_stringify_list_items```
* make a main program to:  
  create random list of numbers  
  randomly stringify some numbers  
  ```print_average``` until failure.  
  
(20)  Create a file ```quadratic.py```
* create a ```QuadError```  exception  
* create a function ```calculate_quadratic_equation```  
  ```ax² + bx + c = 0``` to find x1, x2 using the ```math``` module  
  ![quadratic](https://github.com/yehonadav/python_course/blob/master/exercises/images/quadratic.JPG?raw=true)  
  raise a ```QuadError``` if the equation is not quadratic(a=0) or has no real roots(b²-4ac<0)  
* make a main program to:  
  solve & print results of -> 5x² + 7x = 15  
  solve & print results of -> 6x² + 11x - 35 = 0  
  solve & print results of -> 2x² - 4x - 2 = 0  
  solve & print results of -> 2x² - 64 = 0  
  solve & print results of -> -12x² + 13x = 0  
  try to solve -> 6x² + 11x - 35 = 0
  in case of ```QuadError``` solve -> 11x + 50 = 0
  
(21)  Create a file ```calculator.py```  
* create a ```Calculator```  class  with ```a, b``` arguments  
* create ```display``` method to print the numbers and the last result  
* create ```add``` method to calculate ```a+b```  
* create ```sub``` method to calculate ```a-b```  
* make sure the result is shared between all calculators  
* test the calculators(level 2)  
  
(22)  Create a file ```inherit.py```  
* use ```time``` & ```datetime``` modules  
* create ```Time``` class with ```get_time``` to get a time signature  
* create ```Date``` class with ```get_date``` to get a date signature  
* inherit ```Time``` class from in ```Date``` class  
* create a main program condition:  
  ```if __name__ == "__main__":```  
  use both classes and their available methods  
  
(23)  Create a file ```athlete.py```  
* create ```Athlete``` class with ```name, power, speed, endurance, weight``` arguments  
* create ```Sprinter``` and inherit ```Athlete```  
  boots the ```Sprinter``` parameters as such:  
```  
power *= 2, speed += 1, endurance -= 3  
if endurance < 1: endurance = 1
```  
* create a ```run``` method like so in ```Sprinter```:  
```
    def run(self, distance):
        endurance = 1 + distance/self.endurance
        sleep((self.weight*distance)/(self.power*(self.speed**2)+endurance))
        return self.name
```
  
(25)  Create a file ```timer.py```  
* create ```Measurement``` class with ```date``` & ```run_time```  
  
(26)  in ```timer.py```  
* import ```Date```  from exercise 22  
* create ```Timer``` class & inherit ```Date```  
* create ```__init__``` method with ```f, *args, **kwargs``` arguments  
* save the arguments as such:
```
    self.operation = f
    self.args = args
    self.kwargs = kwargs
    self.last_measurement = Measurement()
```  
* create a ```start``` method  
  to measure time & date,  
  run an operation with its arguments  
  & return the operation result  
  
(27)  in ```timer.py```  
* create a main program condition:  
  ```if __name__ == "__main__":```  
* use these imports: 
```
    from random import randint
    from exercises.level_1.oop.athlete import Sprinter
    from exercises.data import get_data

```
* create ```winner```, ```distance```, ```athletes``` variables  
* loop over the athletes and create sprinters  
* use Timer to measure each sprinter running ```distance```   
* sort the winner  
* print a message with:  
  the date of the competition,  
  winner name, the distance,  
  the winner run time  

  
    
  
level 2:  
---------
  
(1)  Create a file ```fibonacci.py```  
* create a main program condition:  
  ```if __name__ == "__main__":```   
* create a fibonacci_sequence function
* print the result of the first 10 items of the sequence  
* create a fibonacci_generator function  
* create a fibonacci_iterator function  
* iterate over fibonacci_iterator and print  
  the result from 5  to 89.  
  
(2)  Create a file ```assert_program_is_done.py```  
* create a ```UserQuit``` exception  
* create a ```ask_user``` function with a question  
  argument. try to ask the question using ```input```  
  and expect an ```y,n,q```  answer.  
  raise a UserQuit exception if an ```EOFError```  
  is encountered or if the user pressed "Q/q/quit/QUIT"  
  if the user pressed "Y/YES/N/NO/y/yes/n/no"  
  return the uppercased first character the user pressed.  
  for anything else recurse the ```ask_user``` function  
* create a ```assert_program_is_done``` function  
  use the ```time``` module to measure how long it  
  took the user to answer. if a UserQuit error rises  
  print a message stating that the user quit before  
  assertion was completed, else: check if the answer is 'Y'  
  print the time it took the user to answer, if the answer  
  is 'N' print ```'better luck next time'```  
  finally print ```'assertion is done'```  
* call ```assert_program_is_done```  
  
(3)  Create a file ```first_recurring_char.py```    
* create a function to find the first recurring char in a string.  
* make it performance worthy!  
  
(4)  Create a file ```required_keyword_positionals.py```    
* create a function that accepts only keyword arguments  
* you can't use ```**kwargs``` or its variants  
* arguments can't have default values  
* the function must print all local variables
* make it in 1 line of code. - what's cool about this function?
  
(5)  Create a simple address book application,  
to store, search, modify & delete records containing:  
name, address, email & phone number (level 2+)  
* you must use a class called ```AddressBook```  
* use the pickle module as a database  
  
(6)  Create a progress bar using ```sys``` & ```time``` modules  
![progressbar1](https://github.com/yehonadav/python_course/blob/master/exercises/images/progressbar.JPG?raw=true)  
  
(7)  Create a file ```best_sum_and_ratio.py``` (level 2++)  
* import:  
```
import random  
from exercises.level_2.overloaded_function import expon, results
```  
* create & run a function to try and run expon with None  
  and run it again with a str/int(randomly) with a random value: 0-4.  
  in case of failure run expon with a list of 2 random values: 0-4, 2-3.  
* create a ```create_results``` function  
  it will run this loop:  
```
    while res_sum > stop:
        print("sum {} > {}".format(res_sum, stop))
        ...
        # we can wrap this into a function
        expon(random.randint(0, 1025))
        expon(random.randint(0, 1025) * 0.001)
        expon([random.randint(1, 101) * 68 / 47 * random.randint(1, 3) for _ in range(random.randint(0, 25))])

        stop = len(results)
        # we can wrap this into a function
        if stop > ...:
            before = start - n
            if before < 1:
                before = 1
            for i in range(before, stop):
                if results[i] > 1:
                    results[i] = 1/results[i]
                    
        # should be able to reach +5000 results
        n = int(str((n+1)*...*(n+1)).split('.')[0])+1
        res_sum = sum(results)
        ...
    print("sum {} < {}\n\n\n".format(res_sum, stop))
```  
  res_sum: expon results summary  
  stop: expon results length  
  results: expon results  
  n: a counter starting from 0  
  start: expon results length  
  ...: fill your own code    
* create a ```find_best_sum_and_ratio``` function  
  inside the function: create a SUM class with ```sum, len, ratio``` attributes  
  find the point in time where the summary of the results was the highest  
  find the point in time where the ratio summary:length of results was the highest  
  print them.

(8)  Create a file ```users.py```  
* create exceptions: ```LowCreditsError, LowStockError, MissingItemError```  
* create ```User``` class:  
```
class User:
    users = {}

    def __init__(self, name, password, credit):
        self.name = name
        self.password = password
        self.credit = credit
        self.items = {}
    
    ...
```
* create ```login, logout, buy, sell, create``` methods:  
login/logout need to compare passwords and return True/None
buy/sell will add/subtract items and change user credit, use exceptions accordingly  
create is a classmethod to create users and add them to the users by their names:
```
class User:
    users = {} # right here
```  
  
(9)  Create a test for ```users.py```  
  
(10)  Create a simple game using pyxel  
  
(11)  Build a fill-in-the-blanks quiz game.  
Your quiz will prompt a user with a sentence  
containing several blanks. The user should then be asked to fill in each blank appropriately to complete the sentence.  
  
(12)  create a tic tac toe game  
  
  
level 3:  
---------
  
(1)  create a black jack game  
  
(2)  Build a randomly generated Python space game.  
With traveling, trading, mining, resource management, battles and storyline events  
along with saving the users data to that of an output file.  
  
(3)  Create a snake game using the pygame module  
![Snake](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/sanke.JPG?raw=true)  
* Create a python package ```snake```  
![Snake package](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/snake_package.JPG?raw=true)  
* create a ```__main__.py``` file for the package  
  and import a Play class to run the game.  
* create a play.py file with a Play class.  
  the Play class should contain a ```run```,```restart``` & ```start```  
  methods to run the game, go back to the menu & start the menu.  
  an ```__init__``` method should also be defined with some variables:  
  self.menu: to include the menu object.  
  self.game: to include the running game object.  
  self.screenX & self.screenY: to set the screen size of the game.  
  after setting the variables the init method should call the start method.  
* import a Game & StartMenu classes from the snake package.
* create a game.py & menu.py file to import from.  
* in the StartMenu class create a start & exit buttons
  for calling sys.exit() or proceeding to choose a game size.
![menu](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/menu.JPG?raw=true)  
* have a choose_size method with ```Small Normal Big``` buttons  
  to set the snake & apple sizes and proceeding to choose a difficulty level.
![choose size](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_size.JPG?raw=true)  
* have a choose_difficulty method with ```Easy Normal Hard Expert``` buttons  
  to set the snake moving speed and proceeding to run the game.  
![choose difficulty](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_difficulty.JPG?raw=true)  
* use these methods to run the game from the menu:  
```    
    def easy(self):
        self.game.run(0.25, self.size)

    def normal(self):
        self.game.run(0.5, self.size)

    def hard(self):
        self.game.run(1, self.size)

    def expert(self):
        self.game.run(2, self.size)
```  
* create a mainloop method to run events in the menu.  
* create a resources package, add snake.py & apple.py  
  and create a Snake & Apple classes.  
* go to the ```game.py``` file, import the Snake & Apple classes  
* create a Game class
* use the ```__init__``` method to set the screen
* create an over method to show the score, go back to the menu or exit the program  
![game over](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/game_over.JPG?raw=true)  
* create a loop method that will:  
  fill the screen ```self.screen.fill((30, 40, 100))```  
  update the snake object ```self.snake.update()```  
  check snake for collisions  
  check for apples  
  update image positions of snake & apple  
  check for key events  
good luck!  
  
  


  
