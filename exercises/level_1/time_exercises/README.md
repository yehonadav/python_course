# Time Modules Exercises  
  

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
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  