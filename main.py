from password_gen import generate_list
from password_creator import create_password
from password_keeper import print_menu, print_list, PasswordKeeper

if __name__ == "__main__":
    password_list = generate_list()
    password_helper = PasswordKeeper()

    print("***********************************")
    print("Hello! Welcome to Password Manager")
    print("***********************************")

    while True:
        print_menu()
        ans = input("Enter: ")
        if ans == '1':
            password_list = create_password(password_list)
        elif ans == '2':
            print_list(password_list)
        elif ans == '3':
            print("The password is {}\n".format(password_helper.find_password(password_list).get_password()))
        elif ans == '4':
            password_helper.change_password(password_list)
        elif ans == '5':
            password_helper.change_username(password_list)
        else:
            exit()
