#!/usr/bin/env python3

### Martes 6 Oct 2020

def is_prime(n) :
    '''Checks whether n is a prime number.
    Divides n by all the numbers below it. If n is divisible by a number larger than 1,
    n is not a prime number.'''
    
    prime = True  # Initially is not prime
    
    if n == 1 :
        prime = False
    
    elif n == 2 or n == 3 : # 2 and 3 are prime numbers
        prime = True
    
    else :  # all the numbers are divisible by 1, so start to check from 3
        
        for i in range(3,n) :  # check divisibility from 3 until previous number to n
            
            if n % i == 0 :  # if is divisible, it's remain will be zero
                prime = False
                break
    
    return prime

def times_divisible(a,b) :  # how many times a is divisible by b
    ''' If a is divisible by b, calculate how many times is possible to do this.
    Divide the quotient of the division recursively by b until the remainder is not 0.
    Counter variable times stores the times a was able to be divided by b.'''
    
    if a % b == 0 :
        divisible = True
        times = 0
        
        while  a % b == 0 : # repeat until a is no more divisible by b
            times += 1
            a = a / b
            
        return times
    
    else :
        divisible = False
        return divisible
         
def list_of_primes (n) :
    ''' Finds all the prime numbers below the given number n. Checks if it is prime using
    function is_prime(). When it finds a prime number below n, it stores it in the list primes.'''
     
    primes=[]  # store the prime numbers below the given number
    
    for i in range(2,n) :  # check if is number for all numbers below given number
        if is_prime(i) :
            primes.append(i)  # add it to the list
    
    return primes

def get_factorization (n) :
    '''Create a dictionary: {key:value} ---> {prime number : times n is divisible by this prime number }
    To create this dictionary, check all the prime numbers below n and add to the dict only those who are divisible by n.'''
    
    factorization={}
    primes = list_of_primes(n)
    
    for i in primes :  # create the factorization of given number in the form of a dictionary
        if n % i == 0 :  # add it to the list only if n is divisible by this prime number (i)
            times = times_divisible(n,i)  # find out how many times n can be divided by i
            factorization.update( {i : times } )
    
    return factorization

def print_factorization (n , factorization ) :
    ''' Print in a formated way the factorized descomposition of number n'''
    
    print(f'\nLa factorización del número {n} es: ', end='')
    factors = list( factorization.items() )  # transform into list the items of the dictionary to handle easier
    for f in factors :
        
        if f != factors[-1] :
            
            ## If factor only appears once, don't write factor^1 but simply factor
            ##  Add ' · ' between factors except for the last factor
            print (f'{f[0]}^{f[1]}' , end=' · ') if f[1] != 1 else print (f'{f[0]}' , end=' · ')
        
        else :
           print (f'{f[0]}^{f[1]}') if f[1] != 1 else print (f'{f[0]}')
                    

### Star to ask for a number to be factorized ###

number = 1

while number :
    number = int ( input('\nIntroduce un número para factorizar. Introduce 0 para finalizar.\nNúmero: ') )
    
    if number == 0 :
        break  # terminate the program when 0 is entered
    
    elif number < 0 :
        print('¡Introduce un número positivo!')  # no negative numbers allowed
        continue
    
    else :  # an allowed number is entered
        if is_prime(number) : # check if number is prime. If so, say it and start over
            print(f'El número {number} es primo y no puede factorizarse.')
            continue
        
        else :  # number is not prime and therefore can be factorized
            factorization = get_factorization(number)
            print_factorization(number, factorization)
            continue
        
