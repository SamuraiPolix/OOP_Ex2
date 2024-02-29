# Implementing the Singleton design pattern
from User import User


class SocialNetwork:
    __instance = None
    __name: str
    __users: list

    def __new__(cls, network_name: str):
        # If an instance doesn't already exist, create one
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, network_name: str):
        # Makes sure the name is set only on the first created instance
        if not hasattr(self, '_SocialNetwork__name') or not self.__name:
            self.__name = network_name
            self.__users = []
            print(f"The social network {network_name} was created!")
        else:
            print(f"Social network {self.__name} already exists!")

    # Register a user to the network - returns null of registration fails
    def sign_up(self, username: str, password: str):
        if self.__is_valid_username(username) and self.__is_valid_password(password):
            user = User(username, password)
            self.__users.append(user)
            return user
        else:
            print(f"Error signing up user \"{username}\": username is already taken!")
            return None
            # Throw exception? no control over main.py

    def log_in(self, username: str, password: str):
        # search for user in list of users
        for user in self.__users:
            if user.get_username() == username:
                try:
                    user.connect(password)      # try connecting with the password
                    print(f"{username} connected")
                except Exception as e:          # connection failed
                    print(f"Error logging in user \"{username}\": ", e)
                return      # finished here - user found in list - either connected or not
        # If we got to here - the user was not found in the list - print error
        print(f"Error logging in user \"{username}\": User does not exist!")

    def log_out(self, username: str):
        # search for user in users
        for user in self.__users:
            if user.get_username() == username:
                user.disconnect()
                print(f"{username} disconnected")
                return
        # If we got to here - the user was not found in the list - print error
        print(f"Error logging out user \"{username}\": User does not exist!")

    def __is_valid_username(self, username: str):
        for user in self.__users:
            if user.get_username() == username:
                return False
        return True

    def __is_valid_password(self, password: str):
        return 4 <= len(password) <= 8

    def __str__(self):
        network_str = f"{self.__name} social network:"
        for user in self.__users:
            network_str += f"\n{user}"
        network_str += "\n"
        return network_str

