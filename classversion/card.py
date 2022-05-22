class Card:
    def __init__(self, ponit, pattern):
        self.pattern = pattern
        self.point = ponit

    def get_card_name(self):
        return self.pattern + str(self.point)

    def get_pattern(self):
        return self.pattern

    def get_color(self):
        if self.pattern == "红桃":
            return "red"
        if self.pattern == "方片":
            return "red"
        if self.pattern == "梅花":
            return "black"
        if self.pattern == "黑桃":
            return "black"

    def compare_ponit(self, point):
        # 如果目前的点数比给定的点数大，返回1
        if self.point > point:
            return 1
        # 如果目前的点数比给定的点数大，返回1
        if self.point == point:
            return 0
        if self.point < point:
            return -1

    def compare_card(self, card):
        # 如果目前的点数比给定的的card对象的点数大，返回1
        if self.point > card.point:
            return 1
        # 如果目前的点数比给定的点数大，返回1
        if self.point == card.point:
            return 0
        if self.point < card.point:
            return -1

    def get_actual_ponit(self):
        # 返回目前牌的实际点数
        if self.point >= 10:
            return 10
        return self.point

    def get_ponit(self):
        # 返回目前牌的点数
        return self.point


if __name__ == "__main__":
    card1 = Card(10, "方片")
    card2 = Card(12, "方片")
    card3 = Card(1, "黑桃")
    print("card1是", card1.get_card_name())
    print("card1的点数", card1.get_ponit(), "颜色", card1.get_color(), "花色", card1.pattern, " 实际点数",
          card1.get_actual_ponit())

    print("card2是", card2.get_card_name())
    print("card2的点数", card2.get_ponit(), "颜色", card2.get_color(), "花色", card2.pattern, " 实际点数",
          card2.get_actual_ponit())

    print("card3是", card3.get_card_name())
    print("card3的点数", card3.get_ponit(), "颜色", card3.get_color(), "花色", card3.pattern, " 实际点数",
          card3.get_actual_ponit())

    print("card1和card2的点数比较", card1.compare_card(card2))
    print("card1和card3的点数比较", card1.compare_card(card3))
    # CRTL+ALT+L 快捷键，让你的代码自动变得整齐

    # 类可以被添加到列表里面，并且可以被for循环使用
    card_list=[]
    for i in range(1,14):
        new_card = Card(i,"红桃")
        card_list.append(new_card)
    for i in range(1, 14):
        new_card = Card(i, "黑桃")
        card_list.append(new_card)

    for t in card_list:
        print("目前卡牌是", t.get_card_name())
        print("点数", t.get_ponit(), "颜色", t.get_color(), "花色", t.pattern, " 实际点数",
          t.get_actual_ponit())

    # 另外一种创建牌堆的方式
    card_list = []
    for p in ["红桃","黑桃","梅花","方片"]:
        for i in range(1, 14):
            new_card = Card(i, p)
            card_list.append(new_card)

    for t in card_list:
        print("目前卡牌是", t.get_card_name())
        print("点数", t.get_ponit(), "颜色", t.get_color(), "花色", t.pattern, " 实际点数",
              t.get_actual_ponit())
