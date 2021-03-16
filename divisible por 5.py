from random import randint as rnd
counter = 0
while counter <= 10 :
    
    num = rnd(1,100)
    if num % 5 == 0:
        print(f'El número {num} es divisible por 5. Se acabó.')
        break        
    else :
        print(num)
        counter += 1
    