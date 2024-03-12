# Views/view_manager.py
import tkinter as tk

class AccountManager():

    def __init__(self, pin, access_level):
        self.pin = pin
        self.access_level = access_level

    @classmethod # this makes the method 'login' recieve a class as it's first argument ('cls') instead of 'self'
    def login(cls, pin, access_level, control):
        # Gets data from sql database
        # 'cls' is the class passed into 'login'
        cls.control = control
        return cls.control.get_login(pin, access_level)
        # Example:
        # name = "Jimmy"
        # pin = "1234"
        # access_level = 1
