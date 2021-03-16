"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

### https://cybernews.com/best-password-managers/how-to-create-a-strong-password/

### lowercase alphabet ASCII codes range from 97 ('a') to 122 ('z')
### uppercase alphabet ASCII codes range from 65 ('A') to 90 ('Z')
### numbers ASCII codes range from 49 ('1') to 57('9')
### symbols = ['!','¡','@','#','$','&','/','?','¿','*','>','<','"'","'",'(',')','=',';','[',']','^','{','}','~','|']

from random import randint

def pass_gen (length) :
    uppercase = [chr(i) for i in range(65,91)]
    lowercase = [chr(i) for i in range(97,123)]
    numbers = list( range(10) )
    symbols = ['!','¡','@','#','$','&','/','?','¿','*','>','<','(',')','=',';','[',']','^','{','}','~','|',"'",'"']
    ## create a dictionary containing 4 types of elements for the password
    elements_password = {1:uppercase,2:lowercase,3:numbers,4:symbols} 
    
    password = ''
    
    for i in range(length) :
        
        ## choose a type of character
        type = randint(1,4) 
        ## once one type of element of the password is chosen,
        ## tell me its length to set the range of values to choose from
        length_of_type = len(elements_password[type])
        ## add a random element within the chosen type
        password += str( elements_password[type][randint(0,length_of_type-1)] )
    
    return password

while True :
    strength = int( input('\nPassword strength: ') )
    if strength < 6 :
        print('Your password would be too weak. Choose a longer password.')
        continue
    print(f'\nYour new password is: {pass_gen(strength)}')


