from password_gen import find_object


class PasswordKeeper:

    def change_password(self, password_list):
        password_changer = self.find_password(password_list)
        verify_password = input("To change your password, enter your current password: ")
        if verify_password != password_changer.get_password():
            print("You have not entered the right password. Please try again later")
            exit()

        while True:
            ans = input("Please enter your new password:")
            if ans != "":
                password_changer.set_password(ans)
                print("Your new password is {}\n".format(password_changer.get_password()))
                break
            print("You have not entered your new password. Please try again.\n")

    def change_username(self, password_list):
        default_usernames = []
        username_changer = self.find_username(default_usernames, password_list)

        while True:
            ans = input("Please enter your new username:")
            if ans != "":
                username_changer.set_username(ans)
                break
            print("You have not entered your new username. Please try again.\n")

    def find_password(self, password_list):
        while True:
            ans = input("Please enter the website: ")
            website = find_object(ans, password_list)
            if website is not None:
                username = self.find_username(website.usernames, password_list=None)
                return username.password
            else:
                print("The website you entered is not in our list. Please try again")

    def find_username(self, usernames, password_list):
        if password_list is not None:
            ans1 = input("Please enter the website: ")
            website = find_object(ans1, password_list)
            if website is not None:
                usernames = website.usernames

        while True:
            ans2 = input("Enter the current username: ")
            for username in usernames:
                if ans2 == username.get_username():
                    return username
            print("Couldn't find current username. Please try again.\n")


def print_menu():
    print("-----------------------------")
    print("[1] Create a new password")
    print("[2] Print password list")
    print("[3] Search for password")
    print("[4] Change a password")
    print("[5] Change username")
    print("[0] Quit")
    print("-----------------------------")


def print_list(password_list):
    print("PASSWORD LIST:")
    print("[website]\n\t[username]\n\t\t[password]\n")

    for website in password_list:
        print("{}".format(website.get_website()))
        for username in website.usernames:
            print("\t{}".format(username.get_username()))
            password = username.password
            print("\t\t{}".format(password.get_password()))