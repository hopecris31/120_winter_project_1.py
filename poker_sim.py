#help from: CS Help desk, office hours
import deck as d
import hands as h
import cards as c

game_size = 100000
interval_size = 10000
flush_index = 0
pair_index =

def check_hand_type(hand):
    """

    :param hand:
    :return:
    """
    #keep counter wherever i am running the experiment


    if h.check_flush(hand):
        return 'Flush'
    elif h.check_two_pair(hand):
        return 'Two Pair'
    elif h.check_pair(hand):
        return 'Pair'
    else:
        return 'High Card'


def deal_round(num_rounds):
    rounds_played = []
    deck = d.create_deck()
        for i in range(num_rounds):
            if d.enough_in_deck(deck):
                rounds_played.append(check_hand_type(get_round(deck)))
            else:
                deck = d.create_deck()
                rounds_played.append(check_hand_type(get_round(deck)))







def hand_counter(hand):
    flush_counter = 0
    pair_counter = 0
    two_pair_counter = 0
    high_card_counter = 0

    if h.check_hand_type(hand) == 'Flush':
        flush_counter += 1
    elif h.check_hand_type(hand) == 'Pair':
        pair_counter += 1
    elif h.check_hand_type(hand) == 'Two Pair':
        two_pair_counter += 1
    else:
        high_card_counter += 1




def play_rounds():
    #create deck
    #shuffle
    #create hands
    #identify each card hand
    #add card

    pass
