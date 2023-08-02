from card import Card
import random

class Deck:

    def __init__(self):
        self.deck = []
        self.rank = ('0','1','2','3','4','5','6','7','8','9','Skip','Reverse','Draw2','Draw4','Wild')
        self.color= ('RED','GREEN','BLUE','YELLOW')

        # Creating deck
        for clr in self.color:
            for ran in self.rank:
                self.deck.append(Card(clr, ran))
                self.deck.append(Card(clr, ran))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    # Deals card from deck using pop so the card dealt is from top of deck
    def deal(self):
        return self.deck.pop()