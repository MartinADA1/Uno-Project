import random
import time
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
    
def player_action(player_name, player_hand, opponent_hand, top_card, deck):

    win = False
    skip_turn = False

    print(colored("\nIt's " + player_name + "'s turn\n", attrs=['bold']))
    time.sleep(1)

    print('The top card is: ' + str(top_card))
    print('Your cards: ')

    player_hand.cards_in_hand()
    player_choice = input("\nWould you like to Play or Draw? (p/d): ")

    # If player chooses to play a card
    if player_choice == 'p':
        pos = int(input('Enter number of the card you want to play: '))
        temp_card = player_hand.single_card(pos)

        # Checking if the chosen card is valid to play
        if single_card_check(top_card, temp_card):
            # If it's a number type card it'll be played without any extra effects
            if temp_card.cardtype == 'number':
                top_card = player_hand.remove_card(pos)
                print("\n" + player_name + f" has played {temp_card}")
                time.sleep(1)
            else:
                # If chosen card is a skip or reverse, the next player's turn is skipped
                if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                    skip_turn = True
                    top_card = player_hand.remove_card(pos)
                    print("\n" + player_name + f" has played {temp_card}")
                    time.sleep(1)
                # If chosen card is a draw 2, the next player's turn is skipped and they draw 2 cards
                elif temp_card.rank == 'Draw2':
                    skip_turn = True
                    for i in range(2):
                        draw_card = deck.deal()
                        opponent_hand.add_card(draw_card)
                    top_card = player_hand.remove_card(pos)
                    print("\n" + player_name + f" has played {temp_card}")
                    time.sleep(1)
                # If chosen card is a draw 4, the next player's turn is skipped and they draw 4 cards
                # The player also gets to choose the color in play after playing a draw 4
                elif temp_card.rank == 'Draw4':
                    skip_turn = True
                    for i in range(4):
                        draw_card = deck.deal()
                        opponent_hand.add_card(draw_card)
                    top_card = player_hand.remove_card(pos)
                    draw4color = input('Enter which color you want to change to: ')
                    if draw4color != draw4color.upper():
                        draw4color = draw4color.upper()
                    top_card.color = draw4color
                    print("The color has been changed to " + f"{draw4color}")
                    time.sleep(1)
                # If chosen card is a wild card, the player can choose the color in play
                elif temp_card.rank == 'Wild':
                    top_card = player_hand.remove_card(pos)
                    wildcolor = input('Enter which color you want to change to: ')
                    if wildcolor != wildcolor.upper():
                        wildcolor = wildcolor.upper()
                    top_card.color = wildcolor
                    print("The color has been changed to " + f"{wildcolor}")
                    time.sleep(1)
        else:
            print('This card cannot be used')

    # If player chooses to draw
    elif player_choice == 'd':
        temp_card = deck.deal()
        print('You got: ' + str(temp_card))
        time.sleep(1)
        # If card is valid, player will get a chance to play it
        if single_card_check(top_card, temp_card):
            player_hand.add_card(temp_card)
        # If not, player will have the card added to their hand and their turn ends
        else:
            print('Cannot use this card')
            player_hand.add_card(temp_card)

    if win_check(player_hand):
        win = True

    return top_card, win, skip_turn
    
def playerVplayer():
    while True:
        print('\nWelcome to UNO! Finish your cards first to win!')
        time.sleep(1)
        p1_name = input("\nPlayer 1, please enter your name: ")
        p2_name = input("Player 2, please enter your name: ")
        deck = Deck()
        deck.shuffle()

        player1_hand = Hand()
        for i in range(7):
            player1_hand.add_card(deck.deal())

        player2_hand = Hand()
        for i in range(7):
            player2_hand.add_card(deck.deal())

        top_card = deck.deal()
        if top_card.cardtype != 'number':
            while top_card.cardtype != 'number':
                top_card = deck.deal()
        print('\nThe starting card is: {}'.format(top_card))
        time.sleep(1)
        playing = True

        turn = choose_first_playerVplayer()
        if turn == 'Player 1':
            print('\n' + p1_name + ' will go first')
        else:
            print('\n' + p2_name + ' will go first')
        
        time.sleep(2)

        while playing:
            if turn == 'Player 1':
                top_card, win, skip_turn = player_action(p1_name, player1_hand, player2_hand, top_card, deck)
                if win:
                    print('\n' + p1_name + ' WON!!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Player 1'  # Skip the next player's turn
                else:
                    turn = 'Player 2'
            elif turn == 'Player 2':
                top_card, win, skip_turn = player_action(p2_name, player2_hand, player1_hand, top_card, deck)
                if win:
                    print('\n' + p2_name + ' WON!!')
                    playing = False
                    break
                if skip_turn:
                    turn = 'Player 2'  # Skip the next player's turn
                else:
                    turn = 'Player 1'

        new_game = input('Would you like to play again? (y/n)')
        if new_game != 'y':
            print('\nThanks for playing!')
            break
    
def playerVAI():
    while True:

        print('\nWelcome to UNO! Finish your cards first to win!')
        time.sleep(1)

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
        time.sleep(1)
        playing = True

        turn = choose_first()

        # Player logic
        # Same as player logic in function above
        if turn == "Player":
            print('\n' + player_name + ' will go first')
        else:
            print('\n' + pc_name + ' will go first')

        while playing:

            if turn == 'Player':
                print(colored("\nIt's your turn\n",attrs=['bold']))
                time.sleep(1)
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
                            time.sleep(1)
                            turn = 'Pc'
                        else:
                            if temp_card.rank == 'Skip' or temp_card.rank == 'Reverse':
                                turn = 'Player'
                                top_card = player_hand.remove_card(pos)
                                print("\nYou played {temp_card}")
                                time.sleep(1)
                            elif temp_card.rank == 'Draw2':
                                for i in range(2):
                                    pc_hand.add_card(deck.deal())
                                top_card = player_hand.remove_card(pos)
                                print("\nYou played {temp_card}")
                                time.sleep(1)
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
                                time.sleep(1)
                                turn = 'Player'
                            elif temp_card.rank == 'Wild':
                                top_card = player_hand.remove_card(pos)
                                wildcolor = input('Enter which color you want to change to: ')
                                if wildcolor != wildcolor.upper():
                                    wildcolor = wildcolor.upper()
                                top_card.color = wildcolor
                                print("The color has been changed to " + f"{wildcolor}")
                                time.sleep(1)
                                turn = 'Pc'
                    else:
                        print('This card cannot be used')

                elif choice == 'd':
                    temp_card = deck.deal()
                    print('You got: ' + str(temp_card))
                    time.sleep(1)
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
                time.sleep(1)
                # If PC has a valid card to play in hand itll be played
                if temp_card != 'no card':
                    print('\n' + pc_name + f' throws: {temp_card}')
                    time.sleep(1)
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
                    time.sleep(1)
                    temp_card = deck.deal()
                    # If drawn card is valid AI will play it
                    if single_card_check(top_card, temp_card):
                        print('\n' + pc_name + f' throws: {temp_card}')
                        time.sleep(1)
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
                        time.sleep(1)
                        pc_hand.add_card(temp_card)
                        turn = 'Player'
                print('\n' + pc_name + ' has {} cards remaining'.format(pc_hand.no_of_cards()))
                time.sleep(1)
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
        playerVplayer()

    elif option == 3:
        break
    
    # If invalid input is given this error message is given and player will have to input a correct choice
    else:
        print(colored("Invalid choice, please choose a valid option: ", "black", "on_red"))
        print("")