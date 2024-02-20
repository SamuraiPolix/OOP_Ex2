from Sender import *
from Receiver import *
from Post import PostFactory


class User (Sender, Receiver):
    def __init__(self, username: str, password: str):
        Sender.__init__(self)
        self.__username = username
        self.__password = password
        self.__isConnected = True
        self.__posts = []

    def get_username(self):
        return self.__username

    def is_connected(self):
        return self.__isConnected

    def is_correct_password(self, password: str):
        return password == self.__password

    def connect(self, password: str):
        if self.is_correct_password(password):
            self.__isConnected = True
        else:
            raise Exception(f"Password is incorrect!")

    def disconnect(self):
        self.__isConnected = False

    def follow(self, user):
        if self.__isConnected:
            user.add_follower(self)
            print(f"{self.__username} started following {user.__username}")
        else:
            # raise Exception(f"{self.__username} is not online!")
            print(f"Error: {self.__username} couldn't follow {user.get_username()} because {self.__username} is offline!")

    def unfollow(self, user):
        if self.__isConnected:
            try:
                user.remove_follower(self)
                print(f"{self.__username} unfollowed {user.__username}")
            except ValueError as ve:
                print(f"Error: Couldn't remove follower, because he is not following")
        else:
            # raise Exception(f"{self.__username} is not online!")
            print(f"Error: {self.__username} couldn't follow {user.get_username()} because {self.__username} is offline!")

    def publish_post(self, post_type: str, *args):
        post_maker = PostFactory(self)
        post = post_maker.create(post_type, *args)
        return post


    def print_notifications(self):



    def update(self, message: str):
        pass # TODO

    def __str__(self):
        return f"User name : {self.__username}, Number of posts: {len(self.__posts)}, Number of followers: {len(self._followers)}"





