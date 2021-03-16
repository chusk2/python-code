def is_palindrome(string) :

    ### ascii ordinals for letters from A to Z and a to Z
    # ord('A') = 65
    # ord('Z') = 90
    # ord('a') = 97
    # ord('z') = 122

    palindrome      = False
    string          = string.lower()
    only_letters    = ''

    ### clean string from non alphabetic characters
    for letter in string :
        # check if its an alphabetic character between 'a' and 'z'
        #if ord(letter) >= 97 and ord(letter) <= 122 :
        if letter.isalpha() :
            only_letters += letter    

    # string_reversed = ''

    string_reversed = only_letters[::-1]
    
    # for i in only_letters[::-1] :  # traverse only_letters backwards
    #     string_reversed += i
    """ only_letters_reversed = only_letters.copy()
    only_letters_reversed.reverse() """

    if only_letters == string_reversed :
        palindrome = True

    return palindrome

string = input('Enter a string to check whether is a palindrome.\nString: ')

print(is_palindrome(string))
