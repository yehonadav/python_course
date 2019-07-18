# Exercises  
  
creating files:  
---------  
  
(1) create hello_world.py file  
* print "hello world"  
* run the file  
  
(2) create text.txt file  
* add this text:  
```text
From Wikipedia, the free encyclopedia
Jump to navigationJump to search
	Look up Text, Texts, text, or texts in Wiktionary, the free dictionary.
A text (in the sense of literary theory) is any object that can be read, including:
    Documents:
        Religious text, a writing that a religious tradition considers to be sacred
        Textbook, a book of instruction in any branch of study
Text may also refer to:
```  
  
(2) create books.json file  
* add this json:  
```json
[
  {
      "Title": "The Cuckoo's Calling",
      "Author": "Robert Galbraith",
      "Genre": "classic crime novel",
      "Detail": {
          "Publisher": "Little Brown",
          "Publication_Year": 2013,
          "ISBN-13": 9781408704004,
          "Language": "English",
          "Pages": 494
      },
      "Price": [
          {
              "type": "Hardcover",
              "price": 16.65
          },
          {
              "type": "Kidle Edition",
              "price": 7.03
          }
      ]
  }
]
```  
  
(3) create weather.csv file  
* add this text:  
```
month,avg_high,avg_low,record_high,record_low,avg_precipitation
Jan,58,42,74,22,2.95
Feb,61,45,78,26,3.02
Mar,65,48,84,25,2.34
Apr,67,50,92,28,1.02
May,71,53,98,35,0.48
Jun,75,56,107,41,0.11
Jul,77,58,105,44,0.0
Aug,77,59,102,43,0.03
Sep,77,57,103,40,0.17
Oct,73,54,96,34,0.81
Nov,64,48,84,30,1.7
Dec,58,42,73,21,2.56
```  
  
python console:  
---------  

(1)  
* open python console  
* enter your name in string format  
* calculate:  
```python
1+1
1-1
1+0.0
2*2
3/4
2**4
2**(1/2)
1+2*2*3/1.5
(1+5) * (2/6) * (1+2+3)
3%10
3//10
```  
* use the exit function  
  
printing:  
---------  
  
(1) create printing101.py  
* print your name  
* use concat to print your name and age (don't forget to space)  
* print 3 numbers separated by tabs  
* print 3 numbers separated by newlines  
* get 4 numbers using input and print their sum  
* print the 4 numbers sum as integers  
* get 3 numbers using input
* print the sum of the first 2 divided by the third
* print a rounded result with no more than 2 characters after the dot (3.333333 -> 3.33)
* get 2 numbers using input
* print how many times the second number consumes the first
* print the leftover  
  
  
text manipulation:  
---------  
  
(1) create stringing.py  
* create a text variable like so:  
```python
text = '''
Victor Hugo's ({}) tale of injustice, heroism and love follows the fortunes of Jean Valjean, an escaped convict determined to put his criminal past behind him. But his attempts to become a respected member of the community are constantly put under threat: by his own conscience, when, owing to a case of mistaken identity, another man is arrested in his place; and by the relentless investigations of the dogged Inspector Javert. It is not simply for himself that Valjean must stay free, however, for he has sworn to protect the baby daughter of Fantine, driven to prostitution by poverty. 

Norman Denny's ({}) lively English translation is accompanied by an introduction discussing Hugo's political and artistic aims in writing Les Miserables. 

Victor Hugo (1802-85) wrote volumes of criticism, dramas, satirical verse and political journalism but is best remembered for his novels, especially Notre-Dame de Paris (also known as The Hunchback of Notre-Dame) and Les Miserables, which was adapted into one of the most successful musicals of all time. 

'All human life is here'
Cameron Mackintosh, producer of the musical Les Miserables

'One of the half-dozen greatest novels of the world'
Upton Sinclair

'A great writer - inventive, witty, sly, innovatory' 
A. S. Byatt, author of Possession
'''
```  
* create name: string variable  
* create word1: string variable  
* create word2: string variable  
* create numbers: string variable  
* create small_letters: string variable  
* create big_letters: string variable  
* get the name index from the text  
* get the name+3 chars from the text  
* get the word1 index from the text range of 0-100  
* get the word2 index from the text range of text_length/2-text_length  
* get the count of the word 'of' from the text  
* check if the text starts with the name  
* check if the text ends with the name  
* format the curly braces of the text into a life span   
* split the text into words  
* join the words into a new text  
* join the words using ',' into a new text  
* join the words using ',' into a new text   
* join the words using '_' into a new text   
* join the words using ' ' into a new text   
* replace the words 'of' with '@🐔' into a new text  
* create a new capitalized text  
* create a new text with no occurrences of 'a'  
* create a new text with stripped trailing white-spaces  
* get the upper name  
* get the lower name  
* check if name is lower case  
* check if name is upper case  
* check if big_letters is upper case  
* check if small_letters is lower case   
* check if '90' is a number  
* check if '90.5' is a number  
* convert '90' into a whole number  
* convert '90.5' into a decimal  
* convert 183 into a string  
* check if '183' is a digit in the [1] position  
* get the first char of small_letters + the last char of big_letters  
* get the string of numbers excluding the first and last chars  
* get all even numbers from numbers  
* get all the odd numbers from numbers  
* print the results  
  
importing:  
---------  
  
(1) create data_structures.py file  
* in my_module.py create a name & age variables  
* from my_module.py import name & age
* import the random module  
* import get_data from exercises/data.py  
* create my_module.py  
  
free style:  
---------   

(1) in data_structures.py  
* use get_data to create 5 users  
* print users type  
* get the first user  
* print first user type  
* print users  
* print users using a for loop  
* print users using the dir() function  
* view the second user  
* get all user names using a for loop  
* get all user names using a while loop  
* get all user names using a list comprehension  
* get all user names using a set comprehension  
* get all user names using a dictionary comprehension (value is name length)  
* get all user names using a generator comprehension  
* get all user names using a for loop and a condition where name length is smaller than 10  
* get all user names using a while loop and a condition where name length is smaller than 10  
* get all user names using a list comprehension and a condition where name length is smaller than 10  
* get all user names using a set comprehension and a condition where name length is smaller than 10  
* get all user names using a dictionary comprehension (value is name length) and a condition where name length is smaller than 10  
* get all user names using a generator comprehension and a condition where name length is smaller than 10  
* view names  
* print names length  
* get the first name  
* get the last name  
* get all names excluding first and last  
* get names 0, 2, 4 ...  
* get names 1, 3, 5 ...  
* print the first name as upper case!  
* print the first name as lower case!  
* get the first and last characters of each name from names  
* sort the result  
* replace all characters with upper case characters  
* translate characters to numbers  
translate = {  
    'A': 0,  
    'B': 1,  
    'C': 2,  
    'D': 3,  
    'E': 4,  
    'F': 5,  
    'G': 6,  
    'H': 7,  
    'I': 8,  
    'J': 9,  
    'K': 10,  
    'L': 11,  
    'M': 12,  
    'N': 13,  
    'O': 14,  
    'P': 15,  
    'Q': 16,  
    'R': 17,  
    'S': 18,  
    'T': 19,  
    'U': 20,  
    'V': 21,  
    'W': 22,  
    'X': 23,  
    'Y': 24,  
    'Z': 25,  
}  
* translate strings to numbers  
* sort the numbers  
* sort in reverse  
* get a random user from users  
* get the user address  
* find 'A', 'B', 'c', 'd' first indexes in the address, why -1 might get printed?  
* count all occurrences of 'A', 'B', 'c', 'd' in the address  
* get all user ages  
* find the average age  
* find the middle(index wise) age  
* find the smallest age before sorting  
* find the biggest age before sorting  
* find the smallest age after sorting  
* find the biggest age after sorting  
* find the middle sorted age  
* multiply users by 3  
* check if 2 users share the same email address  
  
  
more exercises:  
---------    
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  