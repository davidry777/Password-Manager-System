from password_gen import generate_list
from password_creator import create_password

if __name__ == "__main__":
    password_list = generate_list()

    print("***********************************")
    print("Hello! Welcome to Password Manager")
    print("***********************************")

    while True:
        ans = input("""------------------------------------------------------------------------------\n
                       [1] Create a new password\n
                       [2] Print list\n
                       ------------------------------------------------------------------------------\n
                       Enter: """)
        if ans == '1':
            password_list = create_password(password_list)
        elif ans == '2':
            for website in password_list:
                print("{}".format(website.get_website()))
                for username in website.usernames:
                    print("\t{}".format(username.get_username()))
                    password = username.password
                    print("\t\t{}".format(password.get_password()))

        print("***********************************")
