from password_gen import generate_list


if __name__ == "__main__":
    password_list = generate_list()

    for website in password_list:
        print(website)
