def position(alphabet):
    lowercase_alphabet = [ chr(code) for code in range(97,123) ]

    position = lowercase_alphabet.index(alphabet) + 1
    return position

print( position('a') )