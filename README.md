# Password Manager System

### Description

This was a project to demonstrate my Python programming skills.

This project first generates a default password list with websites, usernames, and passwords from a text file.
Each website contains a list of usernames, and each username has access to the password. A user can create a
new password, either by having the user enter their new password or having the program generate a
15-character password. The user can also print out the list, change a password, and change a username.

### How to run the progam

1. Clone the project either by using the git command line: ```% git clone https://github.com/davidry777/Password-Manager-System.git```
   Or by cloning it through Github Desktop or Github CLI: ```% gh repo clone davidry777/Password-Manager-System```.
2. Download and install ```random-password-generator``` by entering in command line ```% pip3 install random-password-generator```.
3. Compile and run the program the program using either a IDE or terminal.

### How it works
A password_list is a list containing Website, Username, and Password objects. The program can access these class objects
through the getter and setter methods in these classes. A list is better to use because it is mutable, meaning that
it can continually be changed and updated.

### The Skeleton of the List
The password_list mainly contains a list of Website objects, and each Website object has the ability to
create a Username. Every time a Username gets created, it will be appended to the list of Username objects(usernames).
Every Username will also have a Password, so the Password gets created along with the Username.

For visual here's how it would look:

![Diagram](https://github.com/davidry777/Password-Manager-System/blob/master/Images/password_list%20diagram.png)

*Generating a Password List*

A Password List is generated using the generate_list() function that reads default_accountList.txt containing default passwords. 
Each line in the text file contains a website, username, and password, each separated using '/'. 
During this process, generate_list() checks if the Website mentioned in each line is already in the password_list. 
If the Website is already in the list, generate_list() moves straight to appending the new Username and Password 
to the Website using the create_username() method. If not, the Website is first appended to the password_list() 
and later runs create_username() method. Once the process is over, password_list gets returned to main.

*User menu*

A menu is printed to the user and the user may enter the corresponding number for their choice. A while loop and
if, elif, and else statements are used to run the functions the user chooses.

### Structure of the Project
*main.py* - In charge of running the entire project. Contains the password_list and the password_helper, which helps
            to manage the updating and changing of lists. It also prints the menu for the user to see.
            
*password_gen.py* - Generates a default password_list for main.py to receive. It also contains Website, Username,
                 and Password objects that contain basic functions for managing its information.
                 
*password_creator.py* - Helps the user in creating a new password and adding it to the password_list. The project gives
                        the user a choice in either making a password or generating a new random password.
                        
*password_keeper.py* - Helps to print the password_list and the menu options. It also contains find_username(),
                       change_username(), find_password(), change_password() for making changes to the password_list.
                       
### Running the Program

The inital menu the user sees is this:
![Image of Menu](https://github.com/davidry777/Password-Manager-System/blob/master/Images/menu.png)

Adding a password would look like this:
![Image of Adding a Password](https://github.com/davidry777/Password-Manager-System/blob/master/Images/creating_password.png)

Changing a password looks like this:
![Image of Changing a Password](https://github.com/davidry777/Password-Manager-System/blob/master/Images/changing_password.png)

Changing a username looks like this:
![Image of Changing a Username](https://github.com/davidry777/Password-Manager-System/blob/master/Images/changing_username.png)

Printing the Password List in the system looks like this:
![Image of Printing the Password List](https://github.com/davidry777/Password-Manager-System/blob/master/Images/print_list.png)
