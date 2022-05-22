import random
from random import choice


def drawcard(cardlist):
    card = choice(cardlist)
    cardlist.remove(card)
    if card >= 10:
        card = 10
    return cardlist, card


def shuffle_cardlist(card_list):
    random.shuffle(card_list)
    return card_list


def generate_init_card_list():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ]


def send_start_hand_card(cardlist, robot_card):
    for i in range(1, 3):
        cardlist = shuffle_cardlist(cardlist)
        cardlist, drawed_card = drawcard(cardlist)
        robot_card.append(drawed_card)
    return cardlist