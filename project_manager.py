
from genericpath import exists
from pathlib import Path
from tkinter import N

#first ask the user for for login information or to sign up
#need to check a file to see if the user info is there to compare
def contains_a_digit(string):
    if string == '':
        return False
    for ch in string:
        if ch.isdigit():
               return True
    return False   

ask_if_new_user = ''
while len(ask_if_new_user) != 1:
    print('New User? Y/N')
    print('Please input only one character')
    ask_if_new_user = input()
    
ask_if_new_user = ask_if_new_user.lower()
if ask_if_new_user == 'y':
    #ask to enter a username and password and save it onto users file
    new_username = ''
    new_password = ''
    while len(new_username) <  5:
       print('Enter a userName greater than 5 characters long (not case sensitive)')
       new_username = input()
    
    # TODO::Ask Why if I put these to while loops toguether with an and the code wont run properly
    while contains_a_digit(new_password) == False:
        new_password = ''
        while len(new_password) < 8:
            print('Enter a password greater than 8 characters long (case sensitive MUST have at least one digit)')
            new_password = input() 
    
    # TODO: make sure the user is happy with the credentials entered or try again if not
    # TODO: make sure the username is on capital letters so it is not case sensitive   
    my_file = Path('./password_manager_users.txt') 
    file_exists = exists(my_file)
    if file_exists == False:
        with open(my_file, 'a') as file:
            file.write(new_username +' ' + new_password + "\n")
    else:
        with open(my_file, 'a') as file:
            file.write(new_username +' ' + new_password + "\n")
else:
    #else ask the user yo input their credentials to acces their passwords
    #my_file is out of scope so i am declaring it again
    #read the file to get the list of users and put it into a list of tuples
    
    # TODO: Make sure the username is on capital letters so it is not case sensitive
    my_file = Path('./password_manager_users.txt')
    credentials_list = []
    with open(my_file, 'r' ) as file:
        for line in file:
            sub = line.split(' ')
            sub[1] = sub[1].rstrip()
            sub = tuple(sub)
            credentials_list.append(sub)
      

    # TODO: Make sure the username is on capital letters so it is not case sensitive

    user_and_pass_match = False
    while user_and_pass_match == False:
        username = ''
        password = ''
        print('Enter Your username and password \nUsername: ')
        username = input()
        print('Enter your password (case sensitive): ')
        password = input()
        
        
        #check if the username and password matches
        for list in credentials_list:
            if(username == list[0] and password == list[1]):
                    user_and_pass_match = True
                    break
            
 # TODO: open the users page and show the appropiate passwords
 # TODO: make sure the code and logic dont have any errors
 # TODO: 
    

        
            
    
    
    
    
