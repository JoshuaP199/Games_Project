import collections

Card = collections.namedtuple('Card', ['suit', 'rank'])

class FrenchDeck: 
    ranks = [str(n) for n in range(2,11)] + list('JQKA') 
    #notice the list comprehension above
    suits = 'spades diamonds clubs hearts'.split() 
    #.split() splits on whitespaces
    
    def __init__(self):
        self._cards = [Card(suit,rank) for suit in self.suits
                                       for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    

def guess():
    print(" For Jack, Queen, King, Ace type J, Q, K, A")
    rank = input('What rank do you think the card is: ')
    print("\n\n")
    print('\n\nEnter either hearts, diamonds, clubs, spades')
    suit = input("Enter a suit: ").lower()
    print("\n\n")
    return Card(suit,rank)

def isGuessGood(mc, gc, l):
    if mc == gc:
        return 1
    elif l == 'easy':
        if mc.rank == gc.rank:
            return 3
        elif mc.suit == gc.suit:
            return 4
    else:
        return 2
    
def guessSuit():
    print('Enter either hearts, diamonds, clubs, spades')
    suit = input("Enter a suit: ").lower()
    return suit
    
def guessRank():
    print(" For Jack, Queen, King, Ace type J, Q, K, A")
    rank = input('What rank do you think the card is: ')
    return rank
    

def cardGuessingGame(level):
    mysteryCard = choice(deck)
    guessCard = guess()
    base(mysteryCard, level, guessCard)

def base(mysteryCard, l, guessCard):
    e = isGuessGood(mysteryCard, guessCard, l)
    if e == 1:
        print("You Won!")
        if input('Do you want to play again? (y)') == 'y':
            l = input('Do you want to play Easy (e) or Hard (h)')
            cardGuessingGame(l)
        else:
            print('Goodbye')
        
    elif e == 3:
        print("You guessed the rank correctly but not the suit")
        if input("Do you want to guess again? (y)") == 'y':
            r = guessCard.rank
            s = guessSuit()
            guessCard = Card(s,r)
            base(mysteryCard,l, guessCard)
            
        else:
            print("The correct answer was: ", mysteryCard.rank, " of ", mysteryCard.spade)
        
    elif e == 4: 
        print("You guessed the suit correctly but not the rank")
        if input("Do you want to guess again? (y)") == 'y':
            s = guessCard.suit
            r = guessRank()
            guessCard = Card(s,r)
            base(mysteryCard,l, guessCard)
        else:
            print("The correct answer was: ", mysteryCard.rank, " of ", mysteryCard.spade)
        
    else:
        print("You were incorrect.")
        if input("Do you want to guess again? (y)") == 'y':
            guessCard = guess()
            base(mysteryCard,l, guessCard)
        else:
            print("The correct answer was: ", mysteryCard.rank, " of ", mysteryCard.spade)
