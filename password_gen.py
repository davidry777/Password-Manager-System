class Password:
    """Class to represent a password

    Attributes:
        password (str): The password for the username
        username (str): The username that owns this password

    Methods:
        get_password: Used to return the password
        set_password: Used to set a new password to the user's account
    """

    def __init__(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password


class Username:
    """Class that represents the websites account(the Username)

    Attributes:
        username (str): The username for this account
        website_name (str): The name of the website the username belongs to

    Methods:
        get_username: Used to return the password
        set_username: Used to set a new password to the user's account
    """

    def __init__(self, username, password=None):
        self.username = username
        self.password = Password(password)

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username



class Website:
    """Class that represents the websites account(the Username)

    Attributes:
        website_name (str): The name of the website for all accounts under it

    Methods:
        get_website: Used to return the name of the website
    """

    def __init__(self, website_name):
        self.website_name = website_name
        self.usernames = []

    def get_website(self):
        return self.website_name

    def create_username(self, username):
        account = Username(username)
        self.usernames.append(account)


def generate_list():
    with open("default_accountList.txt", "r") as passwords:
        for line in passwords:
            website_field, username_field, password_field = tuple(line.strip('\n').split('/'))
            print("{}:{}:{}".format(website_field, username_field, password_field))


if __name__ == "__main__":
    generate_list()
