
import random
import cards

hand_size = 5

def create_deck():
    """
    creates a deck of cards by combining one of each rank and suit
    :return: deck of 52 cards as list
    """
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    suits = ['H', 'D', 'C', 'S']
    for i in range(len(ranks)):
        for j in range(len(suits)):
            card = cards.create_card(ranks[i], suits[j])
            deck.append(card)
    return deck

#print(create_deck())

def shuffle(deck):
    """
    shuffles a deck of cards
    :return: the shuffled deck of cards as a list
    """

    random.shuffle(deck)
    return deck


def enough_in_deck(deck):
    """
    checks if there are enough cards in the deck to make another hand
    :param deck: a list of cards
    :return: True or False, depending of if there are enough cards
    """
    if len(deck) >= hand_size:
        enough = True
    else:
        enough = False
    return enough