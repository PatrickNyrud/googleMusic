import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

class settings:
    def __init__(self, frame):
        self.frame = frame
        self.main_frame = tk.Frame(self.frame, bg = "red")
        self.main_frame.pack(fill = "both", expand = True)

        self.draw()


    def draw(self):
        self.title_name = tk.Label(self.main_frame, text = "Theme", bg = "white")
        self.title_name.grid(row = 0, column = 1)

        self.light_option = tk.Checkbutton(self.main_frame, text = "Light Theme", bg = "white")
        self.light_option.grid(row = 1, column = 1)
