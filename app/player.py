from __future__ import annotations
import random
from typing import Any

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
        self._score = 0
        # pass

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
    def partition(values: list, low: int, high: int) -> int:
        pivot = values[high]

        i = low - 1

        for j in range(low, high):
            if values[j] <= pivot:
                i = i + 1

                (values[i], values[j]) = (values[j], values[i])

        (values[i + 1], values[high]) = (values[high], values[i + 1])

        return i + 1
    
    @staticmethod
    def quick_sort(values: list, low: int, high: int) -> None:
        if low < high:
            pi = Player.partition(values, low, high)

            Player.quick_sort(values, low, pi - 1)

            Player.quick_sort(values, pi + 1, high)

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
    