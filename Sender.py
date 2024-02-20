# Observer Design Patter
# Used as an abstract
from abc import ABC, abstractmethod
import User


class Sender(ABC):
    def __init__(self):
        self._followers = []

    def add_follower(self, follower: User):
        self._followers.append(follower)

    def remove_follower(self, follower: User):
        self._followers.remove(follower)

    def notify_all(self, content: str):
        for follower in self._followers:
            follower.update(content)