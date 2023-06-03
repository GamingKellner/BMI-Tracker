"""Backend for the BMI Tracker application"""


class User():
    """Class User with methods to create and edit users"""

    def __init__(self, username, alter, geschlecht):    
        """Constructor for class User"""
        self.username = "Benutzer"
        self.alter = alter
        self.geschlecht = geschlecht

    def create_user(self, new_username, new_alter, new_geschlecht):
        """Method to create a new User"""
        self.username = new_username
        self.alter = new_alter
        self.geschlecht = new_geschlecht
        user_dict = {"Benutzername": self.username, "Alter": self.alter, "Geschlecht": self.geschlecht} #soll später in Tabelle "Benutzer" eingefügt werden        
        return f'Benutzer: {self.username} erfolgreich erstellt!'

    def change_username(self, new_username):
        """Method to change a users name"""
        self.username = new_username
        user_dict = {"Benutzername": self.username, "Alter": self.alter, "Geschlecht": self.geschlecht} #soll später in Tabelle "Benutzer" eingefügt werden
        return f'Benutzername erfolgreich zu: {self.username} geändert!'