
from tkinter import *
from tkinter import ttk

root=Tk()

label1 =ttk.Label(root,text='Hello Daniel! How are you doing?')
label1.pack()
label1.config( foreground = 'blue' , background = 'yellow')
label1.config(wraplength = 150)
label1.config(font = ('Courier',18,'bold') )
label1.config(justify = CENTER)


list1 = ttk.Combobox( root, textvariable = ' Choose one answer...',
                      values= ['Fine, thanks!' , 'Not a great day :(' ] )

list1.pack()

button1 = ttk.Button(root, text='Fine! Thanks.')
button2 = ttk.Button(root, text='Not a good day...')

button1.pack()
button2.pack()