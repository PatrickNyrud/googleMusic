import Tkinter as tk
from tkinter import ttk
import tkFont
import time
from nova import items_frame

#Button for update, or func like time func for update inventory
#Maybe add update button to nova.py to update evnt new prices 

#Add green text to button when u have updated
#Add button to refresh page, feks when removd item from sale, then over to config, make it update to new inv num

#Add pictures to buttons?=

class nova_config:
	def __init__(self, frame):
		self.frame = frame
		self.scrollbar_canvas = tk.Canvas(self.frame, bg = "pink", width = 1700)
		self.main_frame = tk.Frame(self.frame, bg = "red", width = 50, height = 50)

		self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
		self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)

		self.text_font = tkFont.Font(family = "Helvetica", size = 12)

		self.main_frame.pack(fill = "both", expand = True)

		self.vsb.pack(side="right", fill="both")

		self.scrollbar_canvas.pack(side = "right", fill = "y")
		self.scrollbar_canvas.create_window((4,4), window = self.main_frame, anchor="nw", tags="self.main_frame")

		self.main_frame.bind("<Configure>", self.onFrameConfigure)
		self.main_frame.bind("<MouseWheel>", self.OnMouseWheel)

		self.frame.bind("<Visibility>", self.draw_main_items)


	def draw_main_items(self, event):
		self.frame_list = []
		self.name_list = []
		self.price_list = []
		self.price_name_list = []
		self.inventory_list = []
		self.inv_name_list = []
		self.button_list = []

		self.main_frame.focus_set()

		for widget in self.main_frame.winfo_children():
			widget.destroy()

		self.place_frames()

	def onFrameConfigure(self, event):
		self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

	def OnMouseWheel(self,event):
		self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

	def place_frames(self):
		self.items_object = items_frame()
		self.inv_list = self.items_object.pic_price_file("logs//", "priser.txt")

		self.column =6
		self.item_in_frame = 6

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(self.inv_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.item_frame = tk.Canvas(self.main_frame, bg = "white", height = 180, width = 180, highlightthickness = 5, highlightbackground = "black", highlightcolor = "black")
					self.item_frame.grid_propagate(False)
					self.item_frame.grid(row = row, column = column, padx = (57, 0), pady = (50, 0))
					self.frame_list.append(self.item_frame)
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.item_pos += 1
					for x in range(self.item_in_frame):
						if x == 0:
							self.place_name_label(self.name_list, self.frame_position, self.inv_list[self.frame_position][0], 0, 2)
						elif x == 1:
							self.place_label(self.price_name_list, self.frame_position, "Pris: ", 1, 1, 10, 60)
						elif x == 2:
							self.place_entry(self.price_list, self.frame_position, self.inv_list[self.frame_position][1].strip(), 1, 2, 0, 60)
						elif x == 3:
							self.place_label(self.inv_name_list, self.frame_position, "Antall:", 2, 1, 10, 10)
						elif x == 4:
							self.label_text = self.items_object.inventory(self.inv_list[self.frame_position][0], False)
							self.place_entry(self.inventory_list, self.frame_position, self.label_text, 2, 2, 0, 10)
						elif x == 5:
							self.place_button(self.button_list, self.frame_position, self.inv_list[self.frame_position][0])
					self.frame_position += 1
			except:
				self.t = tk.Label(self.frame_list[self.frame_position], bg = "white", text = "PLACE SOME SHIT HERE?")
				self.t.place(relx = .5, rely = .5, anchor = "center")

	def place_name_label(self, list_type, frame_pos, lbl_text, rw, col):
		self.lbl_list_type = list_type

		self.lbl = tk.Label(self.frame_list[frame_pos], font = self.text_font, text = lbl_text, bg = "white")
		self.lbl.place(relx = .5, rely = .15, anchor = "center")

		self.lbl_list_type.append(self.lbl)

	def place_label(self, list_type, frame_pos, lbl_text, rw, col, pdx, pdy):
		self.lbl_list_type = list_type

		self.lbl = tk.Label(self.frame_list[frame_pos], font = self.text_font, text = lbl_text, bg = "white", anchor = "w")
		self.lbl.grid(row = rw, column = col, padx = (pdx, 0), pady = (pdy, 0))

		self.lbl_list_type.append(self.lbl)

	def place_entry(self, list_type, frame_pos, lbl_text, rw, col, pdx, pdy):
		self.entry_list_type = list_type

		self.entry = tk.Entry(self.frame_list[frame_pos], font = self.text_font, width = 12)
		self.entry.grid(row = rw, column = col, pady = (pdy, 0))
		self.entry.insert(0, lbl_text)

		self.entry_list_type.append(self.entry)

	def place_button(self, list_type, frame_pos, name):
		self.btn_list_type = list_type

		self.btn = tk.Button(self.frame_list[frame_pos], font = self.text_font, text = "UPDATE", bg = "white", command = lambda : self.get_nums(frame_pos, name))
		self.btn.place(relx = .5, rely = .8, anchor = "center")

		self.btn_list_type.append(self.btn)

	def get_nums(self, pos, name):
		self.inv_get = self.inventory_list[pos]
		self.price_get = self.price_list[pos]
		
		self.change_num_file(name, int(self.price_get.get()), "priser.txt")
		self.change_num_file(name, int(self.inv_get.get()), "lager.txt")

	def change_num_file(self, name, change_sum, file):
		self.inventory_num_list = []
		self.change_sum = change_sum
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//" + file, "r") as f:#self.log_folder + self.lager_file
			for x in f:
				self.tmp_var = x.split(",")
				self.inventory_num_list.append(self.tmp_var)
		f.close()

		self.ch_remove = "'[]"
		for j, x in enumerate(self.inventory_num_list):
			if x[0] in name:
				self.remove_inv_sum = self.inventory_num_list[j][1]
				self.new_sum = self.change_sum
				self.inventory_num_list[j][1] = str(self.new_sum) + "\n"
				with open("logs//" + file, "w") as f:
					for x in self.inventory_num_list:
						x[1] = x[1].strip(" ")
						self.final_inv_string = str(x)
						for c in self.ch_remove:
							self.final_inv_string = self.final_inv_string.replace(c, "")
						f.write(self.final_inv_string.replace("\\n", "\n"))
