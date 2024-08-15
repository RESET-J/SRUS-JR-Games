class Player:
    def __init__(self, uid: str, name: str) -> None:
        self._uid = uid
        self._name = name
        # pass

    @property
    def uid(self):
        return self._uid
    @uid.setter
    def uid(self, value):
        self._uid = value
    
    @property
    def name(self): 
        return self._name
    
    def __str__(self) -> str:
        return f"{self._uid} {self._name}"