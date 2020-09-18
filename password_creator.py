from password_gen import find_object, Website
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


def print_password_menu():
    while True:
        # Menu options for adding a new password
        print("Would you like to:")
        ans = input("""\t[1] Enter your own preferred password?
                     \n\t[2] Create a randomly generated password?""")
        if ans == 1:
            return Creator.password_input()
        elif ans == 2:
            return Creator.generate_password()
        else:
            print("Sorry we didn't get the right response. Please try again")


def create_password(password_list):
    website_field = Creator.website_input()
    username_field = Creator.username_input()
    password_field = print_password_menu()

    new_password = find_object(website_field, password_list)
    if new_password is None:
        new_password = Website(website_field)
        password_list.append(new_password)

    new_password.create_username(username_field, password_field)

    return password_list
