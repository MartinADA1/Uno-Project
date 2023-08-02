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
    
#Funciton to randomly select who starts first (Player Vs. Player)
def choose_first_playerVplayer():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'

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
    
def playerVplayer():
    while True:

        print('\nWelcome to UNO! Finish your cards first to win!')
        
        p1_name = input("\nPlayer 1, please enter your name: ")
        p2_name = input("Player 2, please enter your name: ")

        deck = Deck()
        deck.shuffle()

        # Dealing the initial 7 cards
        player1_hand = Hand()
        for i in range(7):
            player1_hand.add_card(deck.deal())

        player2_hand = Hand()
        for i in range(7):
            player2_hand.add_card(deck.deal())

        # Setting the card at top of deck for players to play ontop of
        top_card = deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = deck.deal()
        print('\nThe starting card is: {}'.format(top_card))
        playing = True

        turn = choose_first_playerVplayer()

        if turn == 'Player 1':
            print('\n' + p1_name + ' will go first')
        else:
            print('\n' + p2_name + ' will go first') 
        
        while playing:
            
            # Player 1 Logic
            if turn == 'Player 1':
                print(colored("\nIt's " + p1_name + "'s turn\n", attrs=['bold']))
    

                print('The top card is: ' + str(top_card))
                print('Your cards: ')

                player1_hand.cards_in_hand()
                player1_choice = input("\nWould you like to Play or Draw? (p/d): ")

                # If player 1 chooses to play a card
                if player1_choice == 'p':
                    pos = int(input('Enter number of the card you want to play: '))
                    temp_card = player1_hand.single_card(pos)

                    # Checking if the chosen card is valid to play
                    if single_card_check(top_card, temp_card) == True:
                        # If it's a number type card it'll be played without any extra effects
                        if temp_card.cardtype == 'number':
                            top_card = player1_hand.remove_card(pos)
                            print("\n" + p1_name + f" has played {temp_card}")
                
                            turn = 'Player 2'
                        else:
                            # If chosen card is a skip or reverse, the other players turn is skipped
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Player 1'
                                top_card = player1_hand.remove_card(pos)
                                print("\n" + p1_name + f" has played {temp_card}")
                    
                            # If chosen card is a draw 2, other players turn is skipped and they draw 2 cards
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    player2_hand.add_card(deck.deal())
                                top_card = player1_hand.remove_card(pos)
                                print("\n" + p1_name + f" has played {temp_card}")
                    
                                turn = 'Player 1'
                            # If chosen card is a draw 4, other players turn is skipped and they draw 4 cards
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    player2_hand.add_card(deck.deal())
                                top_card = player1_hand.remove_card(pos)
                                # Player 1 gets to choose which color is in play after playing a draw 4
                                draw4color = input('Enter which color you want to change to: ')
                                if draw4color != draw4color.upper():
                                    draw4color = draw4color.upper()
                                top_card.color = draw4color
                                print("The color has been changed to " + f"{draw4color}")
                    
                                turn = 'Player 1'
                            # If chosen card is a wild card, player 1 can choose which color is in play    
                            elif temp_card.rank == 'Wild':
                                top_card = player1_hand.remove_card(pos)
                                wildcolor = input('Enter which color you want to change to: ')
                                if wildcolor != wildcolor.upper():
                                    wildcolor = wildcolor.upper()
                                top_card.color = wildcolor
                                print("The color has been changed to " + f"{wildcolor}")
                    
                                turn = 'Player 2'
                    else:
                        print('This card cannot be used')
                
                # If player 1 chooses to draw
                elif player1_choice == 'd':
                    temp_card = deck.deal()
                    print('You got: ' + str(temp_card))
        
                    # If card is valid player 1 will get a chance to play it
                    if single_card_check(top_card, temp_card):
                        player1_hand.add_card(temp_card)
                    # If not player 1 will have the card added to their deck and their turn ends
                    else:
                        print('Cannot use this card')
                        player1_hand.add_card(temp_card)
                        turn = 'Player 2'
                if win_check(player1_hand) == True:
                    print('\n' + p1_name + ' WON!!')
                    playing = False
                    break
            
            # Player 2 Logic
            if turn == 'Player 2':
                print(colored("\nIt's " + p2_name + "'s turn\n", attrs=['bold']))
    

                print('The top card is: ' + str(top_card))
                print('Your cards: ')

                player2_hand.cards_in_hand()
                player2_choice = input("\nWould you like to Play or Draw? (p/d): ")

                # If player 2 chooses to play a card
                if player2_choice == 'p':
                    pos = int(input('Enter number of the card you want to play: '))
                    temp_card = player2_hand.single_card(pos)

                    # Checking if the chosen card is valid to play
                    if single_card_check(top_card, temp_card) == True:
                        # If it's a number type card it'll be played without any extra effects
                        if temp_card.cardtype == 'number':
                            top_card = player2_hand.remove_card(pos)
                            print("\n" + p2_name + f" has played {temp_card}")
                
                            turn = 'Player 1'
                        else:
                            # If chosen card is a skip or reverse, the other players turn is skipped
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Player 2'
                                top_card = player2_hand.remove_card(pos)
                                print("\n" + p2_name + f" has played {temp_card}")
                    
                            # If chosen card is a draw 2, other players turn is skipped and they draw 2 cards
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    player1_hand.add_card(deck.deal())
                                top_card = player2_hand.remove_card(pos)
                                print("\n" + p2_name + f" has played {temp_card}")
                    
                                turn = 'Player 2'
                            # If chosen card is a draw 4, other players turn is skipped and they draw 4 cards
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    player1_hand.add_card(deck.deal())
                                top_card = player2_hand.remove_card(pos)
                                # Player 2 gets to choose which color is in play after playing a draw 4
                                draw4color = input('Enter which color you want to change to: ')
                                if draw4color != draw4color.upper():
                                    draw4color = draw4color.upper()
                                top_card.color = draw4color
                                print("The color has been changed to " + f"{draw4color}")
                    
                                turn = 'Player 2'
                            # If chosen card is a wild card, player 2 can choose which color is in play  
                            elif temp_card.rank == 'Wild':
                                top_card = player2_hand.remove_card(pos)
                                wildcolor = input('Enter which color you want to change to: ')
                                if wildcolor != wildcolor.upper():
                                    wildcolor = wildcolor.upper()
                                top_card.color = wildcolor
                                print("The color has been changed to " + f"{wildcolor}")
                    
                                turn = 'Player 1'
                    else:
                        print('This card cannot be used')

                # If player 2 chooses to draw
                elif player2_choice == 'd':
                    temp_card = deck.deal()
                    print('You got: ' + str(temp_card))
        
                    # If card is valid player 2 will get a chance to play it
                    if single_card_check(top_card, temp_card):
                        player2_hand.add_card(temp_card)
                    # If not player 2 will have the card added to their deck and their turn ends
                    else:
                        print('Cannot use this card')
                        player2_hand.add_card(temp_card)
                        turn = 'Player 1'
                if win_check(player1_hand) == True:
                    print('\n' + p2_name + ' WON!!')
                    playing = False
                    break

        # If a player wins, asks user if they'd like to play again                
        new_game = input('Would you like to play again? (y/n)')
        # Restarts loop if yes
        if new_game == 'y':
            continue
        # Prints thank you message and ends game if no
        else:
            print('\nThanks for playing!')
            break
    
def playerVAI():
    while True:

        print('\nWelcome to UNO! Finish your cards first to win!')

        player_name = input("Please enter your name: ")
        pc_name = "Computer"

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        for i in range(7):
            player_hand.add_card(deck.deal())

        pc_hand = Hand()
        for i in range(7):
            pc_hand.add_card(deck.deal())

        top_card = deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = deck.deal()
        print('\nThe starting card is: {}'.format(top_card))
        playing = True

        turn = choose_first_playerVAI()

        # Player logic
        # Same as player logic in function above
        if turn == "Player":
            print('\n' + player_name + ' will go first')
        else:
            print('\n' + pc_name + ' will go first')

        while playing:

            if turn == 'Player':
                print(colored("\nIt's your turn\n",attrs=['bold']))
                print('The top card is: ' + str(top_card))
                print('Your cards: ')
                player_hand.cards_in_hand()
                choice = input("\nWould you like to Play or Draw? (p/d): ")
                if choice == 'p':
                    pos = int(input('Enter number of the card you want to play: '))
                    temp_card = player_hand.single_card(pos)
                    if single_card_check(top_card, temp_card) == True:
                        if temp_card.cardtype == 'number':
                            top_card = player_hand.remove_card(pos)
                            print("\nYou played {temp_card}")
                            turn = 'Pc'
                        else:
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Player'
                                top_card = player_hand.remove_card(pos)
                                print("\nYou played {temp_card}")
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    pc_hand.add_card(deck.deal())
                                top_card = player_hand.remove_card(pos)
                                print("\nYou played {temp_card}")
                                turn = 'Player'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    pc_hand.add_card(deck.deal())
                                top_card = player_hand.remove_card(pos)
                                draw4color = input('Enter which color you want to change to: ')
                                if draw4color != draw4color.upper():
                                    draw4color = draw4color.upper()
                                top_card.color = draw4color
                                print("The color has been changed to " + f"{draw4color}")
                                turn = 'Player'
                            elif temp_card.rank == 'Wild':
                                top_card = player_hand.remove_card(pos)
                                wildcolor = input('Enter which color you want to change to: ')
                                if wildcolor != wildcolor.upper():
                                    wildcolor = wildcolor.upper()
                                top_card.color = wildcolor
                                print("The color has been changed to " + f"{wildcolor}")
                                turn = 'Pc'
                    else:
                        print('This card cannot be used')

                elif choice == 'd':
                    temp_card = deck.deal()
                    print('You got: ' + str(temp_card))
                    if single_card_check(top_card, temp_card):
                        player_hand.add_card(temp_card)
                    else:
                        print('Cannot use this card')
                        player_hand.add_card(temp_card)
                        turn = 'Pc'
                if win_check(player_hand) == True:
                    print('\n' + player_name + ' WON!!')
                    playing = False
                    break
            
            # Computer AI Logic
            if turn == 'Pc':
                temp_card = full_hand_check(pc_hand, top_card)
                # If PC has a valid card to play in hand itll be played
                if temp_card != 'no card':
                    print('\n' + pc_name + f' throws: {temp_card}')
                    # If the played card is a number type, ai's turn ends
                    if temp_card.cardtype == 'number':
                        top_card = temp_card
                        turn = 'Player'
                    # If played card is a skip or reverse, players turn is skipped
                    else:
                        if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                            turn = 'Pc'
                            top_card = temp_card
                        # If played card is a draw 2, players turn is skipped and they have to draw 2 cards
                        elif temp_card.rank == 'Draw2':
                            for i in range(2):
                                player_hand.add_card(deck.deal())
                            top_card = temp_card
                            turn = 'Pc'
                        # If played card is a draw 4, players turn is skipped and they have to draw 4 cards
                        # AI also chooses to what colour is changed to
                        elif temp_card.rank == 'Draw4':
                            for i in range(4):
                                player_hand.add_card(deck.deal())
                            top_card = temp_card
                            draw4color = pc_hand.cards[0].color
                            print('Color changes to', draw4color)
                            top_card.color = draw4color
                            turn = 'Pc'
                        # If wild card is played, AI chooses what the color changes to
                        elif temp_card.rank == 'Wild':
                            top_card = temp_card
                            wildcolor = pc_hand.cards[0].color
                            print("Color changes to", wildcolor)
                            top_card.color = wildcolor
                            turn = 'Player'

                # If AI doesnt have a valid card to play it will draw from deck
                else:
                    print('\n' + pc_name + ' pulls a card from deck')
                    temp_card = deck.deal()
                    # If drawn card is valid AI will play it
                    if single_card_check(top_card, temp_card):
                        print('\n' + pc_name + f' throws: {temp_card}')
                        # Same action card logic as above
                        if temp_card.cardtype == 'number':
                            top_card = temp_card
                            turn = 'Player'
                        else:
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Pc'
                                top_card = temp_card
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    player_hand.add_card(deck.deal())
                                top_card = temp_card
                                turn = 'Pc'
                            elif temp_card.rank == 'Draw4':
                                for i in range(4):
                                    player_hand.add_card(deck.deal())
                                top_card = temp_card
                                draw4color = pc_hand.cards[0].color
                                print('Color changes to', draw4color)
                                top_card.color = draw4color
                                turn = 'Pc'
                            elif temp_card.rank == 'Wild':
                                top_card = temp_card
                                wildcolor = pc_hand.cards[0].color
                                print('Color changes to', wildcolor)
                                top_card.color = wildcolor
                                turn = 'Player'
                    # If not turn ends for AI
                    else:
                        print(pc_name + ' doesnt have a card')
                        pc_hand.add_card(temp_card)
                        turn = 'Player'
                print('\n' + pc_name + ' has {} cards remaining'.format(pc_hand.no_of_cards()))
                if win_check(pc_hand) == True:
                    print('\nThe ' + pc_name + ' has WON!!')
                    playing = False

        new_game = input('Would you like to play again? (y/n)')
        if new_game == 'y':
            continue
        else:
            print('\nThanks for playing!!')
            break

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
        playerVAI()
    
    elif option == 2:
        # playerVplayer()

    elif option == 3:
        break
    
    # If invalid input is given this error message is given and player will have to input a correct choice
    else:
        print(colored("Invalid choice, please choose a valid option: ", "black", "on_red"))
        print("")