from player import Player

class PlayerNode: 
    def __init__(self, player: Player) -> None:
        self._player = player
        self.key = self._player.uid
        self._previous = None
        self._next = None

    def __str__(self) -> str:
        return f"previous {self._previous} this {self.key} succeeding {self._next}"

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, value):
        self._next = value

    @property
    def player(self):
        return self._player