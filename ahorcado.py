words=['perro','gato','huron','murcielago']
#,'cobaya']

#import random integer module
from random import randint as rnd

# function to choose a word
def choose () :
    chosen_word =words[ rnd (0,len(words) - 1 ) ]
    return chosen_word


chosen_word=choose()

length_word=len(chosen_word)
hidden_letters = ['*' for i in chosen_word ]
underscore = ['_' for i in chosen_word ]

# for i in range(length_word) :
#     print('*' , end=' ') if i != (length_word - 1) else print('*', end='\n')
    
def print_underscores() :
    
    print('\n')
    
    for i in range(length_word):
        print(hidden_letters[i] , end=' ') if i != (length_word - 1)  else print(hidden_letters[i], end='\n') 

       
    for i in underscore :
        print('_' , end=' ') if i != (length_word - 1) else print('_', end='\n')
    
    print('\n')

#print("The chosen word is" ,chosen_word )

counter = 0 # counter for the correct letters
fails = 0 # maximum of 6 fails

while counter <= length_word and fails <= 6 : # ask again if there aren't enough correct letters and fails are under 7
    
    print_underscores()
    if counter == length_word : break
    
    letter = input ('Elige una letra: ')
    
    if letter == '0' :
        print('Aborted game.')
        break # abort game entering zero number
    
    if letter in chosen_word : # if there's a match
        
        # get all the positions of the match letter in chosen word
        for i,j in enumerate(chosen_word) : # creates a double array with positions and elements
            
            if letter == j : # if the given letter is a concurrence in chosen word, append its position to a list
                hidden_letters[i] = letter # assign the letter to its correspondend position in the hidden word
                counter += 1 # add one correct answer to the counter
                
    else :
        fails += 1 # if the given letter wasn't a match, then add 1 fail to the fail counter
        print('Fails:',fails)
        
# two ways of finishing the game.
if fails > 6 :
    print('You lost the game. The word was:',chosen_word)

if counter == length_word :
    print('Congratulations! You won the game!')


