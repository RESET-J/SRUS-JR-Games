import unittest

import sys
sys.path.append('./app/')
from app.player_hash_map import *

PLAYER1 = Player("01", "Rocky")
PLAYER2 = Player("02", "Joel")
PLAYER3 = Player("03", "Rafael")

class PlayerHashMapTest(unittest.TestCase):
    def test_add_player(self):
        myhashmap = PlayerHashMap()

        myhashmap["01"] = "Rocky"
        myhashmap["02"] = "Joel"
        myhashmap["03"] = "Rafael"
        myhashmap["07"] = "Testing1"
        myhashmap["04"] = "Testing2"
        myhashmap["05"] = "Testing3"
        myhashmap["06"] = "Testing4"

        self.assertEqual(myhashmap["01"].name, PLAYER1.name)

    def test_remove_player(self):
        myhashmap = PlayerHashMap()

        myhashmap["01"] = "Rocky"
        myhashmap["02"] = "Joel"
        myhashmap["03"] = "Rafael"

        del myhashmap["01"]

        self.assertEquals(len(myhashmap), 2)

    def test_modify_player(self):
        myhashmap = PlayerHashMap()

        myhashmap["01"] = "Rocky"
        myhashmap["02"] = "Joel"
        myhashmap["03"] = "Rafael"

        myhashmap["01"] = "Joel"

        self.assertEqual(myhashmap["01"].name, "Joel")

    def test_length(self):
        myhashmap = PlayerHashMap()

        myhashmap["01"] = "Rocky"

        self.assertEqual(len(myhashmap), 1)
        
        myhashmap["02"] = "Joel"

        self.assertEqual(len(myhashmap), 2)

        myhashmap["03"] = "Rafael"

        self.assertEqual(len(myhashmap), 3)

    def test_display(self):
        myhashmap = PlayerHashMap()

        myhashmap["01"] = "Rocky"
        myhashmap["01"] = "Joel"
        myhashmap["02"] = "Rafael"

        equal = "01 Joel -> 02 Rafael"

        self.assertEqual(myhashmap.display(), equal)

        