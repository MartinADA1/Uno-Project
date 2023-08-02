# Uno-Assignment
Python Uno Game for Advanced Programming Module.

Dependencies:
1. Termcolor -> Install termcolor using `pip install termcolor`

How to run the game:
1. Clone the repository with this link: 
2. Have python installed on your system
3. Open terminal and get to the `/UNO Project` folder
4. Type in `python uno_game.py` and press enter
5. The game should now be running!

## Challenge outline

The task that I decided to choose for this assignment was to try my hand at recreating the popular card game "Uno". The goal of Uno is for players to play all cards in their hand as soon as possible, both regular and powerful action cards are included in this game. I decided to implement a player vs AI option and a player vs player option, however, whilst planning this out in the initial stages of development I came across problems that I may have trouble taken care of later on in development. These problems, as well as their proposed solutions are listed below:

## Summary and review of the problem, overall proposed solution
# Discovered Problems

1. Initially due to the massive amount of things I would have to set up (e.g. the deck) I didn't want to end up with a massive block of code, which would result in me having a very hard time reading over and trying to refactor the code later on.
2. There are alot of rules and concepts in Uno that needed to be covered when coding this, due to the time restraints I had to ensure that my code wasn't repeatitive to make it as efficient as possible.
3. There are alot of different types of card types and actions when devevloping the game of uno so I had to ensure that I avoid having them fixed to one thing in the main code.

# Proposed Solutions

1. Made use of classes that included the set up of the game (such as creating the deck).
2.  Made sure that the game followed a modular approach so that many elements of the game are stored in different files.
3. Made sure to follow object orientated programming when tackling this problem, ensuring that I  made use of simplicity and abstraction in the main code - making the code much easier to come back to refactor as the readability was greatly increased making it much easier to understand.

## UML style diagram illustrating initial overall solution

[Image Link] https://ibb.co/g3DCBhS

## Initial working plan, overall approach, developmentstrategy and approach to quality

As mentioned above, due to the massive amount of requirements and rules that would be needed to be implemented in my Uno game in the given amount of time, I made sure to work in a agile methodology - this allowed me to ensure that I could be adaptable whilst coding as the scope of the game may have changed due to new problems arising, using agile would allow me to go back and change these things to accomodate in the code. My initial planning helped me in identifying the biggest problems that may have arose when taking on this project, I then deconstructed these identified problems into small tasks helping me to essentially create a to do list of things I needed to complete.

Once finishing the planning phase, I got to work on the game's creation. I decided to use an OOP (Object Oriented Programming) method while adopting a modular approach to ensure that the code is trustworthy, comprehensible, and easy to modify when going back to carry out updates or bug fixing. 

When the first development draft was finished I was able to take note of everything that needed to be fixed or added in, following this list and redoing this evaluation after each sprint of development I was able to ensure that the game was working well and contained no bugs.

## Analysis and decomposition of the overall problem into key ‘epic’ style tasks

As mentioned previously, due to carrying out the project using the agile methodology I was able to create smaller tasks from bigger problems that I discovered, resulting in me having a clear list of tasks to complete for the game to be finished. I used OOP to split the main sections of the game into their own classes and files to allow for easier management of these small tasks I created, an example of these will be listed below.

1. Cards: To create a card class that will have all elements related to the cards being used in the game.
2. Deck: To create a deck class that  will have all elements related to the deck being used in the game.
3. Hand: To create a deck class that  will have all elements related to the hand being used in the game.
4. Player Vs Player: To create a function that handled all logic in the case in which user wanted to play against another user.
5. Player Vs AI: To create a function that handled all logic in the case in which user wanted to play against the AI.
6. Main Menu: To create a main menu in the initial loop of the game that allows for users to choose what type of gameplay they want.

## Initial object-oriented design ideas and planned phased breakdown into smaller tasks

Below is a breakdown of the classes I created and the methods inside of them, as well as describing what they do:

Card Class
Gives required attributes to card objects, "color" and "cardtype".
- Assigns types to every type of card in the game
- Assigns color to each card based on its type (wild cards have no color)  

Deck Class
Creates deck by appending all card types and colors to an empty list twice to have 2 of every card in the game.
- shuffle: Randomly shuffles deck before dealing cardsd to players at start of game to ensure fairness.
- deal: Used to give a card to chosen player, makes use of .pop() function to ensure its from the top of the deck to stay inline with the rules of Uno.

Hand Class
Handles the users deck that they have in hand during gameplay.
- add_card: Used to add a card to chosen players hand.
- remove_card: Used to remove card from a players hand based on position/index.
- cards_in_hand: Used to display cards in hand to players in output.
- single_card: Used to temporarily hold a played card so it can be used to carry out the action later on.
- no_of_cards: Used to calculate amount of cards in a hand of chosen user.

### Development
## Adoption and use of ‘good’ standards

Whilst carrying out this project, I tried to ensure that I made use of good programming standards to ensure that my code is readable, doesnt smell and isn't repetitive. Examples of good programming practices I made use of are listed below:

1. Consistently used snake_case throughout the project when naming methods.
2. Made use of object orientated programming to make use of abstraction in my code to increase its simplicity to ensure it was easier to modify when applying updates/fixes.
3. I made sure not to repeat myself throughout the code to avoid unneccessary duplication of code where it wasn't needed.
4. Clear and consise comments were utilised throughout my code to ensure that I documented it well.
5. Used error handling to ensure that users weren't able to break the game with their inputs.

## Development Phases + Ensuring Quality through tests and resolving bugs
# Development Phase 1
Phase 1 of my development was to create the first draft of the initial game, in this first draft I created all three classes (card, deck and hand) - the aim was to get a first working version of the game to help identify problems and extra things to add to my game plan when testing it. These classes were used throughout the game logic so when testing my game it revolved around the functionality of my classes and their methods.

Once phase 1 was complete all of the code was in one file and didn't have the best coding standards used in its development.

# Development Phase 2
In phase 2 I rigourously tested this first draft and made a list of things to add on to improve the user experience and overall standard of code of my game.

As mentioned above my tests revolved around the functionality of my classes and their methods, to start off this phase I split these classes into their own modular files and imported them into the main game file to increase readability and make it easier for me to work on each class seperately now that they were in their own space. 

Below is everything I tested about my classes:

Card Class
- Ensuring that each type of card (number, action, action_nocolor) was assigned the right type.
- Ensuring that number and action type was directly assigned to their color..
- Making sure that wild cards were assigned to no color to allow them to be used in any situation.

Deck Class
- Ensuring that the right number of cards were created using a print deck length method (2 of every card).
- Ensuring that the deck was shuffled randomly consistently to make sure that fairness is upheld via the function.
- Ensuring that when cards are delt from the deck cards are taken from the top of the deck and nowhere else.

Hand Class
- Ensuring that the right amount of cards are added to players decks.
- Ensuring that only the played card is removed from deck when prompted.
- Ensuring that all the cards in a players hand are displayed each turn.

After testing all of these I went on to create a list of features to add to my game, this consisted of:

- Adding color to represent different cards.
- Updating print statements to be more descriptive, aiding user experience.
- Adding a main menu to allow for a user to chose if they want to play vs a player or AI.
- Formatting print statements to increase readability.
- Adding time.sleep functions between prints to ensure there isnt a overload of prints at once allowing for the user to process everything that is going on steadily.

As well as these, I updated the comments in my code to help with further modification later on in development.

# Development Phase 3
In this last phase I added all that I listed in phase 2 and used the same style testing to ensure that it worked correctly.

As well as this I continued to update my comments and carried on refactoring code (reducing repetitiveness, etc) to ensure that the final product was as clear as I could make it and upheld to good coding standards.

## Reflection on key design challenges, innovations and how they were solved

# Challenges I faced in development

1. Handling action_no_color cards color being shown in output.
2. Outputting every event happening in the game in a speed which isn't overwhelming for the user.
3. Making sure that inputs given by user aren't able to able to break again and are able to mitigate against them.

# Solutions to these challenges

1. This was taken care of by checking if the color attribute of card objects were "None" before trying to assign their color to prevent it causing an error.
2. This was resolved by identifying places where outputs became overwhelming and adding in time.sleep functions to take care of this.
3. Creating a loop that throws a message that users are inputting an invalid format till they select the right option - this message was highlighted in red to show its importance.

### Evaluation
## Analysis with embedded examples of key code refactoring, reuse, smells.

When handling action type cards and their effects this included the effects the card "draw 2" had on the opposing player, initially I had it as a repeated line of code making use of the add_card method.

[Image Link] https://ibb.co/cTvzWM0

After refactoring, I made use of a short for loop to get rid of this repetition in my code:

[Image Link] https://ibb.co/0Vv57gk

## Implementation and effective use of ‘advanced’ programming principles
In my code you can see that I've used object orientated programming, as well as this a modular approach has been used to help keep my code readable and easy to modify when needed. Error handling has also been added throughout the code to make sure that user inputs aren't able to stop my code from running. Repetitiveness was also avoided in my development to prevent alot of repeated code being pasted in a block of code.

Below are images to support the usage of these principles:

# Object orientated programming

[Image Link] https://ibb.co/PFXnfWr

# Modular approach

[Image Link] https://ibb.co/4Rgx0Z4

# Error handling

[Image Link] https://ibb.co/RhYkVzw

# DRY (Don't Repeat Yourself)

[Image Link] https://ibb.co/sJH4cdT

## Reflection
In conclusion, I believe my project, "Uno" was a success - it was playable with two different playstyles being vs Ai and another player, object orientated programming was well used to help the clearness of my code as well as using a modular approach. I feel that this challenge has helped me greatly with my understanding of classes and why they are used - especially how they help the clearness of code and when you go back to update anything. If there was something that I think I would've wanted to add on it would probably be to increase the amount of players or AI that could paly in a session, however due to the time given (and missing a week due to illness) this wasnt possible - I wouldve also liked to refactor the player vs player and player vs ai functions more to eventually make them useable from one function rather than 2.




