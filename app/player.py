class Player:
    '''
    Represents an player with an uid and name.
    '''

    def __init__(self, uid: str, name: str) -> None:
        '''
        Initialises an player with an uid and name
        '''
        self._uid = uid
        self._name = name
        # pass

    @property
    def uid(self):
        return self._uid
    
    @property
    def name(self): 
        return self._name
    
    def __str__(self) -> str:
        return f"{self._uid} {self._name}"