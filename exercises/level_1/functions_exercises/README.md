# Functions Exercises  
  
  
(1) given a storage room of 4x4x3  
* create a function to insert/pop items with their size  
* and to calculate how much room is available  

(2) create a function to receive a radius and print its circumference, round the result to x.xx  
    
(3)  Create a program ```bar_mitzva.py```  
use the exercises data:  
```from exercises.data import get_data```  
```data = get_data(10)```  
loop over 10 items and get the first item  
who's age is under 13 & print the item keys  
& values. if none of the items has an age  
less than 13 print a message saying all the  
people are old.  
  
  
(4)  Create a program ```fibonacci_sum.py```  
create a program to summarize the fibonacci sequence.   
  
  
(5)  Create a program ```hobbies_handler.py```  
create a hobbies function with ```name, age, hobby, *optional_hobbies & **other```  
that returns a sentence:
```my name is {name}, my age is {age}.\nI like to {hobby}{optional_hobbies}.{optional_keyword_hobbies}```   
* add ```int``` hint to age argument.  
* add type enforcement to age argument.  
* create a main program condition to call the function:  
  ```if __name__ == "__main__":```  
  and print the result in the main program.  
  
  
(6)  Create a program ```sort_data.py```  
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
  
  
(7)  open ```sort_data.py```  
* create another function called add_random_postal  
  that gets a ```names_with_addresses``` argument(the sorted output of previous function)  
* the function iterates over the list  
  and creates a new list with a third value  
  of every item: a string of 5 random digits.  
* the function return the result.  
  
  
(8)  open ```sort_data.py```  
* create another function called sum_postal_codes  
  that gets a data argument(the output of previous function)  
* the function iterates over the data  
  and sums up the random postal code of each item.  
* the function return the result.  
  
  
(9)  Create a program ```main_sort.py```  
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
  
  
(10)  Create a file ```number_generator.py```  
* import the random module  
* create a numbers function with a range argument  
* add a while range > 0 loop to the function.  
* yeild a random number(0-10,000) in the loop  
* subtract 1 from range in the loop  
* finish the loop and write a return to break the function  
* congrats! you created a generator. test it with  
```for n in numbers(200): print(n)```  
  
  
(11)  Create a file ```even_numbers.py```  
use the number generator from previous exercise(range=40)  
create a list that has only even numbers in it.  
* if list length > 10 raise an exeption stating that the list has exceeded its limit.  
* create a special MaxLengthException for the exercise.  
  
  
(12)  Create a file ```rock_paper_scissors.py```  
create a rock paper scissors game.  
* use the getpass module(doesn't run well with pycharm)  
https://stackoverflow.com/questions/40007802/getpass-getpass-function-in-python-not-working
  
  
(13)  Create a file ```guess_game.py```  
* Generate a random number between 0 and 10  
* Ask the user to guess the number,  
* then tell them whether they guessed too low,  
  too high, or exactly right.   
* Keep the game going until the user types “exit”
* Keep track of  answer + low/high/exact guesses  
  the user has taken in each round,  
  and when the game ends, print this out.  
* use functions & run the game from the main condition.  
  
  
(14)  create a mygame1.py file  
* print this message: 'welcome to my game'  
* create a while loop  
* use the input function to print a menu like so:  
* (1) new game  
* (2) try again  
* (3) quit  
* if the user input is not 1,2 or 3 print an error message  
* if the user pressed 3 break the loop  
* if the user press 1 activate a play function  
* if the user press 2 activate a replay function  
* create a play function  
*   create a number between 1-10  
*   save the number in a dictionary outside the function  
*   loop 3 times  
*       ask the user to guess the number  
*       if the answer is correct, print a message and return  
*       if the loop ended print a lose message and return  
* create a replay function that takes the random number from the dictionary  
* and use it to replay  
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  