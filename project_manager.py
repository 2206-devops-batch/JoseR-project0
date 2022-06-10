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
    
    while contains_a_digit(new_password) == False:
        new_password = ''
        while len(new_password) < 8:
            print('Enter a password greater than 8 characters long (case sensitive MUST have at least one digit)')
            new_password = input() 
       
 
       
           

        
            
    
    
    
    
