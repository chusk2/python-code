# función chr() me devuelve el carácter ASCII cuyo código le suministro
letra_ASCII = chr(91)

# función ord() me devuelve el código ASCII de un determinado símbolo
codigo_ASCII = ord('A')

lowercase_alphabet = [ chr(code) for code in range(97,123) ]
uppercase_alphabet = [ chr(code) for code in range(65,91) ]

# print(lowercase_alphabet)
# print(uppercase_alphabet)

letter = input('Give me a letter to find out its position in alphabet: ')

if letter.isupper() :
    position = uppercase_alphabet.index(letter)
    print(f'Your letter {letter} is in position: {position + 1}')

elif letter.islower() :
    position = lowercase_alphabet.index(letter)
    print(f'Your letter {letter} is in position: {position + 1}')



