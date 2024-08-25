from player_list import PlayerList

class PlayerHashMap:
    def __init__(self) -> None:
        self.SIZE = 10
        self.hashmap = [PlayerList() for number in range(self.SIZE)]

        for item in self.hashmap:
            print(item)

if __name__ == "__main__":
    mylist = PlayerHashMap()