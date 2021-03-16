letters = {}
string = input('Frase para contar letras: ')

counter = 0

letters_in_string = list(string)


for letter in letters_in_string :
    letters.update({letter : string.count( letter ) })

ordered_letters_list = list( sorted(letters_in_string ) )
print(ordered_letters_list)

# for letter,times in letters.items() :
#     print(f'La letra {letter} se repite {times} en la frase.')