# OOP Exercises  
  
  
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
  
  
(8)  create ```play_hunter.py```  
* create classes: Tiger, Wolf, Archer, Player  
* player can inherit one of the classes and use them  
* Tiger: name, health, method meow(when hurt), method killed  
* Wolf: name, health, method bark(when hurt), method killed  
* Archer: name, health, method shoot  
* player is an archer that kill bad Characters  
* create a program of a player and some Characters, kill them  
* add elephant, rhino, give them attack_back method  
* use inheritance to improve the code  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  