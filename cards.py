
def create_card(rank, suit):
    """
    takes the rank and suit of a card (string) and concatenates them to form a card
    :param rank: a letter or number (string)
    :param suit: a letter
    :return: card (string)
    """
    card = rank+suit
    return card

def identify_rank(card):
    """
    :param card: a card (string) with a rank and suit
    :return: rank
    """
    return card[0]

def identify_suit(card):
    """
    :param card: a card (string) with a rank and suit
    :return: suit
    """
    return card[1]
