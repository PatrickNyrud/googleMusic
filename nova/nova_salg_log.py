import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

class salg_log:
    def __init__(self, frame):
        self.frame = frame

        self.log_label_list = []

        self.main_frame = tk.Frame(self.frame, bg = "red")
        self.main_frame.pack(fill = "both", expand = True)

        self.display_log()

    def display_log(self):
        self.mid_frame = tk.Frame(self.main_frame, bg = "pink")
        self.mid_frame.place(relx = .5, rely = .0, anchor = "center")

        for j, line in enumerate(reversed(open("logs//salgs_log.txt").readlines())):
            tt = tk.Label(self.mid_frame, text = line, bg = "white")
            tt.grid(row = j, column = 0)

            self.log_label_list.append(tt)
