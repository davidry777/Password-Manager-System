# Credit Card System

### Description

This was a project to demonstrate my Python programming skills.

This project first generates a default password list with websites, usernames, and passwords from a text file.
Each website contains a list of usernames, and each username has access to the password. A user can create a
new password, either by having the user enter their new password or having the program generate a
15-character password. The user can also print out the list, change a password, and change a username.

### How to run the progam

1. Clone the project either by using the git command line: ```% git clone https://github.com/davidry777/Password-Manager-System.git```
   Or by cloning it through Github Desktop or Github CLI: ```% gh repo clone davidry777/Password-Manager-System```
2. Download and install ```random-password-generator``` by entering in command line ```% pip3 install random-password-generator```
3. Compile and run the program the program using either a IDE or terminal.

### How it works
A Password List is a list containing Website, Username, and Password objects. The program can access these class objects
through the getter and setter methods in these classes. A list is better to use because it is mutable, meaning that
it can continually be changed and updated.

### The Skeleton of the List
The Password List mainly contains a list of Website objects, and each Website object has the ability to
create a Username. Every time a Username gets created, it will be appended to the list of Username objects.
Every Username will also have a Password, so the Password gets created along with the Username.

For visual here's how it would look
