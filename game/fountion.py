from game.blackjack import explosion_rate
from game.card import send_start_hand_card
from game.show_information import show_state


def game_result(bet_human, bet_robot, player_card, result, robot_card):
    if result == 1:
        print("机器人的牌是：", robot_card, "总和是：", sum(robot_card))
        print("你的牌是：", player_card, "总和为：", sum(player_card), "\n恭喜，你赢了")
    elif result == 0:
        print("机器人的牌是：", robot_card, "总和是：", sum(robot_card))
        print("你的牌是：", player_card, "总和为：", sum(player_card), "\n抱歉，你输了")

    else:
        print("机器人的牌是：", robot_card, "总和是：", sum(robot_card))
        print("你的牌是：", player_card, "总和为：", sum(player_card), "\n平局")
    print("电脑剩余的筹码：", bet_robot)
    print("玩家剩余的筹码", bet_human)


def game_initialization(cardlist, player_card, robot_card):
    cardlist = send_start_hand_card(cardlist, robot_card)
    cardlist = send_start_hand_card(cardlist, player_card)
    point = sum(robot_card)
    rate_robot = explosion_rate(point, cardlist)
    point = sum(player_card)
    rate_player = explosion_rate(point, cardlist)
    show_state(robot_card, rate_robot, "robot")
    show_state(player_card, rate_player, "player")
    return cardlist