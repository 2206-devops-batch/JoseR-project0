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
def enter_y_to_proceed(question):
    
    response = ''
    while(len(response) != 1):
        print(question)
        print('Please input only one character') 
        response = input()
        response = response.upper()
        if response == 'Y' or response == 'N':
            return response
        
def add_credentials():
    while True:
        name_for_password = input("Please enter name of new credentials(Id): ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        new_credentials = (password_manager(name_for_password, username, password))
        break
    return new_credentials