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
        pwo = PasswordGenerator()   # pwo, a PasswordGenerator object, is in charge of generating a new random password
        pwo.minlen = 15     # Sets the password length to 15 characters
        pwo.maxlen = 15
        new_password = pwo.generate()   # Generates a random password

        print("Newly generated password: {}".format(new_password))
        print("NOTE: Make sure you copy this password before you create your new account")
        return new_password     # returns the generated password


def print_password_menu():
    while True:
        # Menu options for adding a new password
        print("Would you like to:")
        print("\t[1] Enter your own preferred password?")
        print("\t[2] Create a randomly generated password?")
        ans = input("Please enter: ")
        if ans == '1':
            # If user inputs '1', the user gets to input the new password and returns it
            return Creator.password_input()
        elif ans == '2':
            # If user inputs '2', the program gives the user a randomly generated password and returns it
            return Creator.generate_password()
        else:
            print("Sorry we didn't get the right response. Please try again")   # If no given response, menu loops


def create_password(password_list):
    # Different fields that the user must input to create a new password
    website_field = Creator.website_input()
    username_field = Creator.username_input()
    password_field = print_password_menu()

    new_password = find_object(website_field, password_list)    # Program checks if the website already exists in the list
    if new_password is None:
        new_password = Website(website_field)   # If given website doesn't exist, the new website is added to the list
        password_list.append(new_password)

    new_password.create_username(username_field, password_field)    # Under that website, a new username and password is created

    print("NEW PASSWORD ADDED!\n")  # User gets notified that new password is added

    return password_list    # returns the password list back to main.py
