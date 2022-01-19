#help from: CS Help desk, office hours
import deck as d
import hands as h
import cards as c


sample_size = 100000
interval_size = 10000
first_sample = 10000
flush_index = 0
pair2_index = 1
pair_index = 2
high_card_index = 3
show_percent = 100

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

print(check_hand_type(['AS', 'KS', 'QS', 'JS', '10S']))




def deal_round(num_rounds):
    """
    creates deck, makes hands until
    :param num_rounds: number of rounds that will be played (100k)
    :return:
    """
    rounds_played = []
    deck = d.shuffle(d.create_deck()) #creates and shuffles deck
    for i in range(num_rounds):
        if d.enough_in_deck(deck):
            rounds_played.append(check_hand_type(h.create_hand(deck)))#adds the hand type to the list
        else:
            deck = d.shuffle(d.create_deck()) #if not enough cards for new deck, create new deck
            rounds_played.append(check_hand_type(h.create_hand(deck))) #checks hand type and adds to list
    return print(rounds_played)

print(deal_round(10))


def hand_counter(hand):
    flush_counter = 0
    pair_counter = 0
    two_pair_counter = 0
    high_card_counter = 0

    for card in range(len(hand)):
        if check_hand_type(hand) == 'Flush':
            flush_counter += 1
        elif check_hand_type(hand) == 'Pair':
            pair_counter += 1
        elif check_hand_type(hand) == 'Two Pair':
            two_pair_counter += 1
        else:
            high_card_counter += 1

    won_by = [flush_counter, pair_counter, two_pair_counter, high_card_counter]
    return won_by


def display_percent(won_by_total, index, interval):
    """
    % of total hands won by a given condition
    :param won_by_total: list with totals of each hand
    :param index: index of the win hand you want
    :param interval: total number of hands to iterate through
    :return: percent of each hand
    """
    return show_percent*(won_by_total[index]/interval) #calc %


def table_display(all_rounds):
    """

    :param all_rounds:
    :return:
    """
    header = '# of hands pairs % 2 pairs % flushes % high card %'
    print(header)
    won_by_total = [0, 0, 0, 0]

    for interval in range(first_sample, sample_size +1, interval_size):
        #print('interval: ',interval, 'range(first_sample, sample_size +1, interval_size): ', range(first_sample, sample_size +1, interval_size))
        next_interval = check_hand_type(all_rounds[interval - interval_size: interval])
        #print('next interval: ', next_interval)
        for new_interval in range(len(won_by_total)):
            #print('won_by_total: ', won_by_total, 'new_interval: ', new_interval, 'next interval: ', next_interval, range(len(won_by_total)))
            won_by_total[new_interval] += next_interval[new_interval]



            print('{:>10,}{:>10,}{:>7.2f}{:>11}  {:05.2f}{:>11}  {:05.2f}{:>13}{:>7.2f}'
                  .format(interval, won_by_total[pair_index], display_percent(won_by_total, pair2_index, interval),
                    won_by_total[pair2_index], display_percent(won_by_total, pair2_index, interval),
                    won_by_total[flush_index], display_percent(won_by_total, pair2_index, interval),
                    won_by_total[high_card_index], display_percent(won_by_total, pair2_index, interval)))


def play_rounds():
    """

    :return:
    """
    return table_display(deal_round(sample_size))

print(play_rounds())

#if __name__  == "__main__":
#    play_rounds()