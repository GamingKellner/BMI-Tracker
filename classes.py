"""Backend for the BMI Tracker application"""
from datetime import date

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
        user_dict = {
            "Benutzername": self.username,
            "Alter": self.alter,
            "Geschlecht": self.geschlecht
        } #soll später in Tabelle "Benutzer" eingefügt werden        
        return f'Benutzer: {self.username} erfolgreich erstellt!'

    def change_username(self, new_username):
        """Method to change a users name"""
        self.username = new_username
        user_dict = {
            "Benutzername": self.username,
            "Alter": self.alter,
            "Geschlecht": self.geschlecht
        } #soll später in Tabelle "Benutzer" eingefügt werden
        return f'Benutzername erfolgreich zu: {self.username} geändert!'
    
class Measurement():
    """Class measurement"""

    def __init__(self, username, today, bodyweight, bodyheight):
        """Constructor for every measurement"""
        self.username = User.username
        self.today = date.today()
        self.bodyweight = bodyweight
        self.bodyheight = bodyheight

    
class Calculation():
    """Class Calculation"""

    def __init__(self, username, today, bmi, calories):
        """Constructor for the class Calculation"""
        self.username = User.username
        self.today = date.today()
        self.bmi = bmi
        self.calories = calories

    def calculate_bmi(self, bodyweight, bodyheight):
        """Method to to calculate the bmi"""
        self.bmi = bodyweight / (bodyheight ** 2)
        bmi_dict = {
            "Benutzername": self.username,
            "Datum": self.today,
            "BMI": self.bmi,
            "Kalorien": self.calories
        }