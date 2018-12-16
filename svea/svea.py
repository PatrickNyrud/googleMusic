import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import svea_top
import svea_checkout
import svea_item
import svea_config
import svea_salg_log
from PIL import Image, ImageTk

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

#------Minor mix
#Fix excel logs

#------BUGS------#
#See if can fix click minus button too fast checkout bugs out

#------Addition------#
#Add customer side

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

        self.root.iconbitmap(os.getcwd() + "\\pics\\otherpic\\nova_logo.ico")

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

        self.tab_salg_start = svea_salg_log.salg_log(self.tab_salg_log)
        self.tab_config_start = svea_config.config(self.tab_config)

        self.top_class = svea_top.top_frame()
        self.checkout_class = svea_checkout.checkout_frame()
        self.items_class = svea_item.items_frame()

        self.top_class.initialize(self.main_frame, self.root)
        self.checkout_class.initialize(self.main_frame, self.items_class, self.top_class)
        self.items_class.initialize(self.main_frame, self.checkout_class)

        self.top_class.update_time()
        self.root.mainloop()

if __name__ == "__main__":
    strt = main_frame()
