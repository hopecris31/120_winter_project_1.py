import cards
import deck

def create_hands(deck):
    """

    :param deck:
    :return:
    """
    start = 0
    end = 5
    del deck[0:2]
    dealt_hands = []

    for cards in deck[:10]:
        hand = deck[start:end]
        dealt_hands.append(hand)
        start += 5
        end += 5

    return dealt_hands


def create_hand(deck):
    """

    :param deck:
    :return:
    """

    dealt_cards = []

    for index in range(0,5):
        dealt_cards.append(deck[index]) #dealing individual cards

    return dealt_cards

"""
flush =
#flush, straight flush, royal flush
two_pair =
#two pair, four of a kind, full house
pair =
#pair, three of a kind
high_card =
#high card, straight
"""

flush = []
two_pair = []
pair = []
high_card = []

def check_flush(hand):
    first_suit = cards.identify_suit(hand[0])
    for card in hand:
        if first_suit != cards.identify_suit(card):
            return False
    return True




def check_two_pair(hand):
    pass

def check_pair(hand):
    pass

def check_high_card(hand):
    pass


print(deck.create_deck())
# print(create_hands2(shuffle_deck()))
print(create_hands(deck.create_deck()))
print(check_flush(deck.create_deck()))