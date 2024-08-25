import random

random.seed(42)

pearson_table = list(range(256))
random.shuffle(pearson_table)

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

    @staticmethod
    def hash(key: str) -> int:
        hash_ = 0
        for char in key:
            hash_ = pearson_table[hash_ ^ ord(char)]

        return hash_
    
    def __hash__(self) -> int:
        return self.hash(self.uid)

    @property
    def uid(self):
        return self._uid
    
    @property
    def name(self): 
        return self._name
    
    def __str__(self) -> str:
        return f"{self._uid} {self._name}"