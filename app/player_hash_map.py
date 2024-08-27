from player_list import PlayerList, Player

class PlayerHashMap:
    """
    An hashmap of players

    Attributes:
        SIZE (int): The size of the hashmap
        hashmap (list): List of PlayerList()
    """
    def __init__(self) -> None:
        """
        Initialises an hashmap with the set size of 10
        """
        self.SIZE = 10
        self.hashmap = [PlayerList() for number in range(self.SIZE)]
        self._count = 0

        for item in self.hashmap:
            print(item)

    def __len__(self):
        return self._count

    def get_index(self, key: str | Player) -> int:
        """
        Gets the hash value of the specified key

        Args:
            key (str or Player): The key / uid of the players
        
        Returns:
            int: Returns the hash value of the input player id or key
        """
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        return Player.hash(key) % self.SIZE 
    
    def __getitem__(self, key: str) -> Player:
        index = self.get_index(key) 
        item = self.hashmap[index].find(key)

        return item
    
    def __setitem__(self, key: str, value: str) -> None:
        # if self._count == 0:
        #     raise IndexError("Error, the hash table is empty")
        
        index = self.get_index(key)

        try:
            item = self.hashmap[index].find(key)

            item._name = value
        except (IndexError, KeyError):
            self.hashmap[index].push(Player(key, value))
            self._count += 1

    def __delitem__(self, key:str) -> str:
        if self._count == 0:
            raise IndexError("Error, the hash table is empty")
        index = self.get_index(key)
        self.hashmap[index].delete(key)

        self._count -= 1

    def display(self) -> str:
        """
        Displays the players in the hashmap

        Returns:
            str: Returns an string of the players in the hashmap
        """
        if self._count == 0:
            raise IndexError("Error, the hashmap is empty")
        
        value = str()
        for item in self.hashmap:
            if len(item) >= 1:
                value += item.display(forward=True)

                if item != self.hashmap[len(self.hashmap) - 1]:
                    index = self.hashmap.index(item)
                    if len(self.hashmap[index + 1]) >= 1:
                        value += " -> "

        print(value)

        return value