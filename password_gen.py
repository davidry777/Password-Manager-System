from password_generator import PasswordGenerator


class Password:
    """Class to represent a password

    Attributes:
        password (str): The password for the username
        username (str): The username that owns this password

    Methods:
        get_password: Used to return the password
        set_password: Used to set a new password to the user's account
    """

    def __init__(self, password, username):
        self.password = password
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password