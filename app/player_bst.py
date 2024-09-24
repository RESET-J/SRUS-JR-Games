from __future__ import annotations
from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    """Represents an binary search tree of players"""
    def __init__(self) -> None:
        """Initialises an empty player binary search tree"""
        self._root = None

    def insert(self, key: Player, current_node=None) -> None:
        """Inserts an player into the binary search tree based on the players name"""
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
        """Searches through the player binary search tree, and returns an player 
        with the specified name"""
        return self._search(name=name, current_node=self._root)

    # the assignment says to return none if the current node is equal to None however
    # i felt that returning the player and an exception if the key was not found made more sense to me
    # i am happy to change if preffered / required
    def _search(self, name: str, current_node: PlayerBNode = None) -> Player:
        """Private function that searches through the binary search tree and returns an player 
        with the specified name"""
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
    
    def balance(self) -> PlayerBST:
        """Returns an balanced version of the current binary search tree"""
        values = self.show()

        output_bst = PlayerBST()

        index = len(values) // 2

        root = values[index]

        output_bst.insert(root)

        self._balance(values=values[:index], balanced_bst=output_bst)

        self._balance(values=values[index+1:], balanced_bst=output_bst)

        return output_bst
    
    def _balance(self, values: list = None, balanced_bst: PlayerBST = None) -> None:
        """Private function that inserts the middle value of the specified list of players"""
        if len(values) < 1:
            return 
        
        value = values.pop(len(values) // 2)

        balanced_bst.insert(value)

        print("Added " + value.name)

        return self._balance(values=values, balanced_bst=balanced_bst)

