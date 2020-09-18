from password_gen import generate_list


if __name__ == "__main__":
    password_list = generate_list()

    for website in password_list:
        print("{}".format(website.get_website()))
        for username in website.usernames:
            print("\t{}".format(username.get_username()))
            password = username.password
            print("\t\t{}".format(password.get_password()))
