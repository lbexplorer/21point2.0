# 这个文件改名成为blackjack.py，因为21ponit.py是非法的（不能有中文和数字），非法会导致21ponit.py中的类和方法无法在其他的文件里面通过
# from XXX import XXX （比如from random import choice）的方式使用，也没法写对应的单元测试


def victory_defeat(card_list) :
    result = sum(card_list )
    return result



def than_big(robot_result,player_result):
    if (robot_result > 21) and (player_result < 21 ) :
        return 1
    elif (player_result > 21) and (robot_result<21):
        return 0
    elif (robot_result > 21) and (robot_result>21 ):
        return 2
    else :
        if robot_result > player_result :
            return 0
        elif robot_result < player_result :
            return 1
        else:
            return 2

def explosion_rate(point,cardlist):
    point =21-point
    if point > 10 :
        rate = 0
    elif point < 0 :
        rate = 100
    else :
        count = 0
        number = 0
        for each in cardlist :
            number = number + 1

            if each > point :
                count = count + 1
        rate = ((count * 1.0) / number)*100
    return rate

def count_bet(bet_robot,bet_player,result):
    if result == 1:
        bet_player = bet_player + 500
        bet_robot = bet_robot - 500
    elif result == 2:
        bet_player = bet_player - 500
        bet_robot = bet_robot + 500
    else :
        bet_player = bet_player - 250
        bet_robot = bet_robot - 250
    return bet_robot ,bet_player








