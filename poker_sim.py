#help from: CS Help desk, office hours
#I affirm that I have carried out the attached academic endeavors with full academic honesty, in
#accordance with the Union College Honor Code and the course syllabus.

"""
Refactoring reflection:

I did a lot of refactoring in this project.  I often wrote functions a certain way,
and then as I was writing other code that would use those functions, I figured a better
way to rewrite them and make them more reusable, efficient, and understandable.  There were
a couple of times where I would write a function with multiple lines of code.  Then, I would go
back and remember a method or shorter way of producing the same output, and my code looked much neater and
easier to read after it.  It also made tracing through other functions a lot easier.
"""

import cards as c
import deck as d
import hands as h



total_iterations = 100000
first_iteration = 10000
flush_index = 0
pair2_index = 1
pair_index = 2
high_card_index = 3


def deal_round(num_rounds):
    """
    creates deck, makes hands
    :param num_rounds: number of rounds that will be played (100k)
    :return: the hands specified for the number of rounds
    """
    list_of_hands = []
    deck = d.shuffle(d.create_deck()) #creates and shuffles deck
    for i in range(num_rounds):
        if d.enough_in_deck(deck):#if there are enough cards in deck to make hand
            list_of_hands.append(check_hand_type(h.create_hand(deck)))#checks and adds the hand type to the list
        else:
            deck = d.shuffle(d.create_deck()) #if not enough cards for new deck, create new deck
            list_of_hands.append(check_hand_type(h.create_hand(deck))) #checks and adds hand type and adds to list
    return list_of_hands #list of all hand types from test hands




def check_hand_type(hand):
    """
    :param hand: a hand of 5 cards
    :return: the type of hand it is
    """

    if h.check_flush(hand):
        return 'Flush'
    elif h.check_two_pair(hand):
        return 'Two Pair'
    elif h.check_pair(hand):
        return 'Pair'
    else:
        return 'High Card'



def hand_counter(hands_list): #param:list__of_hands, got from deal_round
    """
    counts the occurrences of each hand from a round
    :param hands_list: a list of hands
    :return: list of the counts of all the hands
    """
    #hands_list = [flush, pair, twoPair, flush, highCard]

    flushes = hands_list.count('Flush')
    two_pairs = hands_list.count('Two Pair')
    pairs = hands_list.count('Pair')
    high_cards = hands_list.count('High Card')

    return [pairs, two_pairs, flushes, high_cards]



def find_percent(hand_counter_list, hand_counter_list_index, interval):
    """
    finds percent chance of a hand occurrence
    :param hand_counter_list: the list with the number of hand occurences
    :param hand_counter_list_index: the index of the hand count you want to access
    :param interval: number of hands to be tested
    :return: the percent of hand occurrences
    """
    percent = (hand_counter_list[hand_counter_list_index]/interval)*100
    return percent




def table_display(all_rounds):
    """

    :param all_rounds:
    :return:
    """
    header = '# of hands    pairs %    2 pairs %    flushes %    high card %'
    print(header)

    increment_size = 10000  #first interval
    create_round = deal_round(increment_size) #creates a deck and number of specified hands (10k)
    hand_counts = hand_counter(create_round) #counts the number of times each hand occurs

    for interval in range(increment_size):

        find_percent(hand_counts, 0, increment_size)
        percent_pairs = find_percent(hand_counts, 0, increment_size)
        percent_two_pairs = find_percent(hand_counts, 1, increment_size)
        percent_flushes = find_percent(hand_counts, 2, increment_size)
        percent_high_cards = find_percent(hand_counts, 3, increment_size)
        print(percent_pairs, percent_two_pairs, percent_flushes, percent_high_cards)
        increment_size += increment_size #double it for next round




    #for hands in create_round:





    #for interval in range(increment_size):








    #for interval in range(first_iteration, total_iterations +1, increment_size): #creates testing in increments of 10k, up to 100k
        #print(interval)
        #next_iteration = hand_counter(all_rounds[interval - increment_size: interval])
        ##next_interval = check_hand_type(all_rounds[interval - increment_size: interval])
        #for new_interval in range(len(won_by_total)):
            ##won_by_total[new_interval] = hand_counter(next_interval)
            #print(won_by_total[new_interval])+= next_interval[new_interval]

            #print(header)
            #print(interval, won_by_total[pair_index], find_percent(won_by_total, pair2_index, interval))
            #print(.format(interval, won_by_total[pair_index], find_percent(won_by_total, pair2_index, interval),
                    #won_by_total[pair2_index], find_percent(won_by_total, pair2_index, interval),
                    #won_by_total[flush_index], find_percent(won_by_total, pair2_index, interval),
                    #won_by_total[high_card_index], find_percent(won_by_total, pair2_index, interval)))


#'{:>10,}  {:>7.2f}{:>11}  {:05.2f}{:>11}  {:05.2f}{:>13}{:>7.2f}'

            #for interval in range(first_sample, sample_size + 1, interval_size):


"""
#'{:>10,}{:>10,}{:>7.2f}{:>11}  {:05.2f}{:>11}  {:05.2f}{:>13}{:>7.2f}'

def table_display2(all_rounds):
    header = '# of hands    pairs %    2 pairs %    flushes %    high card %'
    percent = find_percent((hand_counter(deal_round(interval)))
    for interval in range(first_sample, sample_size + 1,interval_size):  # creates testing in increments of 10k, up to 100k
        print()
        row = [interval, find_percent((hand_counter(deal_round(interval))), 3, 10000), find_percent(won_by_total, pair2_index]

    print('won_by_total: ', won_by_total, 'new_interval: ', new_interval, 'next interval: ', next_interval,
          range(len(won_by_total)))
    #for interval in range(first_sample, sample_size + 1, interval_size):
    print('interval: ', interval, 'range(first_sample, sample_size +1, interval_size): ',
          range(first_sample, sample_size + 1, interval_size))
    print('next interval: ', next_interval)
    
"""



def play_rounds():
    """
    starts the entire program
    :return:
    """
    #return table_display(deal_round(increment_size))

#print(play_rounds())

#if __name__  == "__main__":
#    play_rounds()