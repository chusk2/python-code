
def factorize(num) :
    dividend = num
    factors = {}
    
    for i in range(2,num-1) :
        times = 0
        if dividend == 1 : break  # If the remaining dividend equals 1, we have finished
        
        while dividend % i == 0 :
            times += 1
            dividend = dividend / i
        ### Append the factor i powered to 'times'
        ### Append it only if times is not equal to zero
        if times != 0:
            factors[i]=times
    
    return factors

num = int( input('Number to factorize: ') )
factors=factorize(num)



if not factors.keys() :  # number is a prime number if factors dictionary is empty
    print(f'{num} iS a prime number.')
else :
    ### num is not a prime number
    
    ### transform the result of dict.keys into a list so we
    ### can check if we have reached the last prime factor
    last_factor = ( list( factors.keys() ) )[-1]
    print(f'\nThe decomposition of {num} is:',end=' ')

for k,v in factors.items() :
    
    ### Do not print the exponent if it is one
    if v != 1 :
        print(f'{k}^{v}' ,end=' · ') if k != last_factor else print(f'{k}^{v}')
    ### Add the '·' character to separate the factors
    else:
        print(f'{k}' ,end=' · ') if k != last_factor else print(f'{k}')
print('\n')