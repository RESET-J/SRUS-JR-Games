from __future__ import annotations
from player import Player

class PlayerBNode:
    def __init__(self, player) -> None:
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self) -> Player:
        return self._player
    
    @player.setter
    def player(self, value: Player) -> None:
        self._player = value

    @property
    def left(self) -> PlayerBNode:
        return self._left
    
    @left.setter
    def left(self, value: PlayerBNode) -> None:
        self._left = value

    @property
    def right(self) -> PlayerBNode:
        return self._right
    
    @right.setter
    def right(self, value: PlayerBNode):
        self._right = value
