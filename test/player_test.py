import unittest

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

        self.assertEqual(player1 < player2, True)
        self.assertEqual(player2 < player1, False)

    def test_le_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertEqual(player1 <= player2, True)

    def test_eq_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 2
        player2.score = 2

        self.assertEqual(player1 == player2, True)

        player1 = 1

        self.assertEqual(player1 == player2, False)

    def test_gt_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertEqual(player2 > player1, True)

        player1 = 3

        self.assertEqual(player2 > player1, False)
        
    def test_ge_player(self):
        player1 = Player("01", "Joel")
        player2 = Player("02", "Rocky")

        player1.score = 1
        player2.score = 2

        self.assertEqual(player1 >= player2, False)
        self.assertEqual(player2 >= player1, True)

    def test_lt_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertEqual(player1 < 2, True)

        with self.assertRaises(TypeError):
            self.assertEqual(player1 < "Hello", False)

    def test_le_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertEqual(player1 <= 1, True)

        with self.assertRaises(TypeError):
            self.assertEqual(player1 <= "Hello", False)

    def test_eq_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertEqual(player1 == 1, True)

        self.assertEqual(player1 == 2, False)

    def test_gt_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertEqual(player1 > 2, False)

        with self.assertRaises(TypeError):
            self.assertEqual(player1 > "Hello", False)

    def test_ge_value(self):
        player1 = Player("01", "Raf")

        player1.score = 1

        self.assertEqual(player1 >= 0, True)

        with self.assertRaises(TypeError):
            self.assertEqual(player1 >= "Hello", False)

    def test_quick_sort(self):
        player1 = Player("01", "Joel")
        player1.score = 100
        player2 = Player("02", "Rocky")
        player2.score = 200
        player3 = Player("03", "Raf")
        player3.score = 300

        players = [player3, player1, player2]

        sorted_players = sorted(players)

        Player.quick_sort(players, 0, len(players) - 1)

        self.assertEqual(players, sorted_players)
        
if __name__ == "__main__": 
    unittest.main()