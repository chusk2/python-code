


def main() :

    def num_into_words (num) :


        ### Define the words for the ciphers

        units = {0 : 'zero', 1 : 'one', 2 : 'two' , 3: 'three' ,
                4: 'four', 5: 'five' , 6: 'six' , 7: 'seven' ,
                8: 'eight', 9: 'nine' }
                
        tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty' , 50: 'fifty',
                60: 'sixty', 70: 'seventy', 80: 'eighty' , 90: 'ninety' }

        num_str = str(num)

        unit_w=''     # word for the units
        ten_w=''      # word for the tens
        hundred_w=''  # word for the hundreds

        unit_f=''     # cipher for the units
        ten_f=''      # cipher for the tens
        hundred_f=''  # cipher for the hundreds

        ### example: 1,2,3...,9
        if len(num_str) == 1 :
            
            unit_f = num  # num is one-figure number
            unit_w = units[unit_f]
            word = unit_w

        ### two-figure numbers
        elif len(num_str) == 2 :
            
            ### example: 10,11,12,...,20,30,...,90
            if num in tens.keys() :
                
                ten_w = tens[num]
                word  = ten_w
                   
            ### example: 21,22,45,67,...
            else:
                unit_f = int(num_str[1])
                ten_f  = int(num_str[0]) * 10
                unit_w = units[unit_f]
                ten_w  = tens[ten_f]

                word   = ten_w +'-' + unit_w

        ### three-figure numbers
        else:

            ### example: 100, 200, 300 or 350,140,860
            if num_str[1] == '0' :

                ### example: 100, 200, 300
                if num_str[1:] == '00' :
                    hundred_f   = int(num_str[0])
                    
                    hundred_w   = units[hundred_f]

                    word        = hundred_w + ' hundred'

                ### example 101, 102, 103, 250
                else:
                    hundred_f = int(num_str[0])
                    unit_f    = int(num_str[2])
                    
                    hundred_w = units[hundred_f]
                    unit_w    = units[unit_f]

                    word      = hundred_w + ' hundred and ' + unit_w
               
            ### example: 310, 420, 530, 670
            
            # int(num_str[1:])
            # take the last the last 2 figures
            # of a three-figure number and transform
            # them into an integer to check if in tens dict values
            elif int(num_str[1:]) in tens :
                
                hundred_f   = int(num_str[0])
                # redefine the tens to be multiple of 10
                tens_f      = int(num_str[1]) *10
                    
                hundred_w   = units[hundred_f]
                ten_w       = tens[tens_f]

                word        = hundred_w + ' hundred and ' + ten_w

            ### example: 346, 785, 284
            else:
                hundred_f   = int(num_str[0])
                tens_f      = int(num_str[1]) * 10
                unit_f      = int(num_str[2])

                hundred_w   = units[hundred_f]
                ten_w       = tens[tens_f]
                unit_w      = units[unit_f]

                word = hundred_w + ' hundred and ' + ten_w +'-' + unit_w
    
        return word
    ### end of function num_into_word ###
    
    ask = 'Give me a number from 0 to 999: '
    
    while True:
    
        num = input('Give me a number from 0 to 999: ')
        if num == '' : break
        else :
            num = int(num)
            print( num_into_words (num) )

if __name__ == '__main__' :

    main()

