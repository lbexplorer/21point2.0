# 从game目录底下的blackjack.py 文件导入其中写好的各种方法
from game.blackjack import explosion_rate, victory_defeat, than_big, count_bet
from game.card import drawcard, shuffle_cardlist, generate_init_card_list
from game.file_data_storage import file_data, file_r
from game.fountion import game_result, game_initialization


def main():
    # 载入数据，上局的筹码

    game_contiue = input("继续游戏 or 重新开始:")
    if game_contiue == "继续游戏":
        human_play, robot_play = file_r()
        bet_robot = robot_play["bet"]
        bet_human = human_play["bet"]
        print("游戏开始！")
        print("双方初始筹码为", "电脑：", bet_robot, "玩家：", bet_human)

        cardlist = generate_init_card_list()
        robot_card = []
        player_card = []

        cardlist = game_initialization(cardlist, player_card, robot_card)


    elif game_contiue == "重新开始":
        bet_robot = 1000
        bet_human = 1000
        print("游戏开始！")
        print("双方初始筹码为", "电脑：", bet_robot, "玩家：", bet_human)

        cardlist = generate_init_card_list()
        robot_card = []
        player_card = []

        cardlist = game_initialization(cardlist, player_card, robot_card)

    while True:
        player_lead = input("yes or no: ")
        answer = ["yes", "no"]
        if player_lead not in answer:
            player_lead = input("请输入yes或者no:")
            continue
        if player_lead == "yes":
            cardlist = shuffle_cardlist(cardlist)
            cardlist, drawed_card = drawcard(cardlist)
            player_card.append(drawed_card)

            point = sum(player_card)
            rate_player = explosion_rate(point, cardlist)

            print("drawed_card: ", drawed_card)
            print("此时人的牌：", player_card)
            print("玩家爆率为", rate_player, "%")

            cardlist = shuffle_cardlist(cardlist)
            cardlist, drawed_card = drawcard(cardlist)
            robot_card.append(drawed_card)

            point = sum(robot_card)
            rate_robot = explosion_rate(point, cardlist)

            print("drawed_card: ", drawed_card)
            print("此时机器的牌：", robot_card)
            print("电脑爆率为", rate_robot, "%")
            continue
        else:
            break

    player_result = victory_defeat(player_card)
    robot_result = victory_defeat(robot_card)

    result = than_big(robot_result, player_result)
    # 计算筹码
    bet_robot, bet_human = count_bet(bet_robot, bet_human, result)
    # 判断输赢
    game_result(bet_human, bet_robot, player_card, result, robot_card)

    # 保存数据，筹码的数据，以及玩的次数
    count_game = 1
    data_robot = {}
    data_human = {}
    # 使用字典存储
    data_robot["times"] = count_game
    data_robot["bet"] = bet_robot

    data_human["times"] = count_game
    data_human["bet"] = bet_human

    file_data(data_robot, data_human)


if __name__ == "__main__":
    # 开始游戏
    main()
