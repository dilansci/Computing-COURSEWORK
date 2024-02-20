# Views/view_manager.py
import tkinter as tk

class AccountManager():
    currentAccount = None

    def __init__(self, name, pin, access_level):
        self.name = name
        self.pin = pin
        self.access_level = access_level

    @classmethod
    def login(cls, pin, control):
        # Get data from sql database (USE A FUCKING CONTROLLER)
        cls.control = control
        name = "Jimmy"
        pin = "1234"
        access_level = 3

        cls.currentAccount = AccountManager(name, pin, access_level)