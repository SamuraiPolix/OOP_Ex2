# In charge of all types of 'Post' (ImagePost, TestPost, SalesPost, etc.)
from abc import ABC
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post(ABC):
    def __init__(self, owner):
        self._likes = []
        self._comments = []
        self._owner = owner

    def like(self, user):
        if user.is_connected():
            if not self._likes.__contains__(user):
                self._likes.append(user)
                # Notify only if someone other than the owner likes the post
                if user.get_username() != self._owner.get_username():
                    message = f"{user.get_username()} liked your post"
                    self._owner.update(message)
                    print(f"notification to {self._owner.get_username()}: {message}")
            else:
                print(f"Error: {user.get_username()} already liked {self._owner.get_username()}'s post!")
        else:
            print(f"Error: {user.get_username()} couldn't like {self._owner.get_username()}'s post: {user.get_username()} is offline!")

    def comment(self, user, text):
        if user.is_connected():
            comment = Comment(user, text)
            self._comments.append(comment)
            # Notify only if someone other than the owner commented on the post
            if user.get_username() != self._owner.get_username():
                message = f"{user.get_username()} commented on your post"
                self._owner.update(message)
                print(f"notification to {self._owner.get_username()}: {message}: {text}")
        else:
            print(f"Error: {user.get_username()} couldn't comment on {self._owner.get_username()}'s post: {user.get_username()} is offline!")

    def display(self):
        # Default for all post types that doesn't have a display() function.
        # ImagePost overrides this.
        print(f"Error: display() function is not available for a {self.__class__.__name__}!")

    def __str__(self):
        return self._owner.get_username()


class Comment:
    def __init__(self, user, comment: str):
        self._user = user
        self._comment = comment

    def get_owner(self):
        return self._user

    def get_comment(self):
        return self._comment


class TextPost(Post):
    _content: str

    def __init__(self, owner, text: str):
        super().__init__(owner)
        self._content = text

    def __str__(self):
        return f"{self._owner.get_username()} published a post:\n\"{self._content}\"\n"


class ImagePost(Post):
    _path: str

    def __init__(self, owner, img_path: str):
        # Lets you create a post with an invalid path, but displaying won't work
        super().__init__(owner)
        # if not os.path.isfile(img_path):
        #     print(f"Warning: '{img_path}' File doesn't exist. (Post still created. display() won't work)\n")
        self._path = img_path

    def display(self):
        # if os.path.isfile(self._path):
        print("Shows picture")
        img = mpimg.imread(self._path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        # else:
        #     print(f"Error: couldn't display image '{self._path}': File doesn't exist in current directory.\n")

    def __str__(self):
        return f"{self._owner.get_username()} posted a picture\n"


class SalePost(Post):
    _description: str
    _price: float
    _address: str
    _available: bool
    _status: str

    def __init__(self, owner, description: str, price: float, address: str):
        super().__init__(owner)
        if price < 0:
            print("Warning: Price on sales post is invalid. (Post created anyways)\n")
        self._description = description
        self._price = price
        self._address = address
        self._available = True
        self._status = "For sale!"

    def sold(self, password: str):
        if self._owner.is_correct_password(password):
            self._available = False
            self._status = "Sold!"
            print(f"{self._owner.get_username()}'s product is sold")
        else:
            # raise Exception(f"Error setting Sale Post as sold: Wrong password")
            print("Error setting Sale Post as sold: Wrong password")

    def discount(self, discount_percent: float, password: str):
        if self._owner.is_correct_password(password):
            if discount_percent < 0 or discount_percent > 100:
                print("Error: Discount percent in invalid. (Discount not logged)\n")
            else:
                self._price *= (100-discount_percent)/100
                print(f"Discount on {self._owner.get_username()} product! the new price is: {self._price}")
        else:
            print(f"Error: couldn't add a discount to {self._owner.get_username()}'s Sale Post : Wrong Password!")

    def __str__(self):
        return (f"{self._owner.get_username()} posted a product for sale:"
                f"\n{self._status} {self._description}, price: {self._price}, pickup from: {self._address}\n")



