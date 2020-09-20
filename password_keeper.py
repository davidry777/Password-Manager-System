from password_gen import Website, Username, Password, find_object


class PasswordKeeper():

    def find_password(self, password_list):
        ans1 = input("To search for password, enter website: ")
        webfinder = find_object(ans1, password_list)
        ans2 = input("Enter your username")
        userfinder =

        print("The password for your {1} account, under the username {2}, is {3}".format(webfinder, userfinder,
                                                                                         userfinder.password.get_password()))


    def find_username(self, field, object_list):
        """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for username in object_list.usernames:
        if item.website_name == field:
            return item
    return None


def print_menu():
    print("-----------------------------")
    print("[1] Create a new password")
    print("[2] Print password list")
    print("[3] Search for password")
    print("[4] Change a password")
    print("[5] Change username")
    print("[0] Quit")
    print("-----------------------------")
