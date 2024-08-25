from player_list import PlayerList, Player

class PlayerHashMap:
    def __init__(self) -> None:
        self.SIZE = 10
        self.hashmap = [PlayerList() for number in range(self.SIZE)]
        self._count = 0

        for item in self.hashmap:
            print(item)

    def __len__(self):
        return self._count

    def get_index(self, key: str | Player):
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        return Player.hash(key) % self.SIZE 
    
    def __getitem__(self, key) -> Player:
        index = self.get_index(key) 
        item = self.hashmap[index].find(key)

        return item
    
    def __setitem__(self, key, value) -> None:
        # if self._count == 0:
        #     raise IndexError("Error, the hash table is empty")
        
        index = self.get_index(key)

        try:
            item = self.hashmap[index].find(key)

            item._name = value
        except IndexError or KeyError:
            self.hashmap[index].push(Player(key, value))
            self._count += 1

    def __delitem__(self, key) -> str:
        if self._count == 0:
            raise IndexError("Error, the hash table is empty")
        index = self.get_index(key)
        self.hashmap[index].delete(key)

        self._count -= 1


if __name__ == "__main__":
    mylist = PlayerHashMap()

    mylist["Hello"] = "py"
    mylist["Hello"] = "ay"
    player = mylist["Hello"]

    print(len(mylist))