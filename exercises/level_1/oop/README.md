# OOP Exercises  
  
      
(1)  Create a file ```calculator.py```  
* create a ```Calculator```  class  with ```a, b``` arguments  
* create ```display``` method to print the numbers and the last result  
* create ```add``` method to calculate ```a+b```  
* create ```sub``` method to calculate ```a-b```  
* make sure the result is shared between all calculators  
* test the calculators(level 2)  
  
(2)  in ```calculator.py```  
* create a Calculator2 class that inherits the Calculator class  
* change the last result to a list of results  
* add multiplication method  
* create 3 calculators and make some calculations  
* view the different results  
* override the Calculator methods that needs changes(all but the __init__ method)  
  
(3)  Create a file ```inherit.py```  
* use ```time``` & ```datetime``` modules  
* create ```Time``` class with ```get_time``` method, to get a time signature (epoc time)  
* create ```Date``` class with ```get_date``` method, to get a date signature (datetime object)  
* ```Date``` class inherit ```Time``` class  
* create a main program condition:  
  ```if __name__ == "__main__":```  
  use both classes and their available methods  
  
(4)  Create a file ```athlete.py```  
* create ```Athlete``` class with ```name, power, speed, endurance, weight``` arguments  
* make sure if the speed of the athlete is smaller than the endurance, redefine its value to equal: endurance+3  
  
(5)  in ```athlete.py```  
* create class ```Runner``` and inherit ```Athlete```  
* in the runner's ```__init__``` method, set a default value of power, speed & endurance to 0  
* in the runner's ```__init__``` method, set a default value of weight to 60  
* boost the runner's power by 10 percent of its weight  
* boost runner's speed by 25kmh  
* boost the runner's endurance by 8  
* create a ```get_duration``` method with this code:  
```python
acceleration = self.power / self.weight
top_speed = self.speed
time_to_reach_top_speed = top_speed / acceleration
distance_to_top_speed = top_speed * time_to_reach_top_speed / 2

if distance == distance_to_top_speed:
    duration = time_to_reach_top_speed

elif distance < distance_to_top_speed:
    duration = (2 * distance / acceleration) ** (1 / 2)

else:
    deceleration = acceleration
    endurance_speed = self.endurance
    time_to_reach_endurance_speed = top_speed - endurance_speed / deceleration
    distance_to_endurance_speed = top_speed * time_to_reach_endurance_speed / 2

    if distance == distance_to_top_speed + distance_to_endurance_speed:
        duration = time_to_reach_endurance_speed
    elif distance < distance_to_top_speed + distance_to_endurance_speed:
        duration = time_to_reach_top_speed + (2 * (distance - distance_to_top_speed) / deceleration) ** (1 / 2)
    else:
        time_to_reach_distance = (distance - (distance_to_top_speed + distance_to_endurance_speed)) / endurance_speed
        duration = time_to_reach_top_speed + time_to_reach_endurance_speed + time_to_reach_distance
```  
return the duration result  
* ```def get_duration(self, ?)``` needs an argument, add the missing argument  
* create a ```run``` method that receives a distance(in meters) parameter  
* in the ```run``` method get the running duration of the distance and use time.sleep to wait until the running operation is done  
* in the ```run``` method return the a runner's name  
  
(6)  in ```athlete.py```  
* create a class ```Sprinter``` and inherit ```Runner```  
* in the sprinter's ```__init__``` method, set a default value of power, speed & endurance to 0  
* in the sprinter's ```__init__``` method, set a default value of weight to 70  
* boost the sprinter's power by 75 percent of its weight on top of the runner's boost  
* boost sprinter's speed by 15kmh on top of the runner's boost  
* boost the sprinter's endurance by 1 on top of the runner's boost  
  
(7)  in ```athlete.py```  
* create a class ```MarathonRunner``` and inherit ```Runner```  
* in the marathon runner's ```__init__``` method, set a default value of power, speed & endurance to 0  
* in the marathon runner's ```__init__``` method, set a default value of weight to 55  
* divide the marathon runner's power by 1.1 on top of the runner's boost  
* decrease marathon runner's speed by 3kmh on top of the runner's boost  
* boost the marathon runner's endurance by 7 on top of the runner's boost  
* after the runner's boost, if marathon runner's speed <= 8, set it to equal 8  
* after the runner's boost, if marathon runner's speed < marathon runner's endurance + 1, set it to equal to marathon runner's endurance + 1  
  
(8)  in ```athlete.py```  
* create a main program condition:  
  ```if __name__ == "__main__":```  
* create a tuple of distances: 100m, 200m, 800m, 1.6km, 5km, 20km  
* create a tuple of athletes with 2 sprinters, 1 runner & 1 marathon runner  
* iterate the distances  
*   iterate the athletes for each distance(nested loop)  
*     get the running duration  
*     print the name, distance, and running duration of the athlete
*     when printing the running duration, use this format: ```(a)hr (b)min (c.xx)sec```
  
(9)  Create a file ```timer.py```  
* create ```Measurement``` class with ```date``` & ```run_time``` methods  
  
(10)  in ```timer.py```  
* import ```Date```  from exercise 3  
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
  
(11)  in ```timer.py```  
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
  
(12)  in ```timer.py``` class ```Timer```  
* add doc string explaining the Timer API
* add a hint typing for ```f``` argument hinting it is a function (callable)  
  
  
(13)  create ```play_hunter.py```  
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
  