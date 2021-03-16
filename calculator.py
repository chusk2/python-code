def main() :
    
    while True :
        
        print('Choose an operation to calculate its result: ')
        print('1 for addition')
        print('2 for substraction')
        print('3 for multiplication')
        print('4 for division')
        print('5 for powers')
        print('\nJust hit Enter with no option to exit')
        
        option = input('\nOperation: ')
        
        if option == '' :
            break
               
        operation = int(option)
        
        if operation not in [1,2,3,4,5] :
            print('Option not valid. Please, choose again.')
            continue
        
        if operation == 1 :
            print(f'\nResult of the ADDITION is: { addition() }\n')
        
        elif operation == 2 :
            print(f'\nResult of the SUBSTRACTION is: { substraction() }\n')
        
        elif operation == 3 :
            print(f'\nResult of the MULTIPLICATION is: { multiplication() }\n')
        
        elif operation == 4 :
            print(f'\nResult of the DIVISION is: { division() }\n')
        
    
def addition() -> float :
    
    print('ADDITION SELECTED')
    print('Enter numbers to be added. Enter no value to finish and get result.\n\n')
    counter = 0
    result = 0
    while True :
        number = input('Number: ')
        
        if number == '' and counter in [0,1] :
            return '\nNo addition was made!'
        
        else :
            number = float(number)   
            result += number
            counter += 1
    
    return result

def substraction() -> float :
    
    print('SUBSTRACTION SELECTED')
    print('Enter numbers to be substracted. Enter no value to finish and get result.\n\n')
    counter = 0
    result = 0
    while True :
        number = input('Number: ')
        
        if number == '' and counter in [0,1] :
            return '\nNo substraction was made!'
        
        elif number == '' :
            break
        
        else :
            number = float(number)   
            if counter == 0 :
                result = number
                counter += 1
            else :
                result -= number
                counter += 1

def multiplication() -> float :
    
    print('MULTIPLICATION SELECTED')
    print('Enter numbers to be multiplicated. Enter no value to finish and get result.\n\n')
    counter = 0
    result = 0
    while True :
        number = input('Number: ')
        
        if number == '' and counter in [0,1] :
            return 'No multiplication was made!'
        
        elif number == '' :
            break
        
        else :
            number = float(number)
            if counter == 0 :
                result = number
                counter += 1
            else :
                result *= number
                counter += 1
    return result


def division() -> float :
    
    print('DIVISION SELECTED')
    print('Enter numbers to be multiplicated. Enter no value to finish and get result.\n\n')
    counter = 0
    result = 0
           
    for i in range(2) :
            if i == 0 : # ask for the dividend
                dividend = input ('Enter the dividend: ')
                if dividend == '' :
                    return 'No division was made!'
                else :
                    a = float(dividend)
            
            else : # dividen has been already entered and now the divisor is asked to be entered
                
                while True : # keep on asking for divisor until valid value is entered
                    
                    divisor = input ('Enter the divisor: ') # ask for divisor
                    
                    if divisor == '' :
                        return 'No division was made!'
                    
                    else :
                        
                        divisor = float(divisor) # turn input into float number
                        
                        if divisor == 0 : # cannot divide by zero
                            print('Cannot divide by zero!!')
                            continue # restart the while loop and ask again
                        
                        else : # it was a valid divisor
                            b = divisor
                            break
    return a/b


if __name__ == '__main__' :
    main()