import random





def shuffle_deck():
        """
        shuffles a deck of cards
        :param deck: a deck (list) of 52 cards,
        :return: the deck (list) in random order
        """
        deck = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',
                '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH',
                '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',
                '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS']
        random.shuffle(deck)
        return deck

def create_hands(deck):
        """
        created the maximum number of poker hands possible (10) from a shuffled
        deck (list) of cards. Removes remainder 2 cards
        :param deck: a shuffled deck of cards
        :return: returns 10 hands from a shuffled deck as a list of smaller lists
        """
        hands_list = []
        del deck[0:2]

        #try writing this with a loop

        hand1 = deck[0:5]
        hands_list.append(hand1)

        hand2 = deck[5:10]
        hands_list.append(hand2)

        hand3 = deck[10:15]
        hands_list.append(hand3)

        length = len(deck)
        ten_hands = length // 5



        return deck



def check_flush(hand):
        pass

def check_two_pair(hand):
        pass

def check_high_card(hand):
        pass

print(shuffle_deck())
print(create_hands(shuffle_deck()))