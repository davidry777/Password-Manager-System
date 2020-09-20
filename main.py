from password_gen import generate_list
from password_creator import create_password
from password_keeper import print_menu, print_list, PasswordKeeper

if __name__ == "__main__":
    # password_list gets a generated list from password_gen
    password_list = generate_list()
    # password_helper is a class object that will help handle all the operations of
    # finding/changing usernames and passwords in the list
    password_helper = PasswordKeeper()

    print("***********************************")
    print("Hello! Welcome to Password Manager")
    print("***********************************")

    while True:
        print_menu()    # menu is being printed in password_keeper, gets input from user here in main
        ans = input("Enter: ")
        if ans == '1':
            password_list = create_password(password_list)  # Creates a new password and adds it to password list
        elif ans == '2':
            print_list(password_list)   # Prints the entire list for the user to view
        elif ans == '3':
            # Searches the entire list for the password using user-inputted website and username
            print("The password is {}\n".format(password_helper.find_password(password_list).get_password()))
        elif ans == '4':
            password_helper.change_password(password_list)  # Changes the password in the list
        elif ans == '5':
            password_helper.change_username(password_list)      # Changes the username in the list
        else:
            exit()  # Exits the loop and ends the program
