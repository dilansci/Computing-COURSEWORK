# Views/view_manager.py
import tkinter as tk

class AccountManager():
    currentAccount = None

    def __init__(self, pin, access_level):
        self.pin = pin
        self.access_level = access_level

    @classmethod
    def login(cls, pin, access_level, control):
        # Get data from sql database (USE A FUCKING CONTROLLER)
        print("THIS IS THE PIN",pin)
        print("THIS IS ACCESS_LEVEL",access_level)
        cls.control = control
        return cls.control.get_login(pin, access_level)
        # Example:
        # name = "Jimmy"
        # pin = "1234"
        # access_level = 3

        cls.currentAccount = AccountManager(pin, access_level)