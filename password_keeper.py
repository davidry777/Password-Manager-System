from password_gen import Website, Username, Password, find_object


class PasswordKeeper:

    def find_password(self, password_list):
        while True:
            ans = input("To get password, please enter the website: ")
            website = find_object(ans, password_list)
            if website is not None:
                username = self.find_username(website.usernames, password_list=None)
                return username.password.get_password()
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
