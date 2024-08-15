import unittest
from app.player import Player
# import inc_dec
# from app.player import Player

class TestPlayerClass(unittest.TestCase):

    def test_uid(self):
        a = Player(1, "Test")

        self.assertEqual(a.uid, 1)

    def test_name(self): 
        a = Player(1, "Test")

        self.assertEqual("Test", a.name)

if __name__ == "__main__": 
    unittest.main()