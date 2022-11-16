# NFL Survivor Pool Application
The rules are simple. Pick one NFL team each week to win their game, and survive to play another week. 3 incorrect picks will eliminate you from the competition, so choose wisely.

## Contents
* [Project Brief](#Project-Brief)
* [Requirements](#Requirements)
* [App Design](#App-Design)
* [Database Schema](#Database-Schema)
* [Pipeline](#Pipeline)
* [Testing](#Testing)
* [The App](#The-App)
* [Future Work](#Future-Work)


## Project Brief: 
To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training. 

## Requirements:
* A Trello board (or equivalent Kanban board tech) 
* A relational database with at least 2 tables
* Clear Documentation
* A functional CRUD application created in Python
* Fully designed test suites
* Automated tests for validation
* A functioning front-end website
* Integrated API's, using Flask
* Code fully integrated into a Version Control System using the Feature-Branch model
* Built through a CI server 
* Deployed to a cloud-based virtual machine.

## App Design

I have chosen to create an application for an NFL Survivor Pool

Users will log into application ( create users and picks functionality ) and pick a team that they think will win their matchup each week for the season (update pick functionality). Each player can view the game matchups for each week of the season and also view their picks ( Read functionality ). They can also delete all of their picks ( Delete functionality )

Additional features:
They can only pick a team once per season (complete)
They start with 3 lives. ( not complete )
If they lose, they lose a life and when they run out of lives they cannot make any more picks (not complete)
You can cange your weekly picks up until the start of the first game for that week. (not complete)
They can join leagues and look at the leaderboard for that league and also look at past and present picks for other users in that league ( but not their future picks ) 

## Database Schema
### initial plan

![image](https://user-images.githubusercontent.com/116156199/201987265-57b8e63b-b673-446b-8754-a580c9a15822.png)

### current complete layout 

![image](https://user-images.githubusercontent.com/116156199/202020798-8e19ea0c-2680-478e-85dc-aec8ce8e5987.png)

## Pipeline

I used Trello for project tracking. Items were assigned MoSCow prioritisation and also categorised tasks by story ( Database, gitHub & Application )
Trello board can be accessed [here](https://trello.com/b/V4WOjJ9p/nflsurvivorpool)

![image](https://user-images.githubusercontent.com/116156199/202021926-b93a7d72-8c39-42bf-ad95-50a252814ca1.png)

I used a repository on git hub for version control

## Testing

I used unit testing tests to test my code. I am currently up to 6 psses and coverage of 96%

![image](https://user-images.githubusercontent.com/116156199/202136241-03e1e079-6c5c-4802-b90c-b89c7fdc3248.png)


## The App

The user is first brought to the home page where the user is invited to enter their username
![image](https://user-images.githubusercontent.com/116156199/202028110-3f2a77ef-ae78-43c7-9c46-46a139177881.png)

On entering a username, if the user already exists, they are brought to a page displaying their picks. If they do not exist, the user is created and then brought to the page displaying their picks

![image](https://user-images.githubusercontent.com/116156199/202028469-69f5cb3d-ae96-4277-8238-663ec9a4f48b.png)

The name of each week is a hyperlink and when selected, the game schedule for that week appears below the user picks

![image](https://user-images.githubusercontent.com/116156199/202028629-736ea702-37cf-49a8-b70f-b72538102a54.png)

The user can then select a team for that week. When they select the button beside their chosen team, their pick above is updated and the select button is replaced by a message saying 'Already chosen'. this message will appear for the picked teams for all of the weeks as each team can only be picked once a season. another team can be chosen for the week to update the pick

![image](https://user-images.githubusercontent.com/116156199/202029045-afd80018-cd0f-4370-9695-2bcefb7f05c6.png)

if you go back to the home page, you can see that once there are users, all of their picks will be displayed in a table ( that in the future will resemble more of a league leaderboard table ) with the option of deleting a user and their picks

![image](https://user-images.githubusercontent.com/116156199/202029436-0008928c-15b7-46cb-a306-5f9b3c95c335.png)

## Future Work

i would like to get some results in and mark off the picks as right or wrong and then add the 3 lives per user functionality
i would also like to add a proper login feature
Ideally long term, i would add a leagues table that users can join and a leaderboard for the league











