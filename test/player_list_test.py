import unittest

# from app.player_list import *
import sys
sys.path.append('./app/')
from app.player_list import *

player1 = Player("01", "Testing1")
player2 = Player("02", "Joel")
player3 = Player("03", "Rafael")

class PlayerListTest(unittest.TestCase):
    def test_push_empty(self):
        player = Player("player1", "Testing")
        mylist = PlayerList()

        mylist.push(player)
        self.assertEqual(len(mylist), 1)

    def test_push_multple(self):
        mylist = PlayerList()
        mylist.push(player1)
        mylist.push(player2)

        self.assertEqual(len(mylist), 2)

    def test_pop_empty(self):
        mylist = PlayerList()

        with self.assertRaises(IndexError):
            mylist.pop()

    def test_pop_values(self):
        mylist = PlayerList()

        mylist.push(player1)
        mylist.push(player2)

        self.assertEquals(mylist.pop(), "02")

    def test_push_and_pop(self):
        mylist = PlayerList()

        mylist.push(player1)
        mylist.push(player2)

        mylist.pop()

        self.assertEqual(mylist.pop(), "01")

        mylist.push(player3)

    def test_unshift_empty(self):
        mylist = PlayerList()
        
        mylist.unshift(player1)

        self.assertEqual(len(mylist), 1)

    def test_unshift_multiple(self):
        mylist = PlayerList()
        mylist.unshift(player1)
        mylist.unshift(player2)

        self.assertEqual(mylist.pop(), "01")

    def test_shift_empty(self):
        mylist = PlayerList()

        with self.assertRaises(IndexError):
            mylist.shift()

    def test_shift_values(self):
        mylist = PlayerList()

        mylist.unshift(player1)
        mylist.push(player2)

        self.assertEqual(mylist.shift(), "01")

    def test_shift_unshift(self):
        mylist = PlayerList()

        mylist.unshift(player1)
        mylist.pop()

        # mylist.

    def test_delete_empty(self):
        mylist = PlayerList()

        with self.assertRaises(IndexError):
            mylist.delete("01")

    def test_delete_not_found(self):
        mylist = PlayerList()

        mylist.push(player2)

        with self.assertRaises(KeyError):
            mylist.delete("01")

    def test_delete(self):
        mylist = PlayerList()

        mylist.push(player2)

        self.assertEqual(mylist.delete("02"), "02")
        mylist.unshift(player1)
        mylist.push(player3)

        self.assertEqual(mylist.delete("01"), "01")
        mylist.display(forward=False)

    def test_forward_true(self):
        mylist = PlayerList()

        mylist.push(player1)        
        mylist.push(player2)
        mylist.push(player3)

        value = mylist.display(forward=True)

        correct = "03 Rafael -> 02 Joel -> 01 Testing1"

        self.assertEqual(value, correct)

    def test_forward_false(self):
        mylist = PlayerList()

        mylist.push(player1)
        mylist.push(player2)
        mylist.push(player3)

        value = mylist.display(forward=False)

        correct = "01 Testing1 -> 02 Joel -> 03 Rafael"

        self.assertEqual(value, correct)

if __name__ == "__main__": 
    unittest.main()