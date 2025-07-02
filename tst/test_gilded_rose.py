# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_the_hand_keeps_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 42, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
