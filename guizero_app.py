from guizero import App, Text, TextBox, PushButton
from random import randint
def get_random_int() :
    number = randint(1,100)
    message2.value=f'Your random number is: {number}'

app = App(title="Counting letters", width= 500, height = 150, layout = 'grid')
app.bg='lightblue'
message = Text(app, text="Push the button to get a random number!", grid=[0,0])
message.text_size=12
message.font = 'Verdana'

button1 = PushButton(app,command = get_random_int,text = 'Click me!', grid = [1,0])

message2 = Text(app, color = 'darkblue', size=14, grid=[0,2])

button2 = PushButton(app, text='Button 2', grid=[0,1])
button3 = PushButton(app, text='Button 3', grid=[1,1])

app.display()