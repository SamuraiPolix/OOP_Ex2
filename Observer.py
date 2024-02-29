from abc import ABC

# Observer Design Pattern, used by User
# Used as an abstract


class Sender(ABC):
    _followers: list

    def __init__(self):
        self._followers = []

    def add_follower(self, follower):
        self._followers.append(follower)

    def remove_follower(self, follower):
        self._followers.remove(follower)

    def notify_all(self, content: str):
        for follower in self._followers:
            follower.update(content)


class Receiver(ABC):
    _notifications: list

    def __init__(self):
        self._notifications = []

    def update(self, content: str):
        self._notifications.append(content)

