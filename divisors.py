""""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

def divisors(num) :
    return [i for i in range(1,num-1) if num%i == 0 ]

print('Give me a number greater than 0 and I will return a list of its divisors.')

while True :
    number = input('Number? ')
    if number.isnumeric() :
        number = int(number)
        if number >=1 :
            print(f'Here you have the divisor(s) of {number}: {divisors(number)}')
            break
    else :
        print('Please, give me a NUMBER.')
