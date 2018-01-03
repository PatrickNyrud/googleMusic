from Tkinter import *    
master = Tk()
canvas = Canvas(master)
canvas.pack(side=LEFT)
vbar = Scrollbar(master, orient=VERTICAL)
vbar.config(command=canvas.yview)
vbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=vbar.set)
master.mainloop()