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
    #ask what to do about the remaining 2 cards in deck
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

flush = ['AS', 'QS', '4S', '3S', '5S']

def check_flush(hand):
    first_suit = cards.identify_suit(hand[0])
    for card in hand:
        if first_suit != cards.identify_suit(card):
            return False
    return True



"""
def check_two_pair(hand):
    first_rank = cards.identify_rank(hand[0])
    for card in hand:
        index = 1
        if first_rank == cards.identify_rank(card[index]):
            index += 1
            if cards.identify_rank(card[index]) == cards.identify_rank(card[index + 1]):
                return True
"""


pHand = ['5C', '3D', '5D', '5H', '3H']

def check_two_pair(hand):
    """

    :param hand: a list of 5 cards
    :return: True if there is a two pair, four of a kind, or full house
    """

    pairs = {}

    for card in hand:
        if card[0] not in pairs:
            pairs[card[0]] = 0
        pairs[card[0]] += 1

    print(pairs)


print(check_two_pair(pHand))

"""
def check_two_pair(hand):
    

    :param hand: a list of 5 cards
    :return: True if there is a two pair, four of a kind, or full house
    
    first_rank = cards.identify_rank(hand[0])
    for card in hand:
        index = 1
        if first_rank != cards.identify_rank(card[index]):
            index += 1
        return True
    #returns true all the time
    return False
"""


pairHand = ['AH', '2D', '4D', '5S', '3S'] #test variable

def check_pair(hand):

    """
    checks hand, iterates one pair at a time and tries all card combinations.
    if pair is found, returns True.
    :param hand: hand of 5 cards (list)
    :return: True when a pair is detected
    """

    for i in range(5):
        for j in range(i + 1, 5):
            #print(cards.identify_rank(hand[i]), cards.identify_rank(hand[j]))
            if cards.identify_rank(hand[i]) != cards.identify_rank(hand[j]):
                j += 1
##need to fix this to return false if there are no pairs, but return true works properly
            else:
                return True




def check_high_card(hand):
    """

    :param hand: hand of 5 cards (list)
    :return:
    """
    hand = hand.sort()
    return hand


#print(deck.create_deck())
# print(create_hands2(shuffle_deck()))
#print(create_hands(deck.create_deck()))
#print(check_flush(flush))
#print(check_two_pair(pHand))
#print(check_pair(pairHand))
#print(check_high_card(pairHand))