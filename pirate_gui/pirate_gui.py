import Tkinter as tk
from tkinter import ttk
import tkFont
import pirate_overview

class main_frame:
    def __init__(self):
        self.x = 1200
        self.y = 800

        self.root = tk.Tk()
        self.root.geometry(str(self.x) + "x" + str(self.y))

        self.root.title("Pirate")

        #self.root.iconbitmap(os.getcwd() + "\\pics\\otherpic\\nova_logo.ico")

        self.note = ttk.Notebook(self.root)

        self.overveiw_tab = tk.Frame(self.note)
        self.upcomming_tab = tk.Frame(self.note)
        self.config_tab = tk.Frame(self.note)

        self.note.add(self.overveiw_tab, text = "Overveiw" + (" " * (20-8))) #lazy af
        self.note.add(self.upcomming_tab, text = "Upcomming" + (" " * (20-9)))
        self.note.add(self.config_tab, text = "Config" + (" " * (20-6))) #lazy af

        self.note.pack()

        self.main_frame = tk.Frame(self.overveiw_tab, bg = "black", width = self.x, height = self.y)
        self.main_frame.pack(fill = "both", expand = True)
        
        self.p_overview = pirate_overview.overview_window(self.main_frame)

        self.root.mainloop()

if __name__ == "__main__":
    strt = main_frame()
