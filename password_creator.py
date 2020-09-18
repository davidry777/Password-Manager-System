from password_gen import Website, Username, Password
from password_generator import PasswordGenerator


class Creator:
    """Class for creating a brand new password

    Static Methods:
        website_input (str): Receives user input for what website their new account belongs to.
        username_input (str): Receives user input for the username of their new account
        password_input (str): Receives user input for the password of their new account
        generate_password (str): Creates a randomly generated password using the PasswordGenerator library
    """
    @staticmethod
    def website_input():
        return input("Enter the link of the website your new account belongs to\n ('Website name'.'Domain'): ")

    @staticmethod
    def username_input():
        return input("Enter the username of your new account: ")

    @staticmethod
    def password_input():
        return input("Enter the password to your new account (Don't show it to anyone): ")

    @staticmethod
    def generate_password():
        pwo = PasswordGenerator()
        print("Newly generated password: {}".format(pwo))
        print("NOTE: Make sure you copy this password before you create your new account")
        return pwo