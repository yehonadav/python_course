# Loops Exercises  
  
  
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
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  