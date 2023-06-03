"""Backend for the BMI Tracker application"""


class User():
    """Class User with methods to create and edit users"""

    def __init__(self, username):
        """Constructor for class User"""
        self.username = "Benutzer"

    def create_user(self, new_username):
        """Method to create a new User"""
        self.username = new_username
        return f'Benutzer: {self.username} erfolgreich erstellt!'

    def change_username(self, new_username):
        """Method to change a users name"""
        self.username = new_username
        return f'Benutzername erfolgreich zu: {self.username} geändert!'