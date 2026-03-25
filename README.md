# INET4031 Add Users Script and User List

## Program Description
This program automates the process of creating user accounts and assigning group memberships. Usually, some would have to manually create users and assign users to groups. This manual process can be time-consuming and error-prone.

This code simplifies that process by reading user information from an input file and automatically executing the necessary system commands. It uses the commands used for the manuel process, but automates them through Python. This allows multiple users to be created quickly and consistently with little manual effort.
## Program User Operation
This program reads user data from an input file and processes each line to create user accounts, set passwords, and assign group memberships. The user provides an input file, and the script does everything else.

## Input File Format
This is the correct format for each line the input file: username:password:last:first:groups

## Command Excuction
1. To run the program, first ensure the script is executable: chmod +x create-users.py

2. Then execute the script using input redirection: ./create-users.py < create-users.input

3. To actually create users on the system, the script must be run with elevated privileges: sudo ./create-users.py < create-users.input

## "Dry Run"
A dry run allows the user to test the script without making any changes to the system. In this mode, the script executes all logic but does not run the system commands that create users or modify groups. Instead, it prints out the commands that would have been executed. This is reallyg helpful for verifying that the input file is correctly formatted and that the script behaves properly so that you don't have to go back and make changes after the code has been destroyed.
