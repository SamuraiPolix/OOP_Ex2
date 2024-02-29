from abc import ABC

# Observer Design Pattern, used by User
# Used as an abstract


class Sender(ABC):
    _followers: list

    def __init__(self):
        self._followers = []

    def add_follower(self, follower):
        if not self._followers.__contains__(follower):
            self._followers.append(follower)
            return True
        else:
            return False

    def remove_follower(self, follower):
        # trying to remove the follower
        # if he is already not following - throws exception that is caught by the calling function
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

