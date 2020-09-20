from password_gen import Website, Username, Password, find_object


class PasswordKeeper:

    def change_password(self, password_list):
        password_changer = self.find_password(password_list)

        while True:
            ans = input("Please enter your new password:")
            if ans != "":
                password_changer.set_password(ans)
                break
            print("You have not entered your new password. Please try again.\n")

    def change_username(self, password_list):
        username_changer = self.find_username(usernames=None, password_list)

        while True:
            ans = input("Please enter your new username:")
            if ans != "":
                username_changer.set_username(ans)
                break
            print("You have not entered your new username. Please try again.\n")

    def find_password(self, password_list):
        while True:
            ans = input("To get password, please enter the website: ")
            website = find_object(ans, password_list)
            if website is not None:
                username = self.find_username(website.usernames, password_list=None)
                return username.password
            else:
                print("The website you entered is not in our list. Please try again")

    def find_username(self, usernames, password_list):
        if password_list is not None:
            ans1 = input("To get username, please enter the website: ")
            website = find_object(ans1, password_list)
            if website is not None:
                usernames = website.usernames

        while True:
            ans2 = input("Enter the username: ")
            for username in usernames:
                if ans2 == username.get_username():
                    return username
            print("Couldn't find username. Please try again.\n")


def print_menu():
    print("-----------------------------")
    print("[1] Create a new password")
    print("[2] Print password list")
    print("[3] Search for password")
    print("[4] Change a password")
    print("[5] Change username")
    print("[0] Quit")
    print("-----------------------------")
