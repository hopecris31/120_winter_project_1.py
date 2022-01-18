
import cards
import deck

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




def create_hands(deck):
    """

    :param deck:
    :return:
    """
    start = 0
    end = 5
    del deck[0:2]
    #ask what to do about the remaining 2 cards in deck, delete or not
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




flush = ['AS', 'QS', '4S', '3S', '5S'] #test variable

def check_flush(hand):
    first_suit = cards.identify_suit(hand[0])
    for card in hand:
        if first_suit != cards.identify_suit(card):
            return False
    return True




pHand = ['KC', 'KD', 'KD', '4H', '2S']

def check_two_pair(hand):
    """
    iterates through hand, creates dict and stores values for number of rank appearances.
    :param hand: a list of 5 cards
    :return: True if there is a two pair, four of a kind, or full house
    """
    pairs = {}

    for card in hand:
        if card[0] not in pairs:
            pairs[card[0]] = 0
        pairs[card[0]] += 1
        print(pairs)
    for cardCount in pairs.values():
        if cardCount >= 2:
            print(pairs)
            return True
        else:
            return False
#returns true when it is a regular pair. need help w that

print(check_two_pair(pHand))




pairHand = ['4H', '2D', '4D', '2S', '3S'] #test variable

def check_pair(hand):
    """
    checks hand, iterates one pair at a time and tries all card combinations for pairs.
    if pair is found, returns True.
    :param hand: hand of 5 cards (list)
    :return: True when a pair or three of a kind is detected
    """

    for i in range(5):
        for j in range(i + 1, 5):
            #print(cards.identify_rank(hand[i]), cards.identify_rank(hand[j]))
            if cards.identify_rank(hand[i]) != cards.identify_rank(hand[j]):
                j += 1
##need to fix this to return false if there are no pairs, but return true works properly
            else:
                return True

print(check_pair(pairHand))


def check_high_card(hand):
    """
    :param hand: hand of 5 cards (list)
    :return:
    """
    for card in hand:
        highestRank = 



#print(deck.create_deck())
# print(create_hands2(shuffle_deck()))
#print(create_hands(deck.create_deck()))
#print(check_flush(flush))
#print(check_two_pair(pHand))
#print(check_pair(pairHand))
#print(check_high_card(pairHand))