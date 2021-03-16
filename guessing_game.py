"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

from random import randint as rndint

# define the function to generate a number and check your guesses
def guessing_game() :

    """Generates a number between 1 and 100 and then ask for you to guess
    it. If you do not guess it, it will give you hints asking you for a higher or lower guess.
    
    return codes:

    return 'win'        ---> you guessed the num. One point for you
    return 'no play'    ---> you have quitted before even trying
    return 'finished'   ---> you played but want anymore
    return 'surrender'  ---> you were not able to guess but want to try again
    
    """

    num_to_guess = rndint(1,100) # choose a num to guess
    
    if games_played == 0 :
        print('\nI have chosen a number between 1 and 100. Try to guess it.')
        print('Type "exit" to finish or "quit" to try leave the round and try with another number.\n')
    
    else:
        print('\nYou know the rules. Guess again the number I have thought of.\n')

    attemps = 0

    while attemps <= 5: 

        guess= input('What\'s the number? ')

        # check if it is a valid input
        # you do not want to keep on playing
        if guess == 'exit' :
            
            # if you have played not even once
            if not games_played : 
                return 'no play' # you did not played even once

            # you have played at least once but now you quit
            else :
                return 'finished'
                
        # you quit guessing but try another round            
        elif guess == 'quit' :
            # finish this round but repeat once again
            return 'surrender'
        
        # the input is neither a numeric one nor exit or quit
        if not guess.isnumeric() :
            print('Invalid number. Try again.')
            continue
        
        # the given number was out of range
        elif int(guess) <1 or int(guess) >100 :
            print('Number out of range. Enter a number between 1 and 100. Try again.')
            continue
        
        # ups, too low
        elif int(guess) > num_to_guess :
            print(f'\nYour guess was {guess}. Try a lower number...\n')
            attemps += 1
            print(f'You have {5-attemps} attemps left.')
            continue
        
        # ups, too high
        elif int(guess) < num_to_guess :
            print(f'\nYour guess was {guess}. Try a higher number...\n')
            attemps += 1
            print(f'You have {5-attemps} attemps left.')
            continue
        
        # you guessed it!
        else :
            print('\nCongrats! You guessed the number! One point for you.')
            return 'win' # you have won the round
    print('You lost the game. Nice try.')
    return 'finished'

### Initial assignments
    
valid_answers = ['Y','Yes','yes','y','YES','N','No','no','NO','n']
games_played = 0 # initially you have not played yet
points = 0 # initial score

###

print('Welcome to the guessing game.')
print("""These are the rules of the game:
I will think of a number between 1 and 100 and you have to guess it.
If you fail, I will give you some hints telling you if your guess should be higher or lower.
If you do not guess my number within a maximum of 5 attemps, you lose.
Good luck!""")

# Keep on asking till a valid answer is given
while True: # ask if want to play unless ask is set to False
    
    question = '\nDo you want to play?\nType Yes or No: ' if games_played == 0 else '\nDo you want to play again?\nType Yes or No: '
    play = input(question)   
    # check if a valid answer was given. If not, repeat question
    if play not in valid_answers: 
        print('Invalid answer.')
        continue # repeat the question
    
    # answer was negative
    elif play in ['N','No','no','NO','n'] : 
        
        if games_played == 0 :
            print('Sorry we haven\'t played! I hope next time we can have some fun! See you then!')

        elif games_played != 0 and points == 0 :
            print('Sorry you didn\'t guess any number. I hope you do it better next time!')
            
        else :
            print(f'Your score is {points} points from {games_played} games. I hope you\'ve had a great time!')
        
        break
        
    else:
        
        # if you want to play, let's do it
        # guessing_game returns different results. See function docstring

        result = guessing_game()
        
        if result == 'win' :
            points += 1
            games_played += 1

        elif result == 'no play' :
            print('Sorry we haven\'t played! I hope next time we can have some fun! See you then!')
            break

        elif result == 'finished' :
            
            games_played += 1

            if points == 0 :
                print('Sorry you didn\'t guess any number. I hope you do it better next time!')
                break
            
            else :
                print(f'Your score is {points} points from {games_played} games. I hope you\'ve had a great time!')
                break
        
        elif result == 'surrender' :
            print('Let\'s go again! You know, have to guess the number. Remember: must be between 1 and 100.')
            # try again
            result = guessing_game()
            