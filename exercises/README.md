# Exercises

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
who's age is under 13 and print the item keys  
& values. if none of the items has and age  
less than 13 print a message saying all the  
people are old.  
  
  
(8)  Create a program ```fibonacci_sum.py```  
create a program to summarize the fibonacci sequence.   
  
  
(9)  Create a program ```hobbies_handler.py```  
create a hobbies function with name, age, hobby, *optional_hobbies & **other  
that returns a sentence:
```my name is {name}, my age is {age}.\nI like to {hobby}{optional_hobbies}.{optional_keyword_hobbies}```   
* add ```int``` hint to age argument.  
* add type enforcement to age argument.  
* create a main program condition to call the function:  
  ```if __name__ == "__main__":```  
  and print the result in the main program.  
  
  
(10)  Create a program ```sort_data.py```  
* create a function sort_names_with_addresses that gets a data argument(exercise data)  
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
  that gets a names_with_addresses argument(the sorted output of previous function)  
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
  
  
level 3:  
---------
  
(1)  Create a snake game using the pygame module  
![Snake](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/sanke.JPG)
* Create a python package ```snake```  
* create a __main__.py file for the package  
  and import a Play class to run the game.  
* create a play.py file with a Play class.  
  the Play class should contain a ```run```,```restart``` & ```start```  
  methods to run the game, go back to the menu & start the menu.  
  an __init__ method should also be defined with some variables:  
  self.menu: to include the menu object.  
  self.game: to include the running game object.  
  self.screenX & self.screenY: to set the screen size of the game.  
  after setting the variables the init method should call the start method.  
* import a Game & StartMenu classes from the snake package.
* create a game.py & menu.py file to import from.  
* in the StartMenu class create a start & exit buttons
  for calling sys.exit() or proceeding to choose a game size.
* have a choose_size method with ```Small Normal Big``` buttons  
  to set the snake & apples sizes and proceeding to choose a difficulty level.
* have a choose_difficulty method with ```Easy Normal Hard Expert``` buttons  
  to set the snake moving speed and proceeding to run the game.  
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
* go to the game.py file, import the Snake & Apple classes  
* create a Game class
* use the __init__ method to set the screen
* create an over method to show the score, go back to the menu or exit the program  
* create a loop method that will:  
  fill the screen ```self.screen.fill((30, 40, 100))```  
  update the snake object ```self.snake.update()```  
  check snake for collisions  
  check for apples  
  update image positions of snake & apple  
  check for key events  
good luck!  
  
  


  