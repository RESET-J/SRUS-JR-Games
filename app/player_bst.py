from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self) -> None:
        self._root = None

    def insert(self, key: Player, current_node=None) -> None:
        if current_node is None:
            current_node = self._root

        if self._root is None:
            player = PlayerBNode(key)
            self._root = player
            return
        if key.name == current_node.player.name:
            current_node.player = key
            return
        if key.name < current_node.player.name:
            if current_node.left is None:
                current_node.left = PlayerBNode(key)
            else:
                self.insert(key=key, current_node=current_node.left)
        else:
            if current_node.right is None:
                current_node.right = PlayerBNode(key)
            else:
                self.insert(key=key, current_node=current_node.right)

    def search(self, name: str) -> Player:
        return self._search(name=name, current_node=self._root)

    # the assignment says to return none if the current node is equal to None however
    # i felt that returning the player and an exception if the key was not found made more sense to me
    # i am happy to change if preffered / required
    def _search(self, name: str, current_node: PlayerBNode = None) -> Player:
        if current_node is None:
            raise KeyError("Error, the key is not found")
        
        if current_node.player.name == name:
            return current_node.player
        if current_node.player.name > name:
            return self._search(name=name, current_node=current_node.left)
        elif current_node.player.name < name:
            return self._search(name=name, current_node=current_node.right)
        
    def _show(self, current_node: PlayerBNode = None, values: list = None) -> list:
        """private function returns the items in the player bst as an list"""
        if current_node is None:
            return values
        if values is None:
            values = list()

        return (self._show(
            current_node.left, values) + [current_node.player] + self._show(current_node.right, values))
    
    def show(self) -> list:
        """Shows the items in the player bst as an list"""
        return self._show(current_node=self._root)


        
        


if __name__ == "__main__":
    bst = PlayerBST()

    bst.insert(Player("01", "Player1"))
    bst.insert(Player("02", "Player3"))
    bst.insert(Player("00", "Player2"))
    bst.insert(Player("03", "Player0"))
    bst.insert(Player("04", "player3"))

    print(bst._root.right.player.name)
    print(bst._root.left)
    print(bst._root.right.left.player)

    # print(bst.search("Player"))

    new_list = bst.show()

    for item in new_list: 
        print(item.name)
        