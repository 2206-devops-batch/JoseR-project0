
from Classes import *
import os

#Classes is where the classes for the user passwords are defined
# with a name(id) for easy search, username and password

are_credentials_ok = False

username = ''
password = ''


my_file = Path('password_manager_users.txt')
new_file_exists = exists(my_file)

ask_if_new_user = ''

if new_file_exists == False:
    print('No users exist please add a user')
else:
#first ask the user for for login information or to sign up
    ask_if_new_user = enter_Y_N_to_proceed('New User? Y/N: ')
#bool to check if the credentials are ok to pass    
# if the iser is new. add credentials making sure the username has at least 5 characters and 
# the password at least 8 and contain a number

    

if ask_if_new_user == 'Y' or new_file_exists ==False:
    while are_credentials_ok == False:
    #ask to enter a username and password and save it onto users file
        while len(username) <  5:
            print('Enter a userName greater than 5 characters long NOT spaces (not case sensitive)')
            username = input()
            if ' 'in username:
                username = ''
            
        # TODO::Ask Why if I put these to while loops toguether with an and the code wont run properly
        while contains_a_digit(password) == False:
            lenght = 0
            while lenght<8 :
                print('Enter a password greater than 8 characters long, have a digit') 
                print('and no spaces (case sensitive)')
                password = input()
                lenght = len(password)
                if ' ' in password:
                    lenght = 0            #Ask if the user is satisfied with the credentials entered. otherwise repeat process
        satisfied = ''   
        print('Your credentials are\nusername: ' + username + '\n' +'password: '+ password )
               
        while True :
            print()
            satisfied =  enter_Y_N_to_proceed('Are you satisfied? Y/N')
            if satisfied == 'Y':
                are_credentials_ok = True
                break
            else:
                username = ''
                password = ''
                break
    
    write_to_file('password_manager_users.txt', username.upper() +' ' + password )
else:
    #else ask the user yo input their credentials to acces their passwords
    #read the file to get the list of users and put it into a list of tuples
    #file exists no need to check
    my_file = Path('password_manager_users.txt')
    credentials_list = read_credentials_into_a_list(my_file)
     

    user_and_pass_match = False
    while user_and_pass_match == False:
        
        print('Enter Your username and password')
        username = input( 'Username (no spaces): ')
        username = username.upper()
        password = input('Enter your password (case sensitive no spaces): ')

        
        #check if the username and password matches
        for x in credentials_list:
            x = str(x[0]).split()
            if(username == x[0] and password == x[1]):
                user_and_pass_match = True
                print('here are your passwords\n')
                break
        if user_and_pass_match == False:    
            print('wrong username or password.\n')
            try_again = enter_Y_N_to_proceed('Try Again? Y/N: ')
            if try_again =='N':
               exit() 

#second part of the program is to display the appropiate user' usernames and passwords

my_file = Path('./'+username + '.txt') 
file_exists = exists(my_file)
# if file does not exists create a new file
if file_exists == False:
    while True:
        print ('There are no passwords to show.')
        accept = enter_Y_N_to_proceed('add Passwords? Y/N')
        #adding passwords
        more_passwords = True
        if(accept == 'Y'):
            while more_passwords == True:
                credentials = add_credentials()
                write_to_file('./'+username+'.txt', credentials.name+', '+credentials.username+', '+credentials.password)
                response = enter_Y_N_to_proceed('Add more passwords?: Y/N')
                if response == 'N':
                    more_passwords = False
                    break
            break
        else:
            print('program will exit now...')
            break
else:
    #read the file
    ceedential_list = []
    credential_list = read_credentials_into_a_list(username+'.txt')
    #print list
    print_credential_list(credential_list)
    
choice = ''
while choice != '4':
    print('Do you want to (choose a number):\n1. Add Credentials\n2. Remove Credentials\n3. Show credentials\n4. Exit')
    choice = input()
    if contains_a_digit(choice):
        if choice == '1':
            new_credentials = add_credentials()            
            write_to_file('./'+username+'.txt', new_credentials.name+', '+new_credentials.username+', '+new_credentials.password)
            print("credentials added!!")
        if choice == '2':
            file = Path(username+'.txt')
            file_exists = exists(file)
            if file_exists == True:
                credentials_list = read_credentials_into_a_list(username+'.txt')
                credentials_to_delete = input("please enter the name(ID) of the credentials to delete: ")
                for x in credentials_list:
                    if credentials_to_delete in x:
                        credentials_list.remove(x)
                        os.remove(username+'.txt')
                        for item in credentials_list:
                            write_to_file(username+'.txt', ', '.join(str(y)for y in item))   
                print('Credentials Removed!!')
            else:
                print('No credentials...')
            
        if choice =='3':
            #read the file
            
            file = Path(username+'.txt')
            file_exists = exists(file)
            if file_exists == True:
                credential_list = read_credentials_into_a_list(username+'.txt')
            #print list
                print_credential_list(credential_list)
            else:
                print('No credentials...')