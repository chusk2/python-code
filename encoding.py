'''Encrypt one string using a dictionary to replace
certain letters by numbers.'''

### I have used a dictionary just to practice
### Using the replace string method would be easier and shorter
transcription = {'a' : '4', 'b' : '8',
                 'e' : '3', 'l' : '1',
                 'o' : '0', 's' : '5',
                 't' : '7'}

while True:
    text = input('Enter a string to be encrypted: \n')
    #  To quit just press enter without entering anything
    if text == '' : break  
    encrypted_text = ''    
    for letter in text :

        if letter in transcription :
            letter = transcription[letter]

        encrypted_text += letter
    print(f'The original message was: {text}')
    print(f'The encrypted message is: {encrypted_text}\n')
      
