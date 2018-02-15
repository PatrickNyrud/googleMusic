import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os

class main_frame:
	def __init__(self):
		self.x = 1200
		self.y = 1000

		self.root = tk.Tk()
		self.root.geometry(str(self.x) + "x" + str(self.y))


		self.main_frame = tk.Frame(self.root, bg = "black")
		self.main_frame.pack(fill = "both", expand = True)
		
		self.test = top_frame(self.main_frame)
		self.test1 = items_frame(self.main_frame)
		self.test2 = checkout_frame(self.main_frame, self.test1)

		#self.lbl = tk.Button(self.main_frame, text = "kek", command = lambda : self.test1.change())
		#self.lbl.place(relx = .5, rely = .5, anchor = "center")

		self.root.mainloop()

class top_frame:
	def __init__(self, frame):
		self.frame = frame
		self.top_frame = tk.Frame(self.frame, bg = "red", height = 100)
		self.top_frame.pack(side = "top", fill = "x")

class items_frame:
	def __init__(self, frame):
		self.frame = frame
		self.item_frame = tk.Frame(self.frame, bg = "white", width = 200)
		self.item_frame.pack(side = "left", fill = "y")

		self.label3 = tk.Label(self.item_frame, text = "hei")
		self.label3.place(relx = .5, rely = .5, anchor = "center")

	def change(self):
		self.label3.config(text = "hello")

class checkout_frame(items_frame):
	def __init__(self, frame, c_object):
		self.frame = frame
		self.object = c_object
		self.checkout_frame = tk.Frame(self.frame, bg = "green", width = 1000)
		self.checkout_frame.pack(side = "right", fill = "y")

		self.btn = tk.Button(self.checkout_frame, text = "change", command = lambda : self.object.change())
		self.btn.place(relx = .5, rely = .5, anchor = "center")


if __name__ == "__main__":
	strt = main_frame()