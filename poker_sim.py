#help from: CS Help desk, office hours
import deck as d
import hands as h
import cards as c

game_size = 100000
interval_size = 10000
flush_index = 0
pair2_index = 1
pair_index = 2
high_card_index = 3
show_percent = 100

def check_hand_type(hand):
    """

    :param hand:
    :return:
    """

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
                rounds_played.append(check_hand_type(h.create_hand(deck)))
            else:
                deck = d.create_deck()
                rounds_played.append(check_hand_type(h.create_hand(deck)))




def hand_counter(hand):
    flush_counter = 0
    pair_counter = 0
    two_pair_counter = 0
    high_card_counter = 0

    for card in range(len(all_rounds)):
        if h.check_hand_type(hand) == 'Flush':
            flush_counter += 1
        elif h.check_hand_type(hand) == 'Pair':
            pair_counter += 1
        elif h.check_hand_type(hand) == 'Two Pair':
            two_pair_counter += 1
        else:
            high_card_counter += 1

    won_by = [flush_counter, pair_counter, two_pair_counter, high_card_counter]
    return won_by




def play_rounds():
    #create deck
    #shuffle
    #create hands
    #identify each card hand
    #add card

    pass
