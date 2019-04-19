
# RIDDLE ME THIS

[Website](https://milestone-project-three-ag.herokuapp.com/)

Riddle Me This is a question and answer game developed as an exercise in the Flask framework for Python.

## UX

The UX is very simple, relying entirely on Bootstraps core elements for design. While I enjoyed the challenge of the project, I couldn't come up with a theme to center my design around, and as such it is very basic, but perfectly functional.

## USER STORIES

- As a user I want to be able to specify a username
- As a user I want my username to identify me and track my progress
- As a user I want to be given clearly defined instructions
- As a user I want to be given clear feedback on my input


## FEATURES  

- Players are asked to input a username prior to playing the game. This does not need to be unique
- The Player is then presented with a series of 10 questions
- Each question allows the player 3 guesses, and the previous guess is displayed to the user in case they forget the guess
- Each answer awards the player 10 points, up to a maximum of 100 points
- If the player answers incorrectly 3 times, the game ends and the user is presented with the scoreboard
- If the player attempts to manipulate the game incorrectly, the game ends and the user is presented with the scoreboard, where they will have been logged and flagged as a cheater
 - The user can reset the game at any time

## TESTING

The application was tested thouroughly throughout development. All of the following tests were run numerous times:
 = Attempt to start game with no user name
 = Attempt to answer question with no input
 = Attempt to progress game beyond current question through URL manipulation
 = Attempt to resume a session that has been reset
 = Attempt to cause bugs by running multiple instances of the game

### Responsiveness

Given that the site is essentially plain Bootstrap markup, it is fully responsive down to the smallest smartphone screen size, with the small exceoption of a slight overflow on the Leaderboard table. 


## TECHNOLOGIES

- Python
- MySQL
- Flask
- HTML
- CSS
- Bootstrap

## DEPLOYMENT
 
 COMMANDS USED TO DEPLOY PROJECT TO Heroku:
 
- git init (create empty repository)
- git add ( to add files)
- git commit -m'' (to commit changes and add message)
- heroku login (To log in to heroku platform)
- heroku ps:scale web=1 (to run app on heroku)
- git push heroku master ( to push local repository to heroku)


## CREDITS


