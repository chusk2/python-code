def main():
    
    def amount_into_words(amount) :
        
        '''A function that takes an integer between 0 and 999
        as its only parameter, and returns a string containing
        the English words for that number.
        For example, if the parameter to the
        function is 142 then your function should
        return “one hundred forty two”.'''
        
        units = {0: 'zero', 1: 'one' , 2: 'two' ,
                 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                 7: 'seven', 8: 'eight', 9: 'nine'}
        
        tens = {10: 'ten' , 11: 'eleven' , 12: 'twelve',
                13:'thirteen', 14: 'fourteen' , 15: 'fifteen',
                16 : 'sixteen', 17: 'seventeen', 18: 'eighteen',
                19 : 'nineteen', 20 :'twenty' , 30:'thirty',
                40:'forty', 50 : 'fifty', 60: 'sixty',
                70:'seventy', 80: 'eighty', 90: 'ninety'}
        
        ### one-cipher number 0 --> 0
        
        if amount >= 0 and amount <= 9 :  # one digit
            hundreds_word = None
            tens_word = None
            units_word = units[amount]
                
        ### two-cipher numbers 10 --> 99
        
        elif amount >= 10 and amount <= 99 :  # two digits
            
            ### numbers like 10,11,12,13,20,30,...
            if amount in tens.values() :
                
                hundreds_word = None
                tens_word     = tens[amount]
                units_word    = None
            
            ### numbers like 33,45,78,...
            else :
            
                # divide the two ciphers number into tens and units
                amount_string = str(amount)  
                unit_cipher   = int(amount_string[1])
                tens_cipher   = int(amount_string[0]) * 10
                
                hundreds_word = None
                tens_cipher   = tens[ tens_cipher ]
                units_word    = units [ unit_cipher ]
        
        ### three-cipher numbers 100 --> 999
            
        else :
        
            ### divide the three ciphers number into hundreds, tens and units
            
            # transform number into string so it's easier to take out their ciphers
            amount_string   = str(amount)  
            hundreds_cipher = int(amount_string[0])
            tens_cipher     = int(amount_string[1])
            units_cipher    = int(amount_string[2])
            
            hundreds_word = units[hundreds_cipher]
            
            ### form the tens and units words
            
            # check if tens range from 13 to 19 or in {20,30,40,...}
            # example: 210, 211, 212, 213, 320, 450, 520,...
            
            # use the last 2 ciphers and check if they belong
            # to range 10-19 or in {20,30,40,...}
            last_two_ciphers = int(amount_string[1:])
            if last_two_ciphers in tens :
                
                tens_word   = tens[last_two_ciphers]
                units_word  = None
            
            # check if there is no tens cipher
            # example: 101, 304, 508
            elif tens_cipher == 0 :
                
                tens_word  = None
                units_word = units[units_cipher]
            
            # translate tens into words
            # example: 345, 567, 389,...
            else :  
                
                # redefine the tens cipher multiplying by 10
                tens_cipher *= 10
                tens_word  = tens[tens_cipher]
                units_word = units[units_cipher]
            
        ### words
        
        # one-cipher number
        if (not hundreds_word) and (not tens_word):
            words = units_word
        
        # two-cipher number
        elif not hundreds_word :
            
            # 10, 20, 30, ... OR {11-->19}
            if not units_word :
                words = tens_word
            
            # 21,22,23,... --> 99
            else:
                words = tens_word + '-' + units_word
        
        # three-cipher number
        else :
            
            # only hundreds
            if (not tens_word) and (not units_word) :
                words = hundreds_word + ' hundred'
            
            # hundreds and units
            elif not tens_word:
                words = hundreds_word + ' hundred and ' + units_word
            
            # tens belonging to {10 --> 19}, 20, 30, ...
            elif not units_word :
                words =  hundreds_word + ' hundred and ' + tens_word
            
            # three ciphers 123, 234, 567, ...
            else :
                words = hundreds_word + ' hundred and ' + tens_word + '-' + units_word
        
        ### finally, print the amount using words
        
        return words
    
    amount = int( input('Give me a number: ') )
    print( amount_into_words(amount) )
    

if __name__ == '__main__' :
    
    main()
        
