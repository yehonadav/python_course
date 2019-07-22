# Exercises  
  
basic: 
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
  
loops: 
---------  
  
(1) create ```hobbies.py```  
* add these lines of code:  
```
from exercises.data import get_data
from statistics import median
import random

users = get_data(2000)  
```
* create a list of hobbies  
* create a second list of different hobbies  
* create a __main__ = __name__ condition  

(2) in ```hobbies.py```:  
* create and run a function that extract users and measure their average age  
* create and run a function that extract users and find the most common name  
* create and run a function that extract users and measure their median  
  
(3) in ```hobbies.py```:  
* create and run a function that adds a random hobby to users  
  
* create and run a function to count the hobbies and print their count  
  
* create and run a function that adds a second hobby from the same hobby pool,  
  if the hobbies are the same, randomly change one of the hobbies  
  to a new random hobby from a second hobby pool  
  
* create and run a function to count the hobbies from the second hobby pool  
  and print their count  
  
(4) create ```loopers.py```:  
* import these:  
```python
import time
from exercises.data import get_data
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby, hobbies, hobbies2
```  
  
* create a ```if "__main__" = __name__``` condition  
  
* create 2000 users in your main  
  
(5) in ```loopers.py```:  
* create and run a function named ```get_addresses```  
  the function receive ```(users, start=0, stop=50)``` parameters,  
  iterates through users and return a list of user addresses  
  starting with the starting point up to the stop point.  
  
(6) in ```loopers.py```:  
* create and run a function named ```count_address_numbers```  
  the function receive ```(user_addresses)``` parameter,  
  and holds a counter dictionary & most_counted_address_number parameters  
```python
def count_address_numbers(user_addresses):
    address_number = user_addresses[0].split(' ', 1)[0]
    counter = {address_number: 0}
    most_counted_address_number = address_number
```  

* use the function to iterate through users  
* in each iteration get the first word of the address  
* if the word is not a number continue(ignore that iteration)  
* if the word is in ```counter``` increment counter
* otherwise add the word to the counter with a value of 1
* each time you increment ```counter``` check if the word has beed counted more than the ```most_counted_address_number```  
* if a new word has been counted the most, update ```most_counted_address_number```  
* print the most counted word and how many times it has been counted.  
  
(7) in ```loopers.py```:  
* create and run a function named ```encounter_name_twice```  
  the function receive ```(users)``` parameter,  
  iterates with a while loop through users until it encounters a user name twice  
* use the function to print the name you encountered twice  
  
(8) in ```loopers.py```:  
* create and run a function named ```sum_index30```  
  the function receive ```(users)``` parameter, and  
  iterate users until their age sum is bigger than the current iteration index by 30 fold or more  
* use the function to print the users age summary and index  
    
(9) in ```loopers.py```:  
* create and run a function named ```name_and_address20```  
  the function receive ```(users)``` parameter, and  
  iterate users until it finds a name and address with a combined length bigger than 20 characters  
* use the function to print the combined name+address length, if found  
  
(10) in ```loopers.py```:  
* create and run a function named ```assert_names```  
  the function receive ```(users)``` parameter, and  
  iterate users and assert their name length is between 2-20 characters long  
* if you encounter an AssertionError, make sure your main can handle it  
  
(11) in ```loopers.py```:  
* create and run a function named ```assert_ages```  
  the function receive ```(users)``` parameter, and  
  iterate users and assert their age is between 0-120 characters long  
* if you encounter an AssertionError, make sure your main can handle it  
  
(12) in ```loopers.py```:  
* create and run a function named ```assert_user_hobby```  
  the function receive ```(users)``` parameter  
* use ```hobbies``` & ```hobbies2``` to create ```all_hobbies``` a list containing all hobbies   
* iterate users and assert their hobby is in ```all_hobbies```  
* also assert users second hobby is in ```all_hobbies```
* make sure to run  
```python
add_random_hobby(users)
add_second_hobby(users)
```  
  in your main, before calling ```assert_user_hobby(users)```  
* inject an invalid hobby to a user  
* if you encounter an AssertionError, make sure your main can handle it  
* if the invalid injection failed make sure to raise an exception, with an ```expectation failed: ..``` message  
  
(13) in ```loopers.py```:  
* create a function named ```get_user_uptime```  
  the function receive ```(user)``` parameter, and  
  uses the user's 'created' key to pull an epoc time value, 
  it then measures the current time and subtract the created time to get the user uptime value.  
  if the 'created' key does not exist the caller should handle a KeyError exception.  
  
(14) in ```loopers.py```:  
* create and run a function named ```print_users_avg_uptime```  
  the function receive ```(users)``` parameter, and  
  print the users average uptime  
  
(15) in ```loopers.py```:  
* create and run a function named ```find_equal_neighbor_age```  
  the function receive ```(users)``` parameter, and  
  iterate the users, if 2 neighboring users have the same age  
  a message with their name and age is printed before the function returns  
  
(16) in ```loopers.py```:  
* create and run a function named ```create_more_users```  
  the function receive ```(users)``` parameter, and  
  loops for ~2 seconds, while looping the function creates users
  in sets of 10 and adds them to the main users list  
  before checking the loop condition for the next iteration  
  after the creation process is done, a message telling  
  how many users were added is printed  
  
functions: 
---------
  
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
  
(14)  Create a file ```zero_division.py```
* create a function ```create_numbers``` that returns a list of  
  random numbers with a random length between 0-9  
* create a function ```avg``` that takes the list of ```create_numbers``` and returns an average number  
* create a function ```print_average``` that takes the list of ```create_numbers``` and try to print the average  
* if ```print_average``` fail with ```ZeroDivisionError``` or ```TypeError``` it will print  
  the error and return it.  
* make a main program to call ```print_average``` until failure.  
  
(15)  create a mygame1.py file  
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
  
  
error handling: 
--------- 
  
(1)  Create a file ```type_error.py```
* use and import functions from ```zero_division.py```  
* create a function ```randomly_stringify_list_items```
* make a main program to:  
  create random list of numbers  
  randomly stringify some numbers  
  ```print_average``` until failure.  
  
(2)  Create a file ```quadratic.py```
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
  
  
regEx: 
----   
  
(1) create ```simple_regex.py```:  
* import these:  
```python
import re
from regEx.data import sentences, data as regex_text
from exercises.data import create_user, get_data, get_data_as_text, transform_data_to_text
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby
```
* create a ```__name__ == "__main__"``` condition  
* join all sentences into 1 string
* create a user  
* create 20 users from get data and add a hobby to each user  
* create another 10 users and add a hobby and a second hobby to each user  
* transform all created users into text  
* create another 30 users as text  
* combine all the data into 1 string  
    
(2) in ```simple_regex.py```:  
* create a function called find_matches which receives a regex and string parameters  
* the function must return a list of matches for the regex  

(3) in ```simple_regex.py``` in combined_data text  
print the number of matches for b-x + F-W or whitespace 0 times or more + 2-6  

(4) in ```simple_regex.py``` in user text  
print the number of matches for exclusion any of these characters acegijlnprtvxz    

(5) in ```simple_regex.py``` in user text  
print the number of matches for any none word character or any of IDAN  
  
(6) in ```simple_regex.py``` in user text  
print the number of matches for a/b/c + any character  
  
(7) in ```simple_regex.py``` in user text  
print the number of matches for any 5 characters  
  
(8) in ```simple_regex.py``` in users20 text  
print the number of matches for all numbers  
  
(9) in ```simple_regex.py``` in users30 text  
Search the string to see if it starts with "name" and ends with "a number adn a white-space"  
print the result  
  
(10) in ```simple_regex.py``` in regex_text text  
print the number of matches of 'to'  
  
(11) in ```simple_regex.py``` in user text  
print 0 matches if no match was found for 'zombie'  
  
(12) in ```simple_regex.py``` in regex_text text  
Search for the first white-space character in the string  
print the result  
  
(13) in ```simple_regex.py``` in users20 text  
Make a search that returns no match  
print the result  
  
(14) in ```simple_regex.py``` in user text  
Split at each white-space character  
print the number of matches  
  
(15) in ```simple_regex.py``` in user text  
Split the string only at the first occurrence of a white-space  
print the number of matches  
  
(16) in ```simple_regex.py``` in user text  
replace every white-space character with tab  
  
(17) in ```simple_regex.py``` in user text  
replace the first 2 occurrences of a white-space to _  
  
(18) in ```simple_regex.py``` in regex_text text  
Do a search that will return a Match Object  
The Match object has properties and methods  
used to retrieve information about the search, and the result:  
  .span() returns a tuple containing the start-, and end positions of the match.  
  .string returns the string passed into the function  
  .group() returns the part of the string where there was a match  
print the match regex, string(text) size, span and value(match group)  
  
(19) in ```simple_regex.py``` in users10 text  
print the position (start- and end-position) of the first match occurrence.  
The regular expression looks for any words that starts with a "na"  
  
(20) in ```simple_regex.py``` in regex_text text  
print the value of the first match match.  
The regular expression looks for any words that starts with an "S"  
  
(21) in ```simple_regex.py``` in regex_text text  
print the value of the first match.  
The regular expression looks for any words that starts with an "S"  
whats wrong here? make an error handler  
  
(22) in ```simple_regex.py``` in combined_data text  
print any word that starts with ar  
  
(23) in ```simple_regex.py``` in combined_data text  
print all matches of any characters with 2 following occurrences  
  
(24) in ```simple_regex.py``` in sentences text  
print the starting 2 characters of the sentence  
  
(25) in ```simple_regex.py``` in sentences text  
print the final 10 characters of the sentence  
  
(26) in ```simple_regex.py``` in sentences text  
print the number of matches for the following 3 a-z A-Z characters after each white-space  
  
(27) in ```simple_regex.py``` in combined_data text  
print the number of matches for all valid ip octets(0-255)  
  
(28) in ```simple_regex.py``` in users30 text  
print the number of matches for any single character except \n  
  
(29) in ```simple_regex.py``` in users30 text  
print the number of matches for all `.` occurrences  
  
(30) in ```simple_regex.py``` in combined_data text  
print the number of matches for all website occurrences  
  
(31) in ```simple_regex.py``` in combined_data text  
print the number of matches for all email occurrences  
  
(32) in ```simple_regex.py``` in users30 text  
print set of the matches for all user names  
  
(33) in ```simple_regex.py``` in users20 text  
print set of the matches for all users first hobbies  
  
(34) in ```simple_regex.py``` in users10 text  
print set of the matches for all user hobbies  
  
(35) in ```simple_regex.py``` in combined_data text  
print set of all ip occurrences  
  
  
file handling: 
--------- 
  
(1)  Create a file ```file_exercises.py```  
* import os module  
* use a variable called filename  
* use os to remove the file  
* use os to check if the file exists  
* if the file does not exist create it using open  
* open file and write a sequence  
* open file and read it, print it's contents  
  
(2)  in ```file_exercises.py```  
* write lines to your file  
* read only up to the 10th character  
* read another line  
* read another line  
* read the other lines  
* print the results  
    
(3)  in ```file_exercises.py```  
* use ```with``` to open your file and add another sequence in a new line  
* create a directory  
* copy the file  
* move the file to the directory  
* copy the directory and its contents  
* list all file names in the directory  
* delete the files and directories  
  
(4)  Create a file ```phone_book_file_excercise.py```  
* create a phone book program to write numbers or view a range of numbers  
  
(5)  Create a file ```get_html_content.py```  
* use the requests module to get the url content  
* create a program that receives a url and creates an html file  
* if the url is invalid or the content fails to write, use error handling and a loop to retry  
  
  
  
OOP: 
---- 
  
(1)  Create a file ```calculator.py```  
* create a ```Calculator```  class  with ```a, b``` arguments  
* create ```display``` method to print the numbers and the last result  
* create ```add``` method to calculate ```a+b```  
* create ```sub``` method to calculate ```a-b```  
* make sure the result is shared between all calculators  
* test the calculators(level 2)  
  
(2)  Create a file ```inherit.py```  
* use ```time``` & ```datetime``` modules  
* create ```Time``` class with ```get_time``` to get a time signature  
* create ```Date``` class with ```get_date``` to get a date signature  
* inherit ```Time``` class from in ```Date``` class  
* create a main program condition:  
  ```if __name__ == "__main__":```  
  use both classes and their available methods  
  
(3)  Create a file ```athlete.py```  
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
  
(4)  Create a file ```timer.py```  
* create ```Measurement``` class with ```date``` & ```run_time```  
  
(5)  in ```timer.py```  
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
  
(6)  in ```timer.py```  
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
  
(7)  in ```timer.py``` class ```Timer```  
* add doc string explaining the Timer API
* add a hint typing for ```f``` argument hinting it is a function (callable)  
  
  
lambda map filter reduce: 
----   
  
(1) create ```map_reduce_filter.py``` create and run a function to:  
* create a ```calc``` function to calculate item length multiplied  
  by its partial divergent series, example: ```python
  calc('abc') -> 3 * (1+2+3) -> returns 18
  ```
* declare this variable: ```ai = ['6.', '40.0', '75.00', '126.00']```  
* use the map function to calc ```ai``` and save the result  
* print the sum of the result  
    
(2) in ```map_reduce_filter.py``` create and run a function to:  
* declare this variable: ```names = ['Tom', 'Gon', 'Don', 'Bon']```  
* use the map function & lambda to create upper names  
* use the map function & lambda to create lower names  
* print the names  
  
(3) in ```map_reduce_filter.py``` create and run a function to:  
* import: ```from exercises.data import get_data```  
* create 10 users using imported function  
* map user names (use lambda)  
* print the names    
  
(4) in ```map_reduce_filter.py``` create and run a function to:  
* using these code lines:  
```python
def combo(a, b):
    return a + b

yummy_fruits = ('apple', 'banana', 'cherry')
sour_fruits = ('orange', 'lemon', 'pineapple')
```  
* use the map function to create a fruit 'combo' (combine the fruits to 1 data structure)  
* count the fruits and print them  
  
(5) in ```map_reduce_filter.py``` create and run a function to:  
* filter all yummy fruits with 'a' (use lambda)  
* filter all sour fruits starting with 'o' or ending with 'le' (use lambda)  

(6) in ```map_reduce_filter.py```  
* use these lines:  
```python
from exercises.data import get_data
import random
users = get_data(random.randint(4, 6))
```  
create and run a function to:  
* map users age  
* filter all ages < 18  
* print filtered ages  
    
(7) in ```map_reduce_filter.py```  
* use these lines of code:  
```python
from exercises.data import get_data
from exercises.helpers import random_range
import random
users = get_data(1000)
for _ in random_range(3, 30):
    suspect1 = users[random.randint(0, 999)]
    suspect2 = users[random.randint(0, 999)]
    suspect1['email'] = suspect2['email']
    print(suspect1['email'])
```  
* map users to contain only their name, address, email, phone_number, age
* convert the map to a list  
* find users that are suspect to fraud (users with the same email)  
* print suspects with their name, address, email and phone number  
* filter all users with an age range of 0-17  
* filter all users with an age range of 18-59  
* filter all users with an age range of 60+  
* list all fraud suspects to 1 list  
* filter all fraud suspects with an age range of 0-17  
* filter all fraud suspects with an age range of 18-59  
* filter all fraud suspects with an age range of 60+  
* calculate and print which age group is more susceptible to fraud  
  
(8) in ```map_reduce_filter.py``` create and run a function to:  
* get 5 users  
* use list comprehension to get their birth year  
* use a reducer to get the birth summary  
* print the birth sum and the average sum of the collected years using reduce & lambda  
  
(9) in ```map_reduce_filter.py``` create and run a function to:  
* create 500,000 users with {name, birth, age} fields  
* create a birth_iterator using list comprehension  
* create a birth_iterator using map & lambda  
* use the time module to measure the durations of these operations  
* print out which operation performs faster  
* create a name_iterator from names starting with a-m using list comprehension  
* create a name_iterator from names starting with a-m using filter & lambda  
* use the time module to measure the durations of these operations  
* print out which operation performs faster  
  
(10) in ```map_reduce_filter.py```  
* using this calender:  
```python
calender_2019_07_11 = [
    [0, 7],  # sleep
    [7, 8],  # getting ready for work
    [8, 9],  # drive to work
    [9, 10],  # reading emails
    [10, 12],  # working on assignment
    [12, 13],  # launch break
    [13, 15],  # working on assignment
    [15, 16],  # in a meeting
    [16, 17],  # working on assignment
    [18, 19],  # fitness exercise
    [19, 20],  # buying groceries
    [20, 21],  # dinner break
    [21, 24]  # hobbies and family time
]
```  
* reduce the calender items by merging adjacent events  
* print a result showing a clear picture of where we can insert more event  
    
(11) in ```map_reduce_filter.py``` create and run a function to:  
* create 20 users  
* print the maximum age using reduce & lambda  
  
(12) in ```map_reduce_filter.py``` create and run a function to:  
* create 20 users  
* print their sum birth using reduce and operator  
  
(13) in ```map_reduce_filter.py``` create and run a function to:  
* create 20 users  
* print the multiplication of birth+age of all users using reduce  
  
(14) in ```map_reduce_filter.py``` create and run a function to:  
* create 20 users  
* print the concatenated name+phone_number of all users using reduce  
  
  
Flask: 
---- 
  
(1)  Create ```Hello World``` flask app 
  
(2)  Create a flask app with 4 routes  
    
(3)  Create a flask app with port 80(http protocol) and open your app to other devices  
  
(4)  Create a flask app with a styled page using html  
  
(5)  Create a flask app  
* serve an html template  
* the route will receive a name argument and pass it to the template  

(6)  Create a ```staticfiles``` flask app with route that receives a page name and renders a template by that name.  

(7)  Create a simple login flask app  
![flask_login](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_login.JPG?raw=true)  

(8)  Create a simple form flask app with validations  
![flask_form](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_form.JPG?raw=true)  
  
Jinja Templating:  
Right out of the box, Flask includes the powerful [Jinja](http://jinja.pocoo.org/docs/) templating language. It's modeled after Django templates (but it renders much faster) and, although, Flask does not force you to use any templating language, it assumes that you'll be using Jinja since it does come pre-installed.

For those who have not been exposed to a templating language before, such languages essentially contain variables as well as some programming logic, which when evaluated (or rendered into HTML) is replaced with **actual** values. The variables and/or logic are placed between tags or delimiters. For example, Jinja templates use `{% ... %}` for expressions or logic (like for loops), while `{{ ... }}` are used for outputting the results to the end user. The latter tag, when rendered, is replaced with a value or values, and are seen by the end user.

> Jinja Templates are just .html files. By convention they live in the "/templates" directory in a Flask project.
  
(9)  using jinja2 create a simple hello world template  
  
(10)  Create a file ```simple_message.py```, using jinja2 render a template with a message from user input  
  
(11)  using jinja2 create a simple for loop template  
   
(12)  Create a flask app using jinja2:  
* the following project structure:  
  ```sh
  with_flask
      ├── __init__.py
      ├── requirements.txt
      ├── run.py
      └── app
           ├── __init__.py
           └── templates
                 ├── layout.html
                 ├── macros.html
                 └── template.html
  ```
* use these requirements:  
```
Flask==1.0.2
Jinja2==2.10
MarkupSafe==1.0
Werkzeug==0.14.1
itsdangerous==0.24
wsgiref==0.1.2
```    
* create & activate a virtualenv  
* install the requirements  
* add the following code to ```with_flask/app/templates/template.html```:  
```html
  <!DOCTYPE html>
  <html>
    <head>
      <title>Flask With Jinja Example</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
      <style type="text/css">
        .container {
          max-width: 1000px;
          padding-top: 100px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <p>
        It's worth noting that Jinja only supports a few control structures - 
        if-statements & for-loops are the two primary structures. 
        The syntax is similar to Python, differing in that no colon is required 
        and that termination of the block is done using an endif or endfor 
        instead of by whitespace. You can also complete the logic within your controller 
        or views and then pass each value to the template using the template tags. 
        However, it is much easier to perform such logic within the templates themselves.
        </p>
        <p>string variable: {{string_variable}}</p>
        <p>list index 0 value: {{list_variable[0]}}</p>
        <p>Loop through the list:</p>
        <ul>
          {% for n in wrong_list %}
          <li>{{n}}</li>
          {% endfor %}
        </ul>
        <br>
        <h4>Inheritance</h4>
        <p>
        Templates usually take advantage of <a href="http://jinja.pocoo.org/docs/templates/#template-inheritance">inheritance<a/>, 
        which includes a single base template that defines the basic structure 
        of all subsequent child templates. 
        You use the tags `extends` and `block` to implement inheritance.

        The use case for this is simple: as your application grows, 
        and you continue adding new templates, you will need to keep common code 
        (like a HTML navigation bar, Javascript libraries, CSS stylesheets, and so forth) in sync, 
        which can be a lot of work. 
        Using inheritance, we can move those common pieces to a parent template 
        so that we can create or edit such code one and all child templates will inherent such code.
        </p>
      </div>
      <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
    </body>
  </html>
```  
* fix the broken html code  
* add the following code to ```with_flask/app/__init__.py```:  
```
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def template_index():
    """Here we are establishing the route /, 
    which renders the template template.html 
    via the function render_template(). 
    This function must have a template name. 
    Optionally, you can pass in arguments to the template, 
    like in this example - string_variable & list_variable.
    """
    return render_template('template.html', string_variable="Combat-Bat", list_variable=[n for n in range(0, 7)])
```  
* add the following code to ```with_flask/run.py```:  
```
from with_flask.app import app


if __name__ == '__main__':
    app.run(debug=True)

```    
* run the app    
  
(13)  in your ```with_flask``` app:  
* add the following code to ```with_flask/app/templates/layout.html```:  
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask With Jinja Example</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      .container {
        max-width: 1000px;
        padding-top: 100px;
      }
      h2 {color: red;}
    </style>
  </head>
  <body>
    <div class="container">
      <h2>Before-Block: This is the layout. block templates are inside:</h2>
      <br>
      {% block content %}{% endblock %}
      <br>
      <h2>After-Block: This is the layout. block templates are inside:</h2>
      <!--
        The block defines a block (or area) that child templates can fill in.
        Further, this just informs the templating engine that a child template may override
        the block of the template.

        Think of these as placeholders to be filled in by code from the child template(s).
       -->
    </div>
    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
```
*  Update the *template.html*:  
  ```html
  {% extends "layout.html" %}
  {% block content %}
    <!--
        The `extends` informs the templating engine that this template 
        "extends" another template, layout.html. This establishes the link between the templates.
     -->
    <h3>In-Block-Start: This is a block template nesting inside the layout</h3>
    <br>
    <p> ..prev content.. </p>
    <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% endblock %}
  ```  
* run the app:  
![jinja_nesting_template](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_nesting_template.JPG?raw=true)  
  
(14)  in your ```with_flask``` app:  
* Add a navigation bar: the following code to your layout, just after the opening <body> tag:
```html
  <nav class="navbar navbar-inverse" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="http://jinja.pocoo.org/">Jinja</a>
      </div>

      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li class="active"><a href="#">Link</a></li>
          <li><a href="#">Link</a></li>
        </ul>
        <form class="navbar-form navbar-left" role="search">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Search">
          </div>
          <button type="submit" class="btn btn-default">Go</button>
        </form>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="#">Link</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Profile <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="#">Manage</a></li>
              <li><a href="#">Account</a></li>
              <li><a href="#">Help</a></li>
              <li class="divider"></li>
              <li><a href="#">Sign Out</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
```  
Now every single child template that extends from the layout, will have the same navigation bar.  
Write once, use anywhere.  
* Add a footer block to the layout template at the end of ```<div class="container">```:  
```html
<div class="footer">
  {% block footer %}
    Watch! This will be added to my base and child templates using the super powerful super block!
    <br>
    <br>
  {% endblock %}
</div>
```  
* Add the [super block](http://jinja.pocoo.org/docs/templates/#super-blocks) - `{{ super() }}` block to *template.html*:  
```html
  ...
  <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% block footer %} <!-- add this line -->
  {{super()}} <!-- add this line -->
  {% endblock %} <!-- add this line -->
{% endblock %}
```  
* run the app:  
![jinja_flask_with_navbar_and_footers](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_flask_with_navbar_and_footers.JPG?raw=true)  
  
(15)  in ```with_flask``` app:  
The super block is used for common code  
that both the parent and child templates share,  
such as the <title> where both templates share part of the title,  
then you would just need to pass in the other part. Or for a heading. For example:  
  
  **Parent**

  ```html
  {% block heading %}
    <h1>{% block page %}{% endblock %} - Flask Super Example</h1>
  {% endblock %}
  ```

  **Child**

  ```html
  {% block page %}Home{% endblock %}
  {% block heading %}
    {{ super() }}
  {% endblock %}
  ```  
add these and run the app:  
* make sure to send a title parameter in the ```template_index``` route under ```app/__init__.py```  
* *layout.html*:
```html
<!DOCTYPE html>
<html>
  <head>
    {% block head %}
      <title>{% block title %}{% endblock %} - Flask With Jinja Example</title>
    {% endblock %}
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style type="text/css">
      .container {
        max-width: 1000px;
        padding-top: 100px;
      }
      h2 {color: red;}
    </style>
  </head>
  <body>
    <nav class="navbar navbar-inverse" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="http://jinja.pocoo.org/">Jinja</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Link</a></li>
            <li><a href="#">Link</a></li>
          </ul>
          <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default">Go</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Profile <b class="caret"></b></a>
              <ul class="dropdown-menu">
                <li><a href="#">Manage</a></li>
                <li><a href="#">Account</a></li>
                <li><a href="#">Help</a></li>
                <li class="divider"></li>
                <li><a href="#">Sign Out</a></li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container">
      {% block heading %}
        <h1>
          {% block page %}{% endblock %} - Flask With Jinja Example
        </h1>
      {% endblock %}
      
      <h2>Before-Block: This is the layout. block templates are inside:</h2>
      <br>
      {% block content %}{% endblock %}
      <br>
      <h2>After-Block: This is the layout. block templates are inside:</h2>
      <!--
        The block defines a block (or area) that child templates can fill in.
        Further, this just informs the templating engine that a child template may override
        the block of the template.

        Think of these as placeholders to be filled in by code from the child template(s).
       -->

      <br>
      <div class="footer" style="color: green">
        {% block footer %}
          This will be added to the layout and child templates using `super` block!
          <br>
          <br>
          <br>
        {% endblock %}
      </div>
    </div>

    <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
  </body>
</html>
```  
* *template.html*:  
```html
{% extends "layout.html" %}

{% block title %}
  {{title}}
{% endblock %}

{% block head %}
  {{ super() }}
{% endblock %}

{% block page %}
  {{title}}
{% endblock %}

{% block heading %}
  {{ super() }}
{% endblock %}

{% block content %}
  <h3>In-Block-Start: This is a block template nesting inside the layout</h3>
  <br>
  <!--
    the `extends` informs the templating engine that this template
    "extends" another template, layout.html. This establishes the link between the templates.
  -->
  <p>
    It's worth noting that Jinja only supports a few control structures -
    if-statements & for-loops are the two primary structures.
    The syntax is similar to Python, differing in that no colon is required
    and that termination of the block is done using an endif or endfor
    instead of by whitespace. You can also complete the logic within your controller
    or views and then pass each value to the template using the template tags.
    However, it is much easier to perform such logic within the templates themselves.
  </p>
  <p>string variable: {{string_variable}}</p>
  <p>list index 0 value: {{list_variable[0]}}</p>
  <p>Loop through the list:</p>
  <ul>
    {% for n in list_variable %}
    <li>{{n}}</li>
    {% endfor %}
  </ul>
  <br>
  <h4>Inheritance</h4>
  <p>
    Templates usually take advantage of <a href="http://jinja.pocoo.org/docs/templates/#template-inheritance">inheritance</a>,
    which includes a single base template that defines the basic structure
    of all subsequent child templates.
    You use the tags `extends` and `block` to implement inheritance.

    The use case for this is simple: as your application grows,
    and you continue adding new templates, you will need to keep common code
    (like a HTML navigation bar, Javascript libraries, CSS stylesheets, and so forth) in sync,
    which can be a lot of work.
    Using inheritance, we can move those common pieces to a parent template
    so that we can create or edit such code one and all child templates will inherent such code.
  </p>

  <h3>In-Block-End: This is a block template nesting inside the layout</h3>
  {% block footer %}
  {{super()}}
  {% endblock %}
{% endblock %}
```  
  
(16) in ```with_flask``` app:  
* add a *home* route:  
![jinja_flask_home](https://github.com/yehonadav/python_course/blob/master/exercises/images/jinja_flask_home.png?raw=true)  
  
Time Modules: 
---- 

(1) create ```timeme.py```  
* import datetime, calendar & time  
* get a datetime date object from last year  
* print the date  
  
(2) in ```timeme.py```  
* get a datetime date object from today  
* print the date  
* print the day  
* print the year  
* print the month  
* print the weekday  
* print the isoweekday  
  
(3) in ```timeme.py```  
* create a time delta of 7 days  
* print the date of next week  
* print the date of last week  
* print the month of the date of 5 weeks ago  
  
(4) in ```timeme.py```  
* get a datetime date object of your birthday  
* get the delta between your birthday and today  
* print the delta  
* print the delta in days  
* print the delta in seconds    
* print the delta in microseconds  
  
(5) in ```timeme.py```  
* create a datetime time object  
* print the time  
* print the time seconds  
* print the time hour    
* print the time minute  
* print the time microsecond  
  
(6) in ```timeme.py```  
* create a datetime object  
* print the date  
* print the time  
* print the year    
* print the second  
  
(7) in ```timeme.py```  
* create a timedelta object of 52 weeks and 1 day 
* print date of today+timedelta  
  
(8) in ```timeme.py```  
* create a datetime object of today  
* create a datetime object of now  
* create a datetime object of utcnow  
* print them, they should be ~the same because they are not 'aware'  
  
(9) in ```timeme.py``` make sure ```pytz``` is installed (pip install pytz -U)  
* import pytz  
* create an aware datetime object using tzinfo=pytz.UTC  
* create a datetime object of now using tz=pytz.UTC  
* print them, they should be ~a little differrent because they are 'aware'  

(10) in ```timeme.py```  
* use astimezone and pytz.timezone on an aware object to create an aware datetime object with Israel time zone  
* use pytz.timezone to create an aware object from an naive object, with Israel time zone  
* print an aware object using strftime  
  
(11) in ```timeme.py```  
* using this format: 'July 26, 2016' and strptime
  create a datetime object  
  
(12) in ```timeme.py```  
* using timestamp convert a datetime object into an epoc number  
  
(13) in ```timeme.py```  
* using fromtimestamp & utcfromtimestamp convert an epoc number into a datetime object  
  
(14) in ```timeme.py```  
* create an epoc timestamp using the time module  
* delay the program using time module  
  
(15) in ```timeme.py```, using the calendar module  
* print the week headers with only 1 letter  
* print the week headers with only 2 letters  
* print the week headers with only 3 letters  
* print the first day of the week as 0  
* print a calendar of the 4th month of 1962  
* print the 11th month of 2050 as a 2D list  
* print a calendar of 2019  
* print the week day of today as a number 0-6  
* print if today's year is a leap year  
* print the count of how many leap years are from today - year 3222  
  
  
Pandas: 
----   
  
(1)  
* import numpy as np  
* import pandas as pd  
* create a __name__ == "__main__" condition  
* in define this variable:  
```python
data={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
```    
* create a dataframe and print it  
* view dataframe head  
* view dataframe tail  
* view dataframe head of 3  
* view dataframe tail of 3  
* view dataframe shape  
* view dataframe info  
* view dataframe description  
* view data types  

(2)  
* create a dataframe  
* select a column  
* select 2 columns  
* select the first row  
* select the first element of first column  
  
(3)  
* create a dataframe  
* rename its columns  
* check for empty values  
* check for not-empty values  
* drop all rows that contain null values  
* drop all columns that contain null values  
* drop all rows that have less than 3 non null values
* replace all null values with 99  
* rename all columns to lowercase  
* rename 1 column  
* set Y as  
* increase all indexes by 1  
  
(4)  
* create a dataframe  
* get the rows where the minimal value of X is bigger than 84  
* get the rows where the minimal value of Y is bigger than 86 and smaller than 94  
* sort values of Y in ascending order  
* sort values of Y in descending order  
* sort values of Y in ascending order then Z in descending order  
* group values from one column  
* group values from 2 columns  
* get the mean values in Z, grouped by the values in X  
* create a pivot table that groups by X and calculates the mean of Y and Z  
* get the average across all columns for every unique X group  
* apply the function np.mean() across each column  
* apply the function np.max() across each row 
  
(5)  
* create 2 dataframes: df1, df2
* Add the rows in df1 to the end of df2 (columns should be identical)  
* Add the columns in df1 to the end of df2 (rows should be identical)  
* make SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. The 'how' can be 'left', 'right', 'outer' or 'inner'  

  
(6)  
* create a dataframe  
* Summarize statistics for numerical columns  
* get the mean of all columns  
* get the correlation between columns in a DataFrame  
* get the number of non-null values in each DataFrame column  
* get the highest value in each column  
* get the lowest value in each column  
* get the median of each column  
* get the standard deviation of each column  
  
(7)    
* create a dataframe from CSV file  
* create a dataframe from a delimited text file (like TSV)  
* create a dataframe from an Excel file  
* create a dataframe from a SQL table/database  
* create a dataframe from a JSON formatted string, URL or file.  
* parse an html URL, string or file and extracts tables to a list of dataframes  
* take the contents of your clipboard and pass them to read_table()  
* create a dataframe from a dict, keys for columns names, values for data as lists  
  
(8)  
* Write to a CSV file  
* Write to an Excel file  
* Write to a SQL table  
* Write to a file in JSON format    
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  