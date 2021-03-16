def suma(*args) :
    suma = 0
    if len(args) < 2 :
        print('¿Nada que sumar!')
    else :
        for arg in args:
            suma += arg
        return suma

if __name__ == "__main__":
   print( suma(1,3,5,7,12,-13) )