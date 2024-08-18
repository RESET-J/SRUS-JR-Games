from player import Player
from player_node import PlayerNode

class PlayerList:
    def __init__(self, values=[]) -> None:
        self.head = None
        self.tail = None
        self._count = 0

        for item in values:
            self.push(item)

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

    def pop(self) -> str:
        if self.head == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self.head.player.uid
            self.head == None
            self.tail == None
        else:
            value = self.head.player.uid
            self.head = self.head.previous
            self.head.succeeding = None

        self._count -= 1
        return value
    
    def unshift(self, value: Player):
        if self.head == None and self.tail == None:
            item = PlayerNode(value)
            self.head = item
            self.tail = item
        else:
            item = PlayerNode(value)
            self.tail.previous = item
            item.succeeding = self.tail

            self.tail = item

        self._count += 1

    def shift(self) -> str:
        if self.tail == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self.head.player.uid
            self.head == None
            self.tail == None
        else:
            value = self.tail.player.uid
            self.tail = self.tail.succeeding
            self.tail.previous = None

        self._count -= 1
        return value
    
