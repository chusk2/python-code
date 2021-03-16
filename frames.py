import tkinter as tk

window = tk.Tk()

frames = tk.Frame()

frame_relief= ['flat', 'sunken', 'raised', 'groove', 'ridge']

for i in frame_relief :
    frame = tk.Frame()
    frame.configure( relief = i )
    frame.pack()
    button = tk.Button (master = frame, text=f'This label uses {i} style.')
    button.configure(relief =  i)
    button.pack()
    
window.mainloop()
