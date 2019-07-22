# Error Handling Exercises  
  
  
(1)  Create a file ```zero_division.py```
* create a function ```create_numbers``` that returns a list of  
  random numbers with a random length between 0-9  
* create a function ```avg``` that takes the list of ```create_numbers``` and returns an average number  
* create a function ```print_average``` that takes the list of ```create_numbers``` and try to print the average  
* if ```print_average``` fail with ```ZeroDivisionError``` or ```TypeError``` it will print  
  the error and return it.  
* make a main program to call ```print_average``` until failure.  
  
  
(2)  Create a file ```type_error.py```
* use and import functions from ```zero_division.py```  
* create a function ```randomly_stringify_list_items```
* make a main program to:  
  create random list of numbers  
  randomly stringify some numbers  
  ```print_average``` until failure.  
  
(3)  Create a file ```quadratic.py```
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
  
  
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  