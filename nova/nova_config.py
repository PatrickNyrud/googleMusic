import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import ImageTk

class tabTwo:
	def __init__(self, frame):
		tab2 = tk.Frame(frame, bg = "yellow")
		frame.add(tab2, text = "Config")
		lbl = tk.Label(tab2, text = "cunt")
		lbl.place(relx = .5, rely = .5, anchor = "center")