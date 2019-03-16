 Micro Services Web App 

This is a milestone project where you will be collaborating as a team to create a beautiful web application.  
each member of the team will own and develop a micro service to be used by other services of the app  
so that together the summary of your efforts will bring a working model of our architecture.  

Goal:
-----

Game sharing website  
  
  
Architecture:
============
![game over](https://github.com/yehonadav/python_course/blob/master/exercises/images/final.png?raw=true)    


product requirements:
---------------------

* on *localIPv4:5000* - a home page with: random business advertisements and newsletters feed, login & signup redirects  
* on *localIPv4:5001* - a login page with: validation & authentication on email+password/twitter/google/facebook logins  
* on *localIPv4:5001* - a login page with: a forgot password / signup / lock user / dashboard redirects  
* on *localIPv4:5002* - a user management system: storing user profiles and hashed salted passwords  
* on *localIPv4:5002* - a user management system: when authenticated a jwt token is generated and returned  
* on *localIPv4:5003* - a reset password page  
* on *localIPv4:5004* - a signup page  
* on *localIPv4:5005* - a userlock page  
* on *localIPv4:5006* - a dashboard that redirects to the games/profile/posts/friends/messages sections  
* on *localIPv4:5007* - a games page where users can upload and share games with their friends  
* on *localIPv4:5008* - a profile page with the user details  
* on *localIPv4:5009* - an authentication & authorization server  
* on *localIPv4:5010* - a posts page listing all of the user's posts  
* on *localIPv4:5011* - a friends page listing your friends, search new friends and go to friends posts  
* on *localIPv4:5012* - a private message page showing the user's messages to/from friends  
* on *localIPv4:501x* - ...if the team is big enough, you can add more pages as you like and see fit.  
  
basic instructions:
-------------------

each collaborator must share his IP, port number and routes as well as an api of the routes.  
each collaborator must share his source code via github: create a project and share it with other collaborators.  
run the application from the same LAN as the other collaborators.  
complicated services can be developed by a group of collaborators.  
HAVE FUN!  

score system:
-------------
  
* (+18) use at list 3 external dependencies in your projects  
* (+18) write at list 3 different apis in your projects  
* (+20) have interaction with databases or encryption or other languages(html/js/css/etc..)  
* (+10) own at list 1 project and determine its structure, design and architecture  
* (+10) have at list 1 interaction with other projects apis  
* (+14) make your project run correctly  
* (+10) have your project interact correctly with all of its peers  
* (+10 bonus) have the entire final project run properly  
*passing grade: 65*