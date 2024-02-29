# Implementing Singleton and Factory design patterns
from Post import ImagePost, TextPost, SalePost
from enum import Enum
from abc import ABC


# Enum to set post types
class PostTypes(str, Enum):
    IMAGE = "Image"
    TEXT = "Text"
    SALE = "Sale"


class PostFactory(ABC):
    __instance = None

    def __new__(cls, user):
        # If an instance doesn't already exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user):
        self.__user = user

    def create(self, post_type: str, *args):
        post = None
        if self.__user.is_connected():
            if post_type == PostTypes.TEXT:
                post = TextPost(self.__user, args[0])
            elif post_type == PostTypes.IMAGE:
                post = ImagePost(self.__user, args[0])
            elif post_type == PostTypes.SALE:
                post = SalePost(self.__user, *args)
            else:
                # raise Exception(f"ERROR: Couldn't create a post for {self.__user.get_username()}: \"Post type\" doesn't exist")
                print(f"Error: Couldn't create a post for {self.__user.get_username()}: \"Post type\" doesn't exist!")
        else:
            # raise Exception(f"ERROR: Couldn't create a post for {self.__user.get_username()}: {self.__user.get_username()} is offline!")
            print(f"Error: Couldn't create a post for {self.__user.get_username()}: {self.__user.get_username()} is offline!")

        return post
