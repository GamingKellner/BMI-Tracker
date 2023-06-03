"""Backend for the BMI Tracker application"""


class User():
    """Class User with methods to create and edit users"""

    def __init__(self, username):
        """Constructor for class User"""
        self.username = "Benutzer"

    def create_user(self):
        """Method to create a new User"""
        new_user = input("Wollen Sie einen neuen Benutzer anlegen? (y/n):")
        if new_user == "y":
            self.username = input("Benutzername:")
        return