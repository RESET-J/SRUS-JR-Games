from player import Player
from player_node import PlayerNode

class PlayerList:
    '''
    Represents an linked list of players 
    '''
    def __init__(self, values=[]) -> None:
        """
        Initialises an player list

            Args:
                values (list): Takes an list of players to push to the list
        """
        self._head = None
        self._tail = None
        self._count = 0

        for item in values:
            self.push(item)

    def __len__(self) -> int:
        return self._count
    
    def delete(self, key) -> str:
        '''
        Deletes an value in the list by the given key

            Args:
                    key (str): An key that identifies the value to be removed

            Returns:
                    str: returns the key of the deleted item
        '''
        if self._head == None:
            raise IndexError("Error, the list is empty")
        
        value = None
        if self._count == 1:
            if self._head.key == key:
                value = self._head
                self._head = None
                self._tail = None
            else:
                raise KeyError("Error, the specified key cannot be found")
        else:
            current_item = self._head
            while current_item.previous != None:
                if current_item.key == key:
                    value = current_item
                    break
                current_item = current_item.previous

            if current_item.key == key and value == None:
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
        '''
        Adds an item to the head of the list

            Args:
                value (Player): The item to be added to the list
        '''
        if self._head == None and self._tail == None:
            item = PlayerNode(value)
            self._head = item
            self._tail = item
        else:
            item = PlayerNode(value)
            item.previous = self._head
            self._head.succeeding = item

            self._head = item

        self._count += 1

    def pop(self) -> str:
        '''
        Removes an item from the head of the list
        '''
        if self._head == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self._head.player.uid
            self._head == None
            self._tail == None
        else:
            value = self._head.player.uid
            self._head = self._head.previous
            self._head.succeeding = None

        self._count -= 1
        return value
    
    def unshift(self, value: Player):
        '''
        Adds an item to the tail of the list

            Args:
                value (Player): The item to be added to the list
        '''
        if self._head == None and self._tail == None:
            item = PlayerNode(value)
            self._head = item
            self._tail = item
        else:
            item = PlayerNode(value)
            self._tail.previous = item
            item.succeeding = self._tail

            self._tail = item

        self._count += 1

    def shift(self) -> str:
        '''Removes an item from the tail of the list'''
        if self._tail == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self._head.player.uid
            self._head == None
            self._tail == None
        else:
            value = self._tail.player.uid
            self._tail = self._tail.succeeding
            self._tail.previous = None

        self._count -= 1
        return value
    
    def display(self, forward: bool = True) -> str:
        """
        Displays the items in the list in order, forward = true head -> tail, forward = false tail -> head

            Args:
                forward (bool): Determines the order in which the list in printed
        """
        if self._head == None:
            raise IndexError("Error, the list in empty")

        value = ""

        if forward:
            current_item = self._head
            while current_item.previous != None:
                value += str(current_item.player) + " -> "
                current_item = current_item.previous
        else:
            current_item = self._tail
            while current_item.succeeding != None:
                value += str(current_item.player) + " -> "
                current_item = current_item.succeeding
            

        value += str(current_item.player)

        print(value)

        return value
    
