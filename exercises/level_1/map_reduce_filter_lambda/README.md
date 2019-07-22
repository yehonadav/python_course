# lambda map filter reduce Exercises  
  
  
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
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  