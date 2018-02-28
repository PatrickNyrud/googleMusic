import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import random
from PIL import Image, ImageTk

class salg_log:
    def __init__(self, frame):
        self.log_label_list = []
        self.frame = frame

        self.canvas = tk.Canvas(self.frame, background="bisque", width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.config(scrollregion=self.canvas.bbox("ALL"))
        self.canvas.grid_propagate(False)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_motion)

        # the following two values cause the canvas to scroll
        # one pixel at a time
        self.canvas.configure(xscrollincrement=1, yscrollincrement=1)

        # finally, draw something on the canvas so we can watch it move
        #for i in range(1000):
            #x = random.randint(-1000, 1000)
            #y = random.randint(-1000, 1000)
            #color = random.choice(("red", "orange", "green", "blue", "violet"))
            #self.canvas.create_oval(x, y, x+20, y+20, fill=color)

        #self.mid_frame = tk.Frame(self.main_frame, bg = "pink")
        #self.mid_frame.place(relx = .5, rely = .0, anchor = "center")

        for j, line in enumerate(reversed(open("logs//salgs_log.txt").readlines())):
            tt = tk.Label(self.canvas, text = line, bg = "white")
            tt.pack(side = "bottom")

            self.log_label_list.append(tt)


    def on_press(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_motion(self, event):
        delta_x = event.x - self.last_x
        delta_y = event.y - self.last_y
        self.last_x = event.x
        self.last_y = event.y

        #self.canvas.xview_scroll(-delta_x, "units")
        self.canvas.yview_scroll(-delta_y, "units")