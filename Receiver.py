# Observer Design Patter
# Used as an abstract
from abc import ABC, abstractmethod


class Receiver(ABC):
    def __init__(self):
        self._notifications = []

    @abstractmethod
    def update(self, content: str):
        pass