from player import Player
from player_node import PlayerNode

class PlayerList:
    def __init__(self, values=[]) -> None:
        self.head = None
        self.tail = None
        self._count = 0

    def __len__(self) -> int:
        return self._count

    def push(self, value: Player):
        if self.head == None and self.tail == None:
            item = PlayerNode(value)
            self.head = item
            self.tail = item
        else:
            item = PlayerNode(value)
            item.previous = self.head
            self.head.succeeding = item

            self.head = item

        self._count += 1