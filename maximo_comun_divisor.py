def mcd (a,b) :
    if b != 0 :
        
        if a < b :
            a = b
            b = a
        
        r = a % b
        
        while r != 0 :
            a = b
            b = r
            r = a % b
    return b


print(f'El máximo común denominador de 45 y 27 es: {mcd(148,64)}')