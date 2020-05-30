import random


class Card:

    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

        if self.val == 1:
            self.val = 'Ace'
        if self.val == 11:
            self.val = 'Jack'
        if self.val == 12:
            self.val = 'Queen'
        if self.val == 13:
            self.val = 'King'
        else:
            self.val = str(self.val)

    def __repr__(self):
        return f'{self.val} of {self.suit}'

    def __str__(self):
        return f'{self.val} of {self.suit}'


class Deck:

    def __init__(self):

        self.cards = []
        for suit in ['Spades', 'Hearts', 'Dice', 'Clubs']:
            for val in range(1, 14):
                self.cards.append(Card(val, suit))

        self.pile = []

    def shuffle(self):
        for i in range(51, 0, -1):
            randi = random.randint(0, i)
            self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)

    def show_pile(self):
        print(self.pile)


class Player:

    def __init__(self, name):
        self.name = name
        print(f'{self.name} has joined the game!')
        self.hand = []

    def draw(self, deck, num=1):
        for i in range(num):
            self.hand.append(deck.cards.pop())
        print(f"{self.name} drew {num} cards")

    def show(self):
        print(f"{self.name}'s hand is {self.hand}")

    def discard(self, index, deck):
        c = self.hand.pop(index)
        deck.pile.append(c)
        print(f"{self.name} discarded {c}")

    def draw_pile(self, deck):
        c = deck.pile.pop()
        self.hand.append(c)
        print(f"{self.name} drew {c} from the pile")


myDeck = Deck()
print(myDeck)
myDeck.shuffle()
print(myDeck)
bob = Player('Bob')
alice = Player('Alice')
bob.draw(myDeck, 7)
bob.show()
alice.draw(myDeck, 7)
alice.show()
bob.discard(4, myDeck)
bob.show()
alice.draw_pile(myDeck)
alice.show()







