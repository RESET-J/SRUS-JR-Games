import unittest
import random

from app.player import Player

class TestPlayerClass(unittest.TestCase):

    def test_uid(self):
        player1 = Player("01", "Test")

        self.assertEqual(player1.uid, "01")

    def test_name(self): 
        player1 = Player("01", "Test")

        self.assertEqual("Test", player1.name)

    def test_lt_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertTrue(player1 < player2)
        self.assertFalse(player2 < player1)

    def test_le_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertTrue(player1 <= player2)

    def test_eq_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 2
        player2.score = 2

        self.assertTrue(player1 == player2)

        player1.score = 1

        self.assertFalse(player1 == player2)

    def test_gt_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertTrue(player2 > player1)

        player1.score = 3

        self.assertFalse(player2 > player1)
        
    def test_ge_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertFalse(player1 >= player2)
        self.assertTrue(player2 >= player1)

    def test_lt_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertTrue(player1 < 2)

        with self.assertRaises(TypeError):
            self.assertFalse(player1 < "Hello")

    def test_le_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertTrue(player1 <= 1)

        with self.assertRaises(TypeError):
            self.assertFalse(player1 <= "Hello")

    def test_eq_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertTrue(player1 == 1)

        self.assertFalse(player1 == 2)

    def test_gt_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertFalse(player1 > 2)

        with self.assertRaises(TypeError):
            self.assertFalse(player1 > "Hello")

    def test_ge_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertTrue(player1 >= 0)

        with self.assertRaises(TypeError):
            self.assertFalse(player1 >= "Hello")

    def test_quick_sort(self):
        player1 = Player("01", "Joel")
        player1.score = 100
        player2 = Player("02", "Rocky")
        player2.score = 200
        player3 = Player("03", "Raf")
        player3.score = 300

        players = [player3, player1, player2]

        sorted_players = sorted(players)

        sorted_players.reverse()

        players = Player.quick_sort(players)

        self.assertTrue(players == sorted_players)

    def test_quick_sort_large_data(self):
        random_values = random.sample(range(1000), 1000)
        players = list()

        for item in range(1000):
            player = Player(str(random_values[item]), random_values[item])
            player.score = random_values[item]
            players.append(player)

        sorted_players = sorted(players)

        players = Player.quick_sort(players)

        sorted_players.reverse()

        self.assertEqual(players, sorted_players)
        
if __name__ == "__main__": 
    unittest.main()