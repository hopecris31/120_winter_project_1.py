


def create_card(rank, suit):
    """

    :param rank: (string)...
    :param suit: (string)...
    :return: (string)...
    """
    card = rank+suit
    return card

def identify_rank(card):
    """

    :param card:
    :return:
    """
    return card[0]

def identify_suit(card):
    """

    :param card:
    :return:
    """
    return card[1]


"""
modules:
1. poker_sim.py (runs the actual percentages/chart)
2. one that shuffles and deals cards
3. one that identifies the hands
4. 
"""



"""
1. create standard deck (var, list)
2. shuffle deck (def)
3. deal hand (def, return var, list) (keep making hands of 5 until another cannot be made)
4. identify hand category (def) (if hand category == type, add one to counter)
5. keep count of hand categories (def)
6. deal hands and sort until hands == 10,000 then stop
7. create table
8. output data into table
9. complete process again for 20k, then 30k, etc., up to 100k (in increments of 10k)


"""