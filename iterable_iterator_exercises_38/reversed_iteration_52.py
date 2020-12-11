from collections import namedtuple

_SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
_RANKS = tuple(range(2, 11)) + tuple("JQKA")

Card = namedtuple("Card", "rank suit")

class CardDeck(object):

    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)


    def __iter__(self):
        print("CardDeck __iter__ called")
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)

    #def __len__(self):
    #    return self.length

    class CardDeckIterator(object):

        def __init__(self, length, reverse = False):
            self.i = 0
            self.length = length
            self.reverse = reverse


        def __iter__(self):
            print("CardDeckIterator __iter__ called")
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration

            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)



if __name__ == "__main__":
    deck = reversed(CardDeck())

    for card in deck:
        print(card)
    
    print("="*25)
    deck = CardDeck()
    for card in deck:
        print(card)
