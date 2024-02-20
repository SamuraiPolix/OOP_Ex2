from abc import ABC, abstractmethod
from enum import Enum

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from User import User


class PostTypes(str, Enum):
    IMAGE = "Image"
    TEXT = "Text"
    SALE = "Sale"


# Singleton + Factory
class PostFactory(ABC):
    __instance = None

    def __new__(cls, user: User):
        # If an instance doesn't already exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user: User):
        self.__user = user

    def create(self, post_type: str, *args):
        post = None
        if post_type == PostTypes.TEXT:
            post = TextPost(self.__user, args[0])
        elif post_type == PostTypes.IMAGE:
            post = ImagePost(self.__user, args[0])
        elif post_type == PostTypes.SALE:
            post = SalePost(self.__user, *args)
        return post


class Post(ABC):
    _likes: list
    _comments: []     # TODO stack?
    _owner: User

    def __init__(self, owner: User):
        self._likes = []
        self._comments = []
        self._owner = owner

    def like(self, user: User):
        self._likes.append(user)
        message = f"{user.get_username()} liked your post"
        self._owner.update(message)
        print(f"notification to {self._owner.get_username()}: {message}")

    def comment(self, user: User, text: str):
        comment = Comment(user, text)
        self._comments.append(comment)
        message = f"{user.get_username()} commented on your post: {text}"
        self._owner.update(message)
        print(f"notification to {self._owner.get_username()}: {message}")

    def __str__(self):
        return self._owner.get_username()


class Comment:
    def __init__(self, user: User, comment: str):
        self._user = user
        self._comment = comment

    def get_owner(self):
        return self._user

    def get_comment(self):
        return self._comment


class TextPost(Post):
    _content: str

    def __init__(self, owner: User, text: str):
        super().__init__(owner)
        self._content = text
        print(f"{owner.get_username()} published a post: {text}")

    def __str__(self):
        return self._content


class ImagePost(Post):
    _path: str

    def __init__(self, owner: User, img_path: str):
        super().__init__(owner)
        self._path = img_path
        print(f"{owner.get_username()} published a picture")

    def display(self):
        print("Shows picture")
        img = mpimg.imread(self._path)
        plt.imshow(img)
        plt.show()

    def __str__(self):
        return self._path


class SalePost(Post):
    _description: str
    _price: float
    _address: str
    _available: bool

    def __init__(self, owner: User, description: str, price: float, address: str):
        super().__init__(owner)
        self._description = description
        self._price = price
        self._address = address
        self._available = True
        print(f"{owner.get_username()} posted a product for sale:\n",
              f"For sale! {self.__str__()}")

    def sold(self, password: str):
        if self._owner.is_correct_password(password):
            self._available = False
            print(f"{self._owner.get_username()}'s product is sold")
        else:
            # raise Exception(f"Error setting Sale Post as sold: Wrong password")
            print("Error setting Sale Post as sold: Wrong password")

    def discount(self, discount_percent: float, password: str):
        if self._owner.is_correct_password(password):
            self._price *= (100-discount_percent)
            print(f"Discount on {self._owner.get_username()} product! the new price is: {self._price}")
        else:
            print(f"Error trying to add a discount to {self._owner.get_username()}'s Sale Post : Wrong Password")

    def __str__(self):
        return f"{self._description}, price: {self._price}, pickup from: {self._address}"



