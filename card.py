class Card:

    def __init__(self, color, rank):
        self.rank = rank
        # Assigning types to all card values there can be
        self.ctype = {
            '0':'number','1':'number','2':'number','3':'number','4':'number','5':'number','6':'number',
            '7':'number','8':'number','9':'number','Skip':'action','Reverse':'action','Draw2':'action',
            'Draw4':'action_nocolor','Wild':'action_nocolor'
        }

        # If card is a number or action type let it have a color value
        if self.ctype[rank] == 'number':
            self.color = color
            self.cardtype = 'number'
        elif self.ctype[rank] == 'action':
            self.color = color
            self.cardtype = 'action'
        # If card is a wild card don't assign a color value to it
        else:
            self.color = None
            self.cardtype = 'action_nocolor'

    def __str__(self):
        if self.color == None:
            return self.rank
        else:
            return self.color + " " + self.rank