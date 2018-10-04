import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import random
from PIL import Image, ImageTk

#Fix scroll here, its fast af boi

class salg_log:
    def __init__(self, frame):
        self.frame = frame
        self.scrollbar_canvas = tk.Canvas(self.frame, bg = "grey21", width = 1700)
        self.main_frame = tk.Frame(self.frame, width = 1500, bg = "grey21", height = self.file_len() * 40)

        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
        self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)

        self.text_font = tkFont.Font(family = "Helvetica", size = 20)

        self.main_frame.pack(fill = "both", expand = True)
    
        self.main_frame.pack_propagate(False)


        self.vsb.pack(side="right", fill="both")

        self.scrollbar_canvas.pack(side = "right", fill = "y", expand = True)
        self.scrollbar_canvas.create_window((4,4), window = self.main_frame, anchor="nw", tags="self.main_frame")

        self.main_frame.bind("<Configure>", self.onFrameConfigure)
        self.main_frame.bind("<MouseWheel>", self.OnMouseWheel)

        self.frame.bind("<Visibility>", self.draw_init)


    def onFrameConfigure(self, event):
        self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

    def OnMouseWheel(self,event):
        self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

    def draw_init(self, event):
        self.log_label_list = []

        self.main_frame.focus_set()

        for widget in self.main_frame.winfo_children():
                widget.destroy()

        self.display_log()

    def display_log(self):
        for j, line in enumerate(reversed(open("logs//salgs_log.txt").readlines())):
            self.log_label = tk.Label(self.main_frame, text = line.strip(), font = self.text_font, bg = "grey21", fg = "cornsilk2")
            self.log_label.pack(fill = "both", expand = 1)

            self.log_label_list.append(self.log_label)


    def file_len(self):
        with open("logs//salgs_log.txt", "r") as f:
            for j, x in enumerate(f):
                pass
        f.close()
        
        return j + 1


