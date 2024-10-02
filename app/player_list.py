from player import Player
from player_node import PlayerNode

class PlayerList:
    """
    Represents an linked list of players
    """
    def __init__(self, values=None) -> None:
        """
        Initialises a player list

            Args:
                values (list): Takes an list of players to push to the list
        """
        if values == None:
            values = []
        self._head = None
        self._tail = None
        self._count = 0

        for item in values:
            self.add_to_head(item)

    def __len__(self) -> int:
        return self._count
    
    def delete(self, key: str) -> None:
        '''
        Deletes an value in the list by the given key

            Args:
                    key (str): An key that identifies the value to be removed

            Returns:
                    str: returns the key of the deleted item
        '''
        if self._head == None and self._tail == None:
            raise IndexError("Error, the list is empty")
        
        current_node = self._head
        while current_node is not None:
            if current_node.key == key:
                break
            current_node = current_node.previous

        if current_node == None:
            raise KeyError("The key was not found!!!")
        
        if current_node is self._head:
            self._head = current_node.previous
        if current_node is self._tail:
            self._tail = current_node.next
        
        if current_node.previous != None:
            current_node.previous.next = current_node.next
        if current_node.next != None:
            current_node.next.previous = current_node.previous

        self._count -= 1

    def add_to_head(self, value: Player):
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
            self._head.next = item

            self._head = item

        self._count += 1

    def shift(self) -> str:
        '''
        Removes an item from the head of the list
        '''
        if self._head == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self._head.player.uid
            self._head = None
            self._tail= None
        else:
            value = self._head.player.uid
            self._head = self._head.previous
            self._head.next = None

        self._count -= 1
        return value
    
    def add_to_tail(self, value: Player):
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
            item.next = self._tail

            self._tail = item

        self._count += 1

    def pop(self) -> str:
        '''Removes an item from the tail of the list'''
        if self._tail == None:
            raise IndexError("Error, the list is empty")
        elif self._count == 1:
            value = self._head.player.uid
            self._head = None
            self._tail = None
        else:
            value = self._tail.player.uid
            self._tail = self._tail.next
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
            while current_item.previous is not None:
                value += str(current_item.player) + " -> "
                current_item = current_item.previous
        else:
            current_item = self._tail
            while current_item.next is not None:
                value += str(current_item.player) + " -> "
                current_item = current_item.next
            

        value += str(current_item.player)

        print(value)

        return value
        
    
