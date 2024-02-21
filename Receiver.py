# Observer Design Patter
# Used as an abstract
from abc import ABC, abstractmethod


class Receiver(ABC):
    def __init__(self):
        self._notifications = []

    def update(self, content: str):
        self._notifications.append(content)

