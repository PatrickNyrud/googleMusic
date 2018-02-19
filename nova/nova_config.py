import Tkinter as tk
from tkinter import ttk
import tkFont
import time
from nova import items_frame

#Button for update, or func like time func for update inventory
#Maybe add update button to nova.py to update evnt new prices 

class nova_config:
	def __init__(self, frame):
		self.frame = frame
		self.main_frame = tk.Frame(self.frame, bg = "red", width = 50, height = 50)

		self.place_list = []
		self.frame_list = []

		self.name_list = []
		self.price_list = []
		self.inventory_list = []

		self.main_frame.pack(fill = "both", expand = True)

		self.place_frames()

	def place_frames(self):
		self.items_object = items_frame()
		self.inv_list = self.items_object.pic_price_file("logs//", "priser.txt")

		self.column = 3
		self.item_in_frame = 3

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(self.inv_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.item_frame = tk.Canvas(self.main_frame, bg = "white", height = 50, width = 450, highlightthickness = 5, highlightbackground = "black", highlightcolor = "black")
					
					self.item_frame.grid_propagate(False)

					self.item_frame.grid(row = row, column = column, padx = (57, 0), pady = (50, 0))
					self.frame_list.append(self.item_frame)
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					# self.item_name = price_list[self.item_pos][0]
					# self.item_price = price_list[self.item_pos][1]

					self.item_pos += 1
					for x in range(self.item_in_frame):
						if x == 0:
							self.place_label(self.name_list, self.frame_position, self.inv_list[self.frame_position][0], 0)
						elif x == 1:
							self.place_entry(self.price_list, self.frame_position, self.inv_list[self.frame_position][1].strip(), 1)
						elif x == 2:
							self.label_text = self.items_object.inventory(self.inv_list[self.frame_position][0], False)
							self.place_entry(self.inventory_list, self.frame_position, self.label_text, 2)
					self.frame_position += 1
			except:
				pass

	def place_label(self, list_type, frame_pos, lbl_text, clmn):
		self.lbl_list_type = list_type

		self.lbl = tk.Label(self.frame_list[frame_pos], text = lbl_text)
		self.lbl.grid(row = 1, column = clmn, pady = (20, 0), padx = (30, 30))

		self.lbl_list_type.append(self.lbl)

	def place_entry(self, list_type, frame_pos, lbl_text, clmn):
		self.entry_list_type = list_type

		self.entry = tk.Entry(self.frame_list[frame_pos])
		self.entry.grid(row = 1, column = clmn, pady = (20, 0), padx = (0, 30))
		self.entry.insert(0, lbl_text)

		self.entry_list_type.append(self.entry)

	def get_inv_num(self):
		for x in range(len(self.inv_list)):
			pass