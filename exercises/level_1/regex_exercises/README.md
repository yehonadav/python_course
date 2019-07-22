# regEx Exercises  
  

  
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
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  