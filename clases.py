class Perro :

    def __init__(self,name,age) :
        self.name = name
        self.age = age
    
    def how_old(self):
        return self.age*7
        
    def say_my_name(self) :
        print(f'Mi nombre es {self.name}.')
    
perro1 = Perro(age=10,name='Paquito')
perro2 = Perro(age=12,name='Pachón')

print(f'Tengo dos perros y sus nombres son: {perro1.name} y {perro2.name}.')
print(f'La edad de mi primer perro es {perro1.how_old()} años.')