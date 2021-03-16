
import tkinter as tk

root = tk.Tk()
root.configure(width=30,height=20)

lbl_header = tk.Label( root, text = 'Tkinter window' , fg='Green' , bg = 'black')
lbl_header.configure( font = ('Courier', 22, 'bold') )

lbl_header.pack()

lbl_instructions = tk.Label( text='Escribe aquí tu nombre...')
lbl_instructions.pack()

entry1 = tk.Entry(text='Escribe aquí tu nombre...')
entry1.pack()

root.mainloop()