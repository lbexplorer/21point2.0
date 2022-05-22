from unittest import TestCase

from game.card import generate_init_card_list, drawcard


class Test(TestCase):
    def test_generate_init_card_list(self):
        card_list = generate_init_card_list()
        print("初始的牌组是", card_list)
        print("牌的数目是", len(card_list))
        self.assertEqual(len(card_list), 52)

    def test_drawcard(self):
        card_list = generate_init_card_list()
        print("初始的牌组是", card_list)
        print("牌的数目是", len(card_list))
        print("尝试抽一张牌")

        old_card_number = len(card_list)
        new_cardlist, card = drawcard(card_list)
        new_card_number = len(new_cardlist)
        self.assertEqual(old_card_number - 1, new_card_number)
        self.assertTrue(card != None)
        self.assertNotEqual(card, None)
        self.assertTrue(type(card) == int)
        self.assertEqual(type(card), int)
        self.assertGreater(card, 0)
        self.assertTrue(card > 0)

        print("牌的数目是", len(card_list))
        print("尝试再抽一张牌")

        old_card_number = len(card_list)
        new_cardlist, card = drawcard(card_list)
        new_card_number = len(new_cardlist)
        self.assertEqual(old_card_number - 1, new_card_number)
        self.assertTrue(card != None)
        self.assertNotEqual(card, None)
        self.assertTrue(type(card) == int)
        self.assertEqual(type(card), int)
        self.assertGreater(card, 0)
        self.assertTrue(card > 0)
