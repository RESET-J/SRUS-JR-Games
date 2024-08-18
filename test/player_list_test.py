import unittest
import sys
sys.path.append('./app/')
from player_list import *

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

if __name__ == "__main__": 
    unittest.main()