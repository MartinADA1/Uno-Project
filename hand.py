from termcolor import colored

class Hand:

    def __init__(self):
        self.cards = []
        self.cardsstr = []
        self.number_cards = 0
        self.action_cards = 0

    # Adds card to a players hand
    def add_card(self, card):
        self.cards.append(card)
        self.cardsstr.append(str(card))
        if card.cardtype == 'number':
            self.number_cards += 1
        else:
            self.action_cards += 1

    # Used to remove card that is played
    def remove_card(self, place):
        self.cardsstr.pop(place - 1)
        return self.cards.pop(place - 1)

    # Displays cards in hand to players
    def cards_in_hand(self):
        for i in range(len(self.cardsstr)):
            text_color = self.cards[i].color
            if text_color == None:
                text_color = "white"
            else:
                text_color = text_color.lower()
            print(colored("[" + str(i+1) + "]. " + self.cardsstr[i], text_color))

    # Used to hold cards temporarily to process them after being played
    def single_card(self, place):
        return self.cards[place - 1]

    def no_of_cards(self):
        return len(self.cards)