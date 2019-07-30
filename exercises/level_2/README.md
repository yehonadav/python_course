# Exercises  
   
strings:
--------

(1)  decrypt this binary code:  
```10111010100 10111101000 10111010110 10111010111 10111010001 10111010101 100000 10111100011 10111010101 10111100001 10111100000 10111011001 10111010000 10111011100 100000 10111010011 10111100010 100000 10111011010 10111101010 10111010101 10111010000 100000 10111010001 10111010100 10111010101 10111010000 100000 10111011001 10111100000 10111010000 100000 10111010100 10111011001 10111010101 10111010110```  
  
     
functions:  
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
  
(5)  Create a progress bar using ```sys``` & ```time``` modules  
![progressbar1](https://github.com/yehonadav/python_course/blob/master/exercises/images/progressbar.JPG?raw=true)  
  
(6)  Create a file ```best_sum_and_ratio.py``` (level 2++)  
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
  
(15) in ```exercises.level_1.simple_regex.py``` in combined_data text  
print set of all ip occurrences without using regex  
  
      
OOP:  
---------  
  
(1)  Create a simple address book application,  
to store, search, modify & delete records containing:  
name, address, email & phone number (level 2+)  
* you must use a class called ```AddressBook```  
* use the pickle module as a database  
  
(2)  Create a file ```users.py```  
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
  
(3) Create a test for ```users.py```  
  
  
Games:  
---------  
    
(1) Create a simple game using pyxel  
  
(2) Build a fill-in-the-blanks quiz game.  
Your quiz will prompt a user with a sentence  
containing several blanks. The user should then be asked to fill in each blank appropriately to complete the sentence.  
  
(3) create a tic tac toe game  
  
  
Flask:  
---------    
  
(1)  Create a simple pie, bar & line charts flask app with using Chart.min.js  
![flask_pie_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_pie_chart.JPG?raw=true)  
![flask_line_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_line_chart.JPG?raw=true)  
![flask_bar_chart](https://github.com/yehonadav/python_course/blob/master/exercises/images/flask_bar_chart.JPG?raw=true)  
  
(2)  Create a simple login flask app with sqlite database & 3 users using sqlalchemy  
  
  
Automation:  
---------    
  
(1)  git clone https://github.com/yehonadav/doom_light.git (dont forget to setup python venv)  
*  delete the scripts directory and its contents  
*  recreate the scripts directory  
*  the repository contains .wad & .txt files, some of these file contain game characters  
   the characters format is as follows:('actor' can be fully or partially lower/upper cased and '{' can be after a new line)  
```
actor 'name' 'id' {
    code...
}
```  
  before adding characters we need to run a script to make sure the game characters will not duplicate ids or names,  
  create such a script to list all names and ids in a database and handle possible duplications:  
  * list all actor files  
  * get all ids + actor names  
  * change actor names + ids if duplicates  
  * save all actor names + ids in a DB (text/json file would be sufficient)  
  
(2)  git clone https://github.com/yehonadav/doom_light.git  
*  add the scripts from previous doom_light exercises  
*  create a script to check for animdefs conflicts:  
```
animdefs are animation definitions for the game, each file should have unique animdefs
animdefs names appear right after 'cameratexture', 'Cameratexture', 'CAMERATEXTURE', 'Texture', 'texture', 'TEXRURE', 'Flat', 'flat', 'FLAT', 'Switch', 'switch', 'SWITCH'
or 2 words after 'warp', 'WARP', 'Warp'

our script needs to check conflicts between directories 'JonaDoom' & 'things_to_import'
print the name conflicts and overall conflicts
```  
  
(3)  git clone https://github.com/yehonadav/doom_light.git  
*  add the scripts from previous exercises  
*  create a script to check for new actors conflicts:  
```
this script applies only to .txt files.
we need to collect all names & ids of actors from things_to_import directory
and compare them with a database
```  
  
(4)  git clone https://github.com/yehonadav/doom_light.git  
*  add the scripts from previous exercises  
*  create a script to check for new files conflicts:  
```
we need to collect all filenames from things_to_import and compare them with filenames from JonaDoom
and delete conflicting files from things_to_import
```  
  
(5)  git clone https://github.com/yehonadav/doom_light.git  
*  create a script to find the next available ids, if let's say we need 5 new ids, the script will return the next 5 unused ids    
  
(6)  git clone https://github.com/yehonadav/doom_light.git  
*  add the scripts from previous exercises  
*  replace your current database with an sqlite3 database  
  
(7)  git clone https://github.com/yehonadav/doom_light.git  
* add the scripts from previous exercises  
* create a script to update the database's actors after pasting new files to JonaDoom directory  
* if conflicts are found, ignore them  
* export an actors.csv file containing actor names and ids  
  
(8)  git clone https://github.com/yehonadav/doom_light.git  
* add the scripts from previous exercises  
* create a script to update the database's files after pasting new files to JonaDoom directory(database contains actor & file tables)  
* if conflicts are found, ignore them  
      
more exercises:  
---------   

if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  