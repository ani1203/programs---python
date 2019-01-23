import itertools
import random


class Deck:

    def cards(self):
        deck = list(itertools.product(["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                                      ["Clubs", "Diamonds", "Hearts", "Spades"]))
        for players in range(1, 5):
            random.shuffle(deck)
            print("")
            print("player", players, "got")
            for cards_ in range(1, 10):
                print("    ", deck[cards_][0], "of", deck[cards_][1])


if __name__ == '__main__':
    suit_rank = Deck()
    suit_rank.cards()
