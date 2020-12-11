from collections import namedtuple

SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
RANKS = tuple(range(2,11)) + tuple("JQKA")

Card = namedtuple("Card", "rank suit")

def card_deck_gen():

    for i in range(len(SUITS) * len(RANKS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        yield Card(rank, suit)



class CardDeckIterable:

    def __init__(self):
        pass
    
    def __iter__(self):
        return CardDeckIterable.card_deck_gen()


    def __reversed__(self):
        return CardDeckIterable.rev_card_deck_gen()

    @staticmethod
    def card_deck_gen():
        for suit in SUITS:
            for rank in RANKS:
                yield Card(rank, suit)


    @staticmethod
    def rev_card_deck_gen():
        for suit in reversed(SUITS):
            for rank in reversed(RANKS):
                yield Card(rank, suit)




if __name__ == "__main__":
    card_gen = card_deck_gen()
    for card in card_gen:
        print(card)

    print("="*30)
    for card in CardDeckIterable():
        print(card)
    print("*"*30)
    for card in reversed(CardDeckIterable()):
        print(card)





