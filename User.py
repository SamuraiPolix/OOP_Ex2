from Observer import Sender, Receiver
from PostFactory import PostFactory


# Implementing the Observer design pattern
# A User can be both a Sender and a Receiver (can follow and be followed)
class User (Sender, Receiver):
    __username: str
    __password: str
    __is_connected: bool
    __posts: list

    def __init__(self, username: str, password: str):
        Sender.__init__(self)
        Receiver.__init__(self)
        self.__username = username
        self.__password = password
        self.__is_connected = True
        self.__posts = []

    def get_username(self):
        return self.__username

    def is_connected(self):
        return self.__is_connected

    def is_correct_password(self, password: str):
        return password == self.__password

    def connect(self, password: str):
        if self.__is_connected:
            raise Exception(f"User is already logged in!")
        else:
            if self.is_correct_password(password):
                self.__is_connected = True
            else:
                raise Exception(f"Password is incorrect!")

    def disconnect(self):
        self.__is_connected = False

    def follow(self, user):
        # needs to be online to perform actions
        if self.__is_connected:
            if self.__username != user.get_username():
                was_follow_successful = user.add_follower(self)
                if was_follow_successful:
                    print(f"{self.__username} started following {user.__username}")
                else:   # 'Sender' couldn't add follower because he is already followed
                    print(f"Error: {user.get_username()} already follows {self.__username}")
            else:   # can't follow yourself
                print(f"Error: {self.__username} couldn't follow {user.get_username()}: You cannot follow yourself!")
        else:
            # raise Exception(f"{self.__username} is offline!")
            print(f"Error: {self.__username} couldn't follow {user.get_username()}: {self.__username} is offline!")

    def unfollow(self, user):
        # needs to be online to perform actions
        if self.__is_connected:
            if self.__username != user.get_username():
                try:
                    user.remove_follower(self)
                    print(f"{self.__username} unfollowed {user.__username}")
                except ValueError as ve:        # Error removing from list - no such follower registered
                    print(f"Error: {self.__username} couldn't unfollow {user.get_username()}: Already not following!")
            else:       # can't unfollow yourself
                print(f"Error: {self.__username} couldn't unfollow {user.get_username()}: You cannot unfollow yourself!")
        else:
            # raise Exception(f"{self.__username} is offline!")
            print(f"Error: {self.__username} couldn't unfollow {user.get_username()}: {self.__username} is offline!")

    # returns null if post creation fails
    def publish_post(self, post_type: str, *args):
        # needs to be online to perform actions
        if self.__is_connected:
            post_maker = PostFactory(self)
            post = post_maker.create(post_type, *args)
            if post is not None:      # If post creation was successful
                self.__posts.append(post)
                print(post)
                self.notify_all(f"{self.__username} has a new post")
            return post
        else:
            # raise Exception(f"{self.__username} is offline!")
            print(f"Error: {self.__username} couldn't publish a post: {self.__username} is offline!")
        return None

    def print_notifications(self):
        print(f"{self.__username}'s notifications:")
        for notification in self._notifications:
            print(notification)

    def __str__(self):
        return f"User name: {self.__username}, Number of posts: {len(self.__posts)}, Number of followers: {len(self._followers)}"





