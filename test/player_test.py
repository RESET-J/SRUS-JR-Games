import unittest
import sys
# sys.path.append('./app/')

# from player import *
# import inc_dec
from app.player import Player

class TestPlayerClass(unittest.TestCase):

    def test_uid(self):
        player1 = Player("01", "Test")

        self.assertEqual(player1.uid, "01")

    def test_name(self): 
        player1 = Player("01", "Test")

        self.assertEqual("Test", player1.name)

if __name__ == "__main__": 
    unittest.main()