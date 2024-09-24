from __future__ import annotations
import random
from typing import Any

random.seed(42)

pearson_table = list(range(256))
random.shuffle(pearson_table)

class Player:
    '''
    Represents a player with an uid and name.
    '''

    def __init__(self, uid: str, name: str) -> None:
        '''
        Initialises a player with an uid and name
        '''
        self._uid = uid
        self._name = name
        self._score = 0

    def __lt__(self, other: Player | Any) -> bool:
        if isinstance(other, Player):
            return self._score < other.score
        return self._score < other
    
    def __le__(self, other: Player | Any) -> bool:
        if isinstance(other, Player):
            return self._score <= other.score
        return self._score <= other
    
    def __eq__(self, other: Player | Any) -> bool:
        if isinstance(other, Player):
            return self._score == other.score
        return self._score == other
    
    def __gt__(self, other: Player | Any) -> bool:
        if isinstance(other, Player):
            return self._score > other.score
        return self._score > other
    
    def __ge__(self, other: Player | Any) -> bool:
        if isinstance(other, Player):
            return self._score >= other.score
        return self._score >= other
    
    @staticmethod
    def quick_sort(values: list) -> list:
        """
        Sorts an list of objects with an quick sort algorithm
        """
        if len(values) <= 1:
            return values
        else:
            pivot = values[0]
            left = [x for x in values[1:] if x > pivot]
            right = [x for x in values[1:] if x <= pivot]
            return Player.quick_sort(left) + [pivot] + Player.quick_sort(right)

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
    
    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value: int) -> None:
        self._score = value

    def __str__(self) -> str:
        return f"{self._uid} {self._name}"
    