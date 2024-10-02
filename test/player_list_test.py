import unittest

import sys
sys.path.append('./app/')
from app.player_list import *

player1 = Player("01", "Testing1")
player2 = Player("02", "Joel")
player3 = Player("03", "Rafael")

class PlayerListTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.my_list = PlayerList()

    def test_push_empty(self):
        player = Player("player1", "Testing")

        self.my_list.add_to_head(player)

    def test_push_multple(self):
        self.my_list.add_to_head(player1)
        self.my_list.add_to_head(player2)

        self.assertEqual(len(self.my_list), 2)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.my_list.shift()

    def test_pop_values(self):
        self.my_list.add_to_head(player1)
        self.my_list.add_to_head(player2)

        self.assertEqual(self.my_list.shift(), "02")

    def test_push_and_pop(self):
        self.my_list.add_to_head(player1)
        self.my_list.add_to_head(player2)

        self.my_list.shift()

        self.assertEqual(self.my_list.shift(), "01")

        self.my_list.add_to_head(player3)

    def test_unshift_empty(self):
        self.my_list.add_to_tail(player1)

        self.assertEqual(len(self.my_list), 1)

    def test_unshift_multiple(self):
        self.my_list.add_to_tail(player1)
        self.my_list.add_to_tail(player2)

        self.assertEqual(self.my_list.shift(), "01")

    def test_shift_empty(self):
        with self.assertRaises(IndexError):
            self.my_list.pop()

    def test_shift_values(self):
        self.my_list.add_to_tail(player1)
        self.my_list.add_to_head(player2)

        self.assertEqual(self.my_list.pop(), "01")

    def test_shift_unshift(self):
        self.my_list.add_to_tail(player1)
        self.my_list.shift()

    def test_delete_empty(self):
        with self.assertRaises(IndexError):
            self.my_list.delete("01")

    def test_delete_not_found(self):
        self.my_list.add_to_head(player2)

        with self.assertRaises(KeyError):
            self.my_list.delete("01")

    def test_delete(self):
        self.my_list.add_to_head(player2)
        self.my_list.add_to_head(player1)
        self.my_list.add_to_head(player3)

        before_delete = self.my_list.display()

        self.my_list.delete("02")

        self.assertNotEqual(self.my_list.display(), before_delete)

        self.my_list.add_to_head(player2)

        before_length = len(self.my_list)

        self.my_list.delete("02")

        self.assertEqual(before_length - 1, len(self.my_list))

    def test_forward_true(self):
        self.my_list.add_to_head(player1)        
        self.my_list.add_to_head(player2)
        self.my_list.add_to_head(player3)

        value = self.my_list.display(forward=True)

        correct = "03 Rafael -> 02 Joel -> 01 Testing1"

        self.assertEqual(value, correct)

    def test_forward_false(self):
        self.my_list.add_to_head(player1)
        self.my_list.add_to_head(player2)
        self.my_list.add_to_head(player3)

        value = self.my_list.display(forward=False)

        correct = "01 Testing1 -> 02 Joel -> 03 Rafael"

        self.assertEqual(value, correct)

if __name__ == "__main__": 
    unittest.main()