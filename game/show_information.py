def show_state(handcards, rate, player_type):
    if player_type=="robot":
        show_robot_state(handcards,rate)
    if player_type=="player":
        show_player_state(handcards,rate)


def show_robot_state(robot_card, rate_robot):
    print("此时电脑的牌:", robot_card)
    print("电脑爆率为", rate_robot, "%")


def show_player_state(player_card, rate_player):
    print("玩家的牌：", player_card)
    print("玩家爆率为", rate_player, "%")