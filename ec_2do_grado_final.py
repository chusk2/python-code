"""Programa para ecuación de segundo grado"""

# importa una librería con funciones adicionales
import math

print('\n')
print('Programa para cálculo de ecuaciones de 2do grado.')
print('\n')
print('Las ecuaciones son del tipo: ax^2 + bx + c = 0')

a = input('\nDame el coeficiente "a" : ')
b = input('\nDame el coeficiente "b" : ')
c = input('\nDame el coeficiente "c" : ')



# transformamos los números en forma de texto en números en forma numérica

# a,b y c ahora son números decimales
a = float (a)
b = float (b)
c = float (c)
# guardo los coeficientes en una lista
coeficientes = [a,b,c]

# voy a comprobar si cada uno de los coeficientes es decimal o no

# el ciclo for significa: hazle lo de dentro del bloque
#  a cada uno de los elementos de la lista coeficientes

# creo una nueva lista de coeficientes con su forma final
# el método .append() añade elementos a una lista

coef_final =[]
for numero in coeficientes :
    partes_numero = math.modf(numero)
    if partes_numero[0] == 0 :
        coef_final.append( int(numero) )
    else :
        coef_final.append( numero )

print(coef_final)

a = coef_final[0]
b = coef_final[1]
c = coef_final[2]

# si el número no es con decimales, transfórmalo a entero
# para saber si es con decimales, le pido que me de su parte decimal
# si la parte decimal es 0, es que el número es entero

# el método .modf() me devuelve la parte entera y la parte decimal de un número
# el resultado es una "tupla" con la parte decimal y la parte entera
### ejemplo: obtener la parte entera y la parte decimal de un número decimal
### partes_numer0 = modf(325.48)
### (0.48,325.0)
### necesito acceder al primer número
### partes[0]


if b > 0 :

    signo_b ='+'
else :
    signo_b =''

if c > 0 :
    signo_c ='+'
else :
    signo_c =''

# usando f-string puedo incluir en el texto variables
print(f'\nTu ecuación es: {a}x^2{signo_b}{b}x{signo_c}{c}')

# fórmula de la ecuación de 2do grado:
# x = ( -b +- raiz(b^2 -4*a*c) ) / 2a
# sqrt() me calcula la raiz cuadrada de un número
# para poder usar función sqrt() he tenido que "enseñarle mates" ---> import math

if (b**2-4*a*c) >= 0 :
    
    x1 = (-b + math.sqrt( b**2 - 4*a*c) ) / 2*a
    x2 = (-b - math.sqrt( b**2 - 4*a*c) ) / 2*a

    print(f'\nLa primera solución es: {x1:.2f}')
    print(f'\nLa segunda solución es: {x2:.2f}')

else : 
    print("La ecuación no tiene solución. El discriminante es negativo.")

## ejemplos: x^2+4x+4 = 0
## ejemplo: x^2+4x = 0
## ejemplo: x^2-16 = 0

# print("Estos son los tipos de variables: ")

# imprime el tipo de una variable
# texto ='hola'
# number = 23
# number_decimal = 23.56
# lista = [1,2,3,4,5]
# print( type(texto) ) # str -> string
# print( type(number) ) # int -> integer
# print( type(number_decimal) ) # float -> decimal
# print( type(lista) ) # list -> lista




