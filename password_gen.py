class Password:
    """Class to represent a password

    Attributes:
        password (str): The password for the username

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
        password (str): The password for the username

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

    def create_username(self, username, password):
        account = Username(username, password)
        self.usernames.append(account)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.website_name == field:
            return item
    return None


def generate_list():
    password_list = []

    with open("default_accountList.txt", "r") as passwords:
        for line in passwords:
            website_field, username_field, password_field = tuple(line.strip('\n').split('/'))
            # print("{}:{}:{}".format(website_field, username_field, password_field))

            new_website = find_object(website_field, password_list)
            if new_website is None:
                new_website = Website(website_field)
                password_list.append(new_website)

            new_website.create_username(username_field, password_field)

    return password_list
