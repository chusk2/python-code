from random import randint
from os import system, name
from time import sleep


def clear():

    # for windows
    if name == 'nt':
        clear_command = system('cls')

# for mac and linux(here, os.name is 'posix')
    else:
        clear_command = system('clear')

# sleep for 2 seconds after printing output
    sleep(0.2)
    return clear_command


def hangman():
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    wordlist = ['pato',
                'perro',
                'gato',
                'huron',
                'tortuga',
                'cobaya']
    word = wordlist[randint(0, len(wordlist)-1)]
    print(word)
    # create a list containing the letters of the chosen word
    # letters_list = list(chosen_word)
    # # create a set of unique letters in word
    # unique_letters = set(letters_list)
    # # create a dict with letters in chosen word as keys
    # letters_dict = dict.fromkeys(unique_letters)
    # # populate dict with letter's count as values
    # for letter in unique_letters:
    #     letters_dict[letter] = letters_list.count(letter)
    # # create a dict for correct entered letters
    # correct_entered_letters = dict.fromkeys(unique_letters,0)
    # fails counter

    fails = 0
    invalid_letters = set()
    # Letters layout
    clear()  # clear screen
    # print the gaps for letters to guess

    guessed_ones = [u'\u2591' for i in range(len(word))]

    def check(right_word, entered_letter, blocks):
        for index, value in enumerate(right_word):
            if entered_letter == value:
                blocks[index] = value
        if blocks == list(word):
            print(f'Congratulations!. The word was "{word}". You '
                  f'guessed it!')
            return 1  # return code 1 to finish game

        return blocks

    def print_guessed_ones(block):
        print('\n')
        for i in block:
            print(i, end=' ')
        print('\n')
    def print_wrong(invalids):
        print('Wrong letters:', end=' ') if len(invalids) != 0 else \
            print('')
        for i in invalids:
            print(i, end=' ')
        print(f'\nRemaining attempts: {7 - fails}')

    # start guessing game
    # maximum of 4 fails

    while fails < 7:

        print(HANGMANPICS[fails - 1]) if fails > 0 else print('')
        print_wrong(invalid_letters)
        print_guessed_ones(guessed_ones)
        # ask a valid letter character
        while True:

            letter = input('Type a letter included in the word to guess: ')

            if letter.isalpha() and len(letter) == 1:
                break

            else:
                if not letter.isalpha():
                    print('Please, type only letters...\n')
                    clear()
                    continue
                elif len(letter) != 1:
                    print('Please, type only ONE letter...\n')
                    clear()
                    continue

        if letter in word:
            guessed_ones = check(word, letter, guessed_ones)
            # word was finally guessed
            if guessed_ones == 1:
                break

            # Wrong Letter
        else:
            invalid_letters.add(letter)
            fails += 1
            if fails == 7:
                print(f'You lost the game. The word to guess was: '
                      f'{word}')
            else:
                print(f"Ouch! \"{letter}\" isn't in the word to guess. "
                      f"Fails: {fails}")


if __name__ == "__main__":
    hangman()
