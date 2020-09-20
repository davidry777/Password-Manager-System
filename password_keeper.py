from password_gen import find_object


class PasswordKeeper:
    """Class that will manage the finding and changing of passwords and usernames

    Methods:
        change_password: Changes the password using find_password method and uses verification
        change_username: Changes the username using find_username method
        find_password: Finds the password in the list and returns the Password object
        find_username: Helps change_username in finding the username and returns the Username object
    """
    def change_password(self, password_list):
        password_changer = self.find_password(password_list)    # Helps to change the password in the list
        verify_password = input("To change your password, enter your current password: ")   # Asks the user to input previous password
        if verify_password != password_changer.get_password():      # If password is not right, it declines user and takes it back to main
            print("You have not entered the right password. Please try again later")
            exit()

        while True:
            ans = input("Please enter your new password:")      # If user passes verification, it can enter new password
            if ans != "":
                password_changer.set_password(ans)      # Sets the new password
                print("Your new password is {}\n".format(password_changer.get_password()))      # Notifies user that new password is added
                break
            print("You have not entered your new password. Please try again.\n")    # If password is not entered properly, it loops back

    def change_username(self, password_list):
        default_usernames = []
        username_changer = self.find_username(default_usernames, password_list)     # Helps to change the username in the list

        while True:
            ans = input("Please enter your new username:")      # Asks user to input new username
            if ans != "":
                username_changer.set_username(ans)  # Sets the new username
                break
            print("You have not entered your new username. Please try again.\n")    # If username is not entered properly, it loops back

    def find_password(self, password_list):
        while True:
            ans = input("Please enter the website: ")   # First asks user to enter website
            website = find_object(ans, password_list)   # find_object method checks if website still exists in list
            if website is not None:
                username = self.find_username(website.usernames, password_list=None)    # if it exists, method gets username through find_username method
                return username.password    # returns the Password object of that username
            else:
                print("The website you entered is not in our list. Please try again")   # If website doesn't exist, it loops back

    def find_username(self, usernames, password_list):
        if password_list is not None:   # If usernames list isn't there, user must first enter the website
            ans1 = input("Please enter the website: ")
            website = find_object(ans1, password_list)
            if website is not None:
                usernames = website.usernames

        while True:
            ans2 = input("Enter the current username: ")    # Program asks user to input username
            for username in usernames:  # It goes through each Username object
                if ans2 == username.get_username():     # It checks if username is the same as what the user asked for
                    return username     # returns the Username object
            print("Couldn't find current username. Please try again.\n")    # If username doesn't exist, it loops back


def print_menu():
    print("-----------------------------")      # Prints out menu for user
    print("[1] Create a new password")
    print("[2] Print password list")
    print("[3] Search for password")
    print("[4] Change a password")
    print("[5] Change a username")
    print("[0] Quit")
    print("-----------------------------")


def print_list(password_list):
    print("PASSWORD LIST:")     # How password list is being formatted
    print("[website]\n\t[username]\n\t\t[password]\n")

    for website in password_list:   # Goes through all the websites
        print("{}".format(website.get_website()))
        for username in website.usernames:  # Goes through all the usernames
            print("\t{}".format(username.get_username()))
            password = username.password    # Gets and prints the password
            print("\t\t{}".format(password.get_password()))