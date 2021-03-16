""" Kata de codewars.com: https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python """

def flip(d, a):
    # Do some magic
    
    # el argumento d me indica la dirección a la que se mueven los bloques
    # el argumento a me da las cantidades de bloques que hay en cada columna
    # a es una lista de números que tengo que ordenar de mayor a menor (si d = L)
    # o de menor a mayor (si d = R)
    
    # si se cumple la condición de que d es igual a L, ordénalos de mayor a menor
    if   d == 'L' :
        
        # ordena la lista en orden de mayor a menor
        a.sort( reverse = True)
        
        # el comando return se utiliza para indicarle a la función que devuelva un determinado elemento
        # en este caso le indicamos que devuelva la lista ordenada en un sentido u otro
        return a
    
    elif d == 'R' :
        
        # ordena la lista en orden de menor a mayor
        a.sort()
        
        # devuelve la lista reorganizada
        return a

    ## Ejecuta el programa si quieres ver cómo funciona:

print('\nResultado esperado: [1, 2, 2, 3]')

print( f'\n{ flip( "R", [3, 2, 1, 2] ) } ' )

print('\nResultado esperado: [5, 5, 4, 3, 1]')

print(f'\n{flip("L", [1, 4, 5, 3, 5])}\n')