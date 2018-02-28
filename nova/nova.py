import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import nova_top
import nova_checkout
import nova_item
import nova_config
import nova_salg_log
from PIL import Image, ImageTk

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

#------Minor mix
#Change items_frame width when change sizes
#Edit all the with open to use variables such as self.logfolder
#Set relief on frames, like sunken on items frame

#------BUGS------#
#See if can fix click minus button too fast checkout bugs out

#------Addition------#
#Add nova for 12, 99kr
#Add font to checkout
#Add customer side
#Add return cash
#Add button for changing colors, or maybe in the config for a light and dark theme, a check box
#If so ^^^^, make a file witch has the colors, and change if change theme
#tkinter colos http://www.science.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png

#------Redo------#
#Redo all the images, make em look better

class main_frame:
    def __init__(self):
        self.x = 1600
        self.y = 800

        self.root = tk.Tk()
        self.root.geometry(str(self.x) + "x" + str(self.y))
        #self.root.attributes("-fullscreen", True)

        self.root.title("Nova")
        #self.root.iconbitmap("E:\\github\\googleMusic\\nova\\pics\\otherpic\\nova_logo.ico") #Need full dest for some reason

        self.note = ttk.Notebook(self.root)

        self.tab_sale = tk.Frame(self.note)
        self.tab_salg_log = tk.Frame(self.note)
        self.tab_config = tk.Frame(self.note)

        self.note.add(self.tab_sale, text = "Sale" + (" " * (20-4))) #lazy af
        self.note.add(self.tab_salg_log, text = "Salg log" + (" " * (20-8)))
        self.note.add(self.tab_config, text = "Config" + (" " * (20-6))) #lazy af

        self.note.pack()

        self.main_frame = tk.Frame(self.tab_sale, bg = "black")
        self.main_frame.pack(fill = "both", expand = True)
        
        self.tab_salg_start = nova_salg_log.salg_log(self.tab_salg_log)
        self.tab_config_start = nova_config.config(self.tab_config)

        self.top_class = nova_top.top_frame()
        self.checkout_class = nova_checkout.checkout_frame()
        self.items_class = nova_item.items_frame()

        self.top_class.initialize(self.main_frame, self.root)
        self.checkout_class.initialize(self.main_frame, self.items_class, self.top_class)
        self.items_class.initialize(self.main_frame, self.checkout_class)

        self.top_class.update_time()
        self.root.mainloop()

if __name__ == "__main__":
    strt = main_frame()
