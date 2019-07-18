# Exercises
  
Games 
---------
  
(1)  create a black jack game  
  
(2)  Build a randomly generated Python space game.  
With traveling, trading, mining, resource management, battles and storyline events  
along with saving the users data to that of an output file.  
  
(3)  Create a snake game using the pygame module  
![Snake](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/sanke.JPG?raw=true)  
* Create a python package ```snake```  
![Snake package](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/snake_package.JPG?raw=true)  
* create a ```__main__.py``` file for the package  
  and import a Play class to run the game.  
* create a play.py file with a Play class.  
  the Play class should contain a ```run```,```restart``` & ```start```  
  methods to run the game, go back to the menu & start the menu.  
  an ```__init__``` method should also be defined with some variables:  
  self.menu: to include the menu object.  
  self.game: to include the running game object.  
  self.screenX & self.screenY: to set the screen size of the game.  
  after setting the variables the init method should call the start method.  
* import a Game & StartMenu classes from the snake package.
* create a game.py & menu.py file to import from.  
* in the StartMenu class create a start & exit buttons
  for calling sys.exit() or proceeding to choose a game size.
![menu](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/menu.JPG?raw=true)  
* have a choose_size method with ```Small Normal Big``` buttons  
  to set the snake & apple sizes and proceeding to choose a difficulty level.
![choose size](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_size.JPG?raw=true)  
* have a choose_difficulty method with ```Easy Normal Hard Expert``` buttons  
  to set the snake moving speed and proceeding to run the game.  
![choose difficulty](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/choose_difficulty.JPG?raw=true)  
* use these methods to run the game from the menu:  
```    
    def easy(self):
        self.game.run(0.25, self.size)

    def normal(self):
        self.game.run(0.5, self.size)

    def hard(self):
        self.game.run(1, self.size)

    def expert(self):
        self.game.run(2, self.size)
```  
* create a mainloop method to run events in the menu.  
* create a resources package, add snake.py & apple.py  
  and create a Snake & Apple classes.  
* go to the ```game.py``` file, import the Snake & Apple classes  
* create a Game class
* use the ```__init__``` method to set the screen
* create an over method to show the score, go back to the menu or exit the program  
![game over](https://github.com/yehonadav/python_course/blob/master/exercises/level_3/snake/images/game_over.JPG?raw=true)  
* create a loop method that will:  
  fill the screen ```self.screen.fill((30, 40, 100))```  
  update the snake object ```self.snake.update()```  
  check snake for collisions  
  check for apples  
  update image positions of snake & apple  
  check for key events  
good luck!  
  
    
more exercises:  
---------   
    
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  