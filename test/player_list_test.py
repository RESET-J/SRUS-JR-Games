import unittest
import sys
sys.path.append('./app/')
from player_list import *

class PlayerListTest(unittest.TestCase):
    def test_push_empty(self):
        player = Player("player1", "Testing")
        mylist = PlayerList()

        mylist.push(player)

if __name__ == "__main__": 
    unittest.main()