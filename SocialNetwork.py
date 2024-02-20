# Singelton
from typing import Type

import UsersManager
from User import *


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
        self.__name = network_name
        self.__users = []
        print(f"The social network {network_name} was created!")
        # self.__users_manager = UsersManager.UsersManager()

    # Register a user to the network
    def sign_up(self, username: str, password: str):
        if self.__is_valid_username(username) and self.__is_valid_password(password):
            user = User(username, password)
            self.__users.append(user)
            return user
        else:
            return None
            # TODO Throw exception?

    def log_in(self, username: str, password: str):
        for user in self.__users:
            if user.get_username() == username:
                try:
                    user.connect(password)
                    print(f"{username} connected")
                except Exception as e:
                    print(f"Error logging in user \"{username}\": ", e)
                break

    def log_out(self, username: str):
        # TODO just remove and Throw exception?
        for user in self.__users:
            if user.get_username() == username:
                user.disconnect()
                print(f"{username} disconnected")
                break

    def __is_valid_username(self, username: str):
        for user in self.__users:
            if user.get_username() == username:
                return False
        return True

    def __is_valid_password(self, password: str):
        return 4 <= len(password) <= 8
