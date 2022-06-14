
from genericpath import exists
from pathlib import Path
import Classes
#Classes is where the classes for the user passwords are defined
# with a name(id) for easy search, username and password

 

#need to check a file to see if the user info is there to compare

# This class goes trough a string and return true if it contains a digit. false otherwise
def contains_a_digit(string):
    if string == '':
        return False
    for ch in string:
        if ch.isdigit():
               return True
    return False   

#first ask the user for for login information or to sign up
ask_if_new_user = ''
while True:
    print('New User? Y/N')
    print('Please input only one character')
    ask_if_new_user = input()
    ask_if_new_user = ask_if_new_user.upper()
    if ask_if_new_user == 'Y' or ask_if_new_user == 'N':
        break

#bool to check if the credentials are ok to pass    
are_credentials_ok = False
new_username = ''
new_password = ''
# if the iser is new. add credentials making sure the username has at least 5 characters and 
# the password at least 8 and contain a number
if ask_if_new_user == 'Y':
    while are_credentials_ok == False:
    #ask to enter a username and password and save it onto users file
        while len(new_username) <  5:
            print('Enter a userName greater than 5 characters long (not case sensitive)')
            new_username = input()
            
            # TODO::Ask Why if I put these to while loops toguether with an and the code wont run properly
            while contains_a_digit(new_password) == False:
                new_password = ''
                while len(new_password) < 8:
                    print('Enter a password greater than 8 characters long (case sensitive MUST have at least one digit)')
                    new_password = input()
            #Ask if the user is satisfied with the credentials entered. otherwise repeat process
            satisfied = ''   
            print('Your credentials are\nusername: ' + new_username + '\n' +'password: '+ new_password +'\nAre you satisfied? Y/N')
        
            while True :
                print('Please input only one character Y/N')
                satisfied = input()
                satisfied = satisfied.upper()
                if satisfied == 'Y':
                    are_credentials_ok = True
                    break
                else:
                    new_username = ''
                    new_password = ''
                    break
    
    
    #Now that the user has his credentials, they get saved on the "password_manager_users"
    my_file = Path('./password_manager_users.txt') 
    file_exists = exists(my_file)
    #check if the file exists write the info otherwise append it so old info dont get erased
    # make sure username gets capitalized so it is case insensitive
    if file_exists == False:
        with open(my_file, 'w') as file:
            file.write(new_username.upper() +' ' + new_password + "\n")
    else:
        with open(my_file, 'a') as file:
            file.write(new_username.upper() +' ' + new_password + "\n")
else:
    #else ask the user yo input their credentials to acces their passwords
    #read the file to get the list of users and put it into a list of tuples
    my_file = Path('./password_manager_users.txt')
    credentials_list = []
    with open(my_file ) as file:
        for line in file:
            sub = line.split(' ')
            sub[1] = sub[1].rstrip()
            sub = tuple(sub)
            credentials_list.append(sub)
      

    user_and_pass_match = False
    while user_and_pass_match == False:
        
        username = ''
        password = ''
        print('Enter Your username and password \nUsername: ')
        username = input()
        username = username.upper()
        print('Enter your password (case sensitive): ')
        password = input()
        
        
        #check if the username and password matches
        for list in credentials_list:
            if(username == list[0] and password == list[1]):
                    user_and_pass_match = True
                    print('here are your passwords\n')
        if user_and_pass_match == False:    
            print('something went wrong please try again or exit and create a new user') 
               
# TODO: open the users page and show the appropiate passwords            
my_file = Path('./'+username + 'txt') 
file_exists = exists(my_file)
if file_exists == False:
    
    while True:
        print('There are no passwords to show. add Passwords? Y\N') 
        accept = input()[0]
        accept = accept.upper()
        if(accept == 'Y'):
            break
        else:
            print('Quit? Y/N')
        
                            
else:
    with open(my_file, 'r') as file:
        for line in file:
            lines = file.readlines()