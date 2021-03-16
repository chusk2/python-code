from guizero import PushButton, App, Text
def cambiar() :
    #boton.text = 'Ha cambiado text'
    boton.value = 'Ha cambiado value'
    
app = App()
boton = PushButton(app, text='Boton3', command = cambiar)
message = Text(app, text=f'{boton.text}')
app.display()

