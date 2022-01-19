
import cards
import deck as d



def get_ranks(hand):
    hand_ranks = []

    for card in hand:
        rank = cards.identify_rank(card)
        hand_ranks.append(rank)

    return hand_ranks



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
        dealt_cards.append(deck.pop(0)) #remove dealt cards and add to list

    return dealt_cards



print(create_hands(d.shuffle(d.create_deck())))
print(create_hand(d.shuffle(d.create_deck())))




def check_flush(hand):
    first_suit = cards.identify_suit(hand[len-1])
    for card in hand:
        if first_suit != cards.identify_suit(card):
            return False
    return True


def check_pair(hand):
    """
    checks hand, iterates one pair at a time and tries all card combinations for pairs.
    if pair is found, returns True.
    :param hand: hand of 5 cards (list)
    :return: True when a pair or three of a kind is detected
    """
    ranks = get_ranks(hand)

    for card in range(len(ranks)):
        for card_compare in range(card + 1,(len(ranks))):
            if ranks[card] == ranks[card_compare]:
                return True
    return False





pHand = ['6C', '6H', '6D', '6H', '5S']

def check_two_pair(hand):
    """
    iterates through hand, creates dict and stores values for number of rank appearances.
    :param hand: a list of 5 cards
    :return: True if there is a two pair, four of a kind, or full house

    """
    if check_pair(hand) == True:

        pairs = 0
        ranks = get_ranks(hand)
        for card in range(len(ranks)):
            for card_compare in range(len(ranks) - card - 1):
                if ranks[card] == ranks[card + card_compare + 1]:
                    pairs += 1
                    ranks[card] = 'none'
                    ranks[card + card_compare +1] = 'none1'
                    if pairs == 2:
                        return True
    return False

        #check if regular pair first, then if that returns False then check the rest of these tests
#returns true when it is a regular pair. need help w that

print(check_two_pair(pHand))
print(check_pair(pHand))



#print(deck.create_deck())
# print(create_hands2(shuffle_deck()))
#print(create_hands(deck.create_deck()))
#print(check_flush(flush))
#print(check_two_pair(pHand))
#print(check_pair(pairHand))
#print(check_high_card(pairHand))
