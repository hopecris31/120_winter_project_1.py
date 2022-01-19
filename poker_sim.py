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




def table_display(iteration_total, iteration_limit):
    """
    creates a table for the percent chances of all hands
    :return: a table with
    """
    pass
header = '# of hands    pairs   %         2 pairs   %         flushes   %         high card   %'
print(header)

increment_size = 10000
iteration_total = 10000
iteration_limit = 100000
#first interval
     #counts the number of times each hand occurs

for interval in range(increment_size):
    create_round = deal_round(increment_size)  # creates a deck and number of specified hands (10k)
    hand_counts = hand_counter(create_round)
    find_percent(hand_counts, 0, increment_size)

    num_pairs = hand_counts[0]
    percent_pairs = find_percent(hand_counts, 0, increment_size)

    num_two_pairs = hand_counts[1]
    percent_two_pairs = find_percent(hand_counts, 1, increment_size)

    num_flushes = hand_counts[2]
    percent_flushes = find_percent(hand_counts, 2, increment_size)

    num_high_cards = hand_counts[3]
    percent_high_cards = find_percent(hand_counts, 3, increment_size)


    print("{:,}".format(iteration_total), '    ', "{:,}".format(num_pairs),' ', "{:.2f}".format(percent_pairs), '       '
          "{:,}".format(num_two_pairs),'   ', "{:.2f}".format(percent_two_pairs), '        '
          "{:,}".format(num_flushes),'   ', "{:.2f}".format(percent_flushes),'     ',
          "{:,}".format(num_pairs), '     ', "{:.2f}".format(percent_high_cards))
    iteration_total += 10000 #add 10k to it for next round
    if iteration_total >= iteration_limit +1:
        break




def play_rounds():
    """
    starts the entire program
    :return:
    """
    return table_display()


#if __name__  == "__main__":
#    play_rounds()