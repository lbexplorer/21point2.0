from unittest import TestCase

from game.blackjack import explosion_rate


class Test(TestCase):
    def test_explosion_rate(self):
        card_list = [1, 2, 3, 4, 5]
        rate = explosion_rate(20, card_list)
        self.assertEqual(rate, 80)
        rate = explosion_rate(1, card_list)
        self.assertEqual(rate, 0)
        rate = explosion_rate(19, card_list)
        self.assertEqual(rate, 60)