import random
from card import Card
from hand import Hand
from deck import Deck
from termcolor import colored

#Funciton to randomly select who starts first (Player Vs. AI)
def choose_first_playerVAI():
    if random.randint(0,1)==0:
        return 'Player'
    else:
        return 'Pc'

#Function to check if the card thrown by Player/AI is a valid card by comparing it with the top card
def single_card_check(top_card,card):
    if card.color==top_card.color or top_card.rank==card.rank or card.cardtype=='action_nocolor':
        return True
    else:
        return False
    
#FOR AI ONLY
#To check if AI has any valid card to throw 
def full_hand_check(hand,top_card):
    for c in hand.cards:
        if c.color==top_card.color or c.rank == top_card.rank or c.cardtype=='action_nocolor':
            return hand.remove_card(hand.cardsstr.index(str(c))+1)
    else:
        return 'no card'


#Function to check if either wins
def win_check(hand):
    if len(hand.cards)==0:
        return True
    else:
        return False
    
def playerVAI():

#Main Menu
while True:

    print(15*"-" + " Martin's UNO Main Menu " + 15*"-" + "\n\n")
    print(" [1]. Player VS. Computer "+ "\n")
    print(" [2]. Player VS. Player "+ "\n")
    print(" [3]. Quit "+ "\n\n")
    print(54*"-")

    # Lets player(s) choose what they want to play
    option = int(input("Please select an option: "))

    if option == 1:
        # playerVAI()
    
    elif option == 2:
        # playerVplayer()

    elif option == 3:
        break
    
    # If invalid input is given this error message is given and player will have to input a correct choice
    else:
        print(colored("Invalid choice, please choose a valid option: ", "black", "on_red"))
        print("")