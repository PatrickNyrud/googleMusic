from Tkinter import *
from ttk import *

root = Tk()
note = Notebook(root)

tab1 = Frame(note)

note.add(tab1, text = "Tab One")
note.pack()
root.mainloop()
exit()