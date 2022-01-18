
import random
import cards

def create_deck():
    """
    creates a deck of cards by combining one of each rank and suit
    :return: deck of 52 cards as list
    """
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    for i in range(len(ranks)):
        for j in range(len(suits)):
            card = cards.create_card(ranks[i], suits[j])
            deck.append(card)
    return deck



def shuffle(deck):
    """
    shuffles a deck of cards
    :return: the shuffled deck of cards as a list
    """

    random.shuffle(deck)
    return deck


