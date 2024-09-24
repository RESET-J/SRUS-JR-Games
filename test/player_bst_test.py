import unittest
import sys
sys.path.append('./app/')

from app.player_bst import PlayerBST, Player
import random

class PlayerBSTTest(unittest.TestCase): 
    def setUp(self) -> None:
        super().setUp()

        self.bst = PlayerBST()

    def test_player_bst_insert_value(self):
        self.bst.insert(Player("01", "Player1"))
        self.bst.insert(Player("03", "Player3"))
        self.bst.insert(Player("02", "Player2"))
        self.bst.insert(Player("05", "Player5"))
        self.bst.insert(Player("04", "Player4"))

        self.assertEqual(self.bst._root.player.name, "Player1")
        self.assertEqual(self.bst._root.right.player.name, "Player3")
        self.assertEqual(self.bst._root.right.right.left.player.name, "Player4")

    def test_player_bst_insert_same_value(self):
        self.bst.insert(Player("01", "Player1"))
        self.bst.insert(Player("02", "Player1"))

        self.assertEqual(self.bst._root.player.uid, "02")

    def test_player_bst_search_when_empty(self):
        with self.assertRaises(KeyError):
            self.bst.search("Player1")

    def test_player_bst_search(self):
        self.bst.insert(Player("01", "Player1"))
        self.bst.insert(Player("02", "Player2"))
        self.bst.insert(Player("03", "Player3"))
        
        self.assertEqual(self.bst.search("Player1").name, "Player1")
        self.assertEqual(self.bst.search("Player3").name, "Player3")

    def test_player_bst_search_multiple(self):
        values = random.sample(range(1000), 1000)

        for value in values:
            self.bst.insert(Player(str(value), "Player" + str(value)))

        for i in range(100):
            random_name = "Player" + str(random.choice(values))

            self.assertEqual(self.bst.search(random_name).name, random_name)

    def test_player_bst_show(self):
        self.bst.insert(Player("01", "Player1"))
        self.bst.insert(Player("02", "Player2"))
        self.bst.insert(Player("03", "Player3"))
        self.bst.insert(Player("04", "Player4"))
        self.bst.insert(Player("05", "Player5"))

        assert_values = sorted(self.bst.show())

        output_values = self.bst.show()

        self.assertEqual(assert_values, output_values)

    def test_player_bst_balance(self):
        self.bst.insert(Player("01", "Player1"))
        self.bst.insert(Player("02", "Player2"))
        self.bst.insert(Player("03", "Player3"))
        self.bst.insert(Player("04", "Player4"))
        self.bst.insert(Player("05", "Player5"))

        self.bst = self.bst.balance()

        self.assertEqual(self.bst._root.player.name, "Player3")
        self.assertEqual(self.bst._root.left.player.name, "Player2")
        self.assertEqual(self.bst._root.right.player.name, "Player5")
        self.assertEqual(self.bst._root.left.left.player.name, "Player1")
        self.assertEqual(self.bst._root.right.left.player.name, "Player4")

