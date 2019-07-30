# Game Exercises  
  
      
(1)  Create a file ```love_msg.py```  
* create a cute messaging program between a dating couple  
  
(2)  Create a file ```guess_with_hints.py```  
* create a simple script to guess a sentence  
* add a looping mechanism, with a quit or retry options  
* using the sys module, use sys.argv to add a custom guess, if no guess was sent to the program, use the default guess value  
  
(3)  in ```guess_with_hints.py```  
* create hints & tries counters  
* create a guess_is_correct function:  
```
    if tries equals to 1:
        print "you guessed correctly"
        print "amazinggggg!!"
    otherwise:
        print "you guessed correctly after {tries} tries"
        if hints equals to 0:
            print "amazing"
        otherwise if hints equals to 1:
            print "awesome"
        otherwise if hints equals to 2:
            print "very good"
        otherwise if hints equals to 3:
            print "nice try"
        otherwise if 3 < hints < 7:
            print "and it only took you {hints} hints"
        otherwise:
            print "with {hints} hints .."
```  
  
(4)  in ```guess_with_hints.py```  
* convert the script into a play function and run it in a ```__name__ == "__main__"``` condition  
* put all the functions in a class  
* create a hint_help function  
  
(5)  in ```guess_with_hints.py```  
* configure the hint_help as follows:
```python
hint = input("maybe a hint would help? y/n")
if hint == 'y':
    self.hints += 1
    if self.hint_the_word_size_of_the_sentence(): return 
    if self.hint_the_letter_size_of_a_word(): return 
    if self.hint_the_edges_of_a_word(): return 
    if self.hint_a_word(): return     
    print("sorry, out of clues")
```
* create the hint_help's dependent functions  
* ```def hint_the_letter_size_of_a_word(self):```, should give the letter size of all words, but only 1 word per hint  
* ```def hint_the_edges_of_a_word(self):```, should give the letter edges of all words, but only 1 letter per 1 word per hint  
* ```def hint_a_word(self):```, should give out all words, but only 1 word per hint  
  
(6)  in ```guess_with_hints.py```  
* configure class variables to improve performance:  
```python
    words = guess.split(?)
    words_length = len(words)
    hint_word_edges_range = range(?, ?)
```  

more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  