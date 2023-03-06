import random


class Card:
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit, rank):
        if suit not in Card.SUITS:
            raise ValueError(f"Not a valid suit, needs to be one of: {Card.SUITS}")
        rank = str(rank)
        if rank not in Card.RANKS:
            raise ValueError(f"Not a valid rank, needs to be one of: {Card.RANKS}")
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._cards.append(Card(suit, rank))

    def __str__(self):
        return str(self._cards)

    def __len__(self):
        return len(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()


class PokerHand:
    def __init__(self, deck: Deck):
        self._cards = []
        for _ in range(5):
            self._cards.append(deck.deal())

    def __str__(self):
        return str(self._cards)

    def is_flush(self):
        suit0 = self._cards[0]._suit
        for card in self._cards[1:]:
            if card._suit != suit0:
                return False
        return True

    def _is_n_of_a_kind(self, n):
        ranks = [card._rank for card in self._cards]
        for rank in ranks:
            if ranks.count(rank) == n:
                return True
        return False

    def is_pair(self):
        return self._is_n_of_a_kind(2)

    def is_3_of_a_kind(self):
        return self._is_n_of_a_kind(3)

    def is_4_of_a_kind(self):
        return self._is_n_of_a_kind(4)

    def is_2_pair(self):
        ranks = [card._rank for card in self._cards]
        ranks = set(ranks)
        if len(ranks) == 3 and not self.is_3_of_a_kind():
            return True
        return False

    def is_fullhouse(self):
        return self.is_pair() and self.is_3_of_a_kind()

c = 0
while True:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_fullhouse():
        break
    c += 1
print(hand)
print(f"it took {c} tries")




