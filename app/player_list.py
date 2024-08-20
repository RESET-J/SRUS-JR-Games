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
    
    def delete(self, key) -> str:
        if self.head == None:
            raise IndexError("Error, the list is empty")
        
        value = None
        if self._count == 1:
            if self.head.key == key:
                value = self.head
                self.head = None
                self.tail = None
            else:
                raise KeyError("Error, the specified key cannot be found")
        else:
            current_item = self.head
            while current_item.previous != None:
                if current_item.key == key:
                    value = current_item
                    break
                current_item = current_item.previous

            if current_item.key == key:
                value = current_item

            if value != None:
                if value.succeeding != None and value.previous != None:
                    value.previous.succeeding = value.succeeding
                    value.succeeding.previous = value.previous
                elif value.succeeding != None:
                    value.succeeding.previous = None
                elif value.previous != None:
                    value.previous.succeeding = None
            else:
                raise KeyError("Error, the specified key cannot be found")
            
        self._count -= 1
        return value.key
        

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
    
