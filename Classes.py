from genericpath import exists
from pathlib import Path
class password_manager:
    
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        
    def __str__(self):
        return f'{self.name} {self.username} {self.password}'
    
def contains_a_digit(string):
    if string == '':
        return False
    for ch in string:
        if ch.isdigit():
               return True
    return False   
def write_to_file(path, thing_to_add):
    my_file = Path(path) 
    file_exists = exists(my_file)
    #check if the file exists write the info otherwise append it so old info dont get erased
    # make sure username gets capitalized so it is case insensitive
    if file_exists == False:
        with open(my_file, 'w') as file:
            file.write(thing_to_add + '\n')
    else:
        with open(my_file, 'a') as file:
            file.write(thing_to_add + "\n")
            
def enter_Y_N_to_proceed(question):
    response = ''
    while(len(response) != 1):
        print(question)
        print('Please input only one character') 
        response = input()
        response = response.upper()
        if response == 'Y' or response == 'N':
            return response
        
def add_credentials():
    name_for_password = ' '
    username = ' '
    password = ' '
    while ' ' in name_for_password:
        name_for_password = input("Please enter name of new credentials(Id) (no spaces): ")
    while ' ' in username:
        username = input("Enter Username (no spaces): ")
    while ' ' in password:
        password = input("Enter Password (no spaces): ")
        
    new_credentials = (password_manager(name_for_password, username, password))
        
    return new_credentials
def read_credentials_into_a_list(path):
    credential_list = []
    my_file = Path(path)
    file_exists = exists(my_file)
    if file_exists == True:
        with open(my_file ) as file:
            for line in file:
                if(line != '\n'):
                    sub = line.split(',') 
                    sub[len(sub)-1] = sub[len(sub)-1].strip()
                    sub = tuple(sub)
                    credential_list.append(sub)
            return credential_list    
        
def print_credential_list(credentials):
    for x in credentials:
        print('ID: '+ x[0]+', Username: '+x[1]+', Password: '+x[2])  