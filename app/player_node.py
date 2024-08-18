from player import Player

class PlayerNode: 
    def __init__(self, player: Player) -> None:
        self._player = player
        self.key = self._player.uid
        self._previous = None
        self._succeeding = None

    def __str__(self) -> str:
        return f"previous {self._previous} this {self.key} succeeding {self._succeeding}"

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, value):
        self._previous = value

    @property
    def succeeding(self):
        return self._succeeding
    
    @succeeding.setter
    def succeeding(self, value):
        self._succeeding = value

    @property
    def player(self):
        return self._player