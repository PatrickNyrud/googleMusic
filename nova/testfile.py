import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os

class main_frame:
	def __init__(self):
		self.x = 1300
		self.y = 1000

		self.root = tk.Tk()
		self.root.geometry(str(self.x) + "x" + str(self.y))


		self.main_frame = tk.Frame(self.root, bg = "black")
		self.main_frame.pack(fill = "both", expand = True)
		
		self.test = top_frame(self.main_frame)
		self.test1 = checkout_frame(self.main_frame)
		self.test2 = items_frame(self.main_frame)

		self.root.mainloop()

class top_frame:
	def __init__(self, frame):
		self.frame = frame
		self.top_frame = tk.Frame(self.frame, bg = "red", height = 100)
		self.top_frame.pack(side = "top", fill = "x")

class checkout_frame:
	def __init__(self, frame):
		self.frame = frame
		self.item_frame = tk.Frame(self.frame, bg = "yellow", width = 200)
		self.item_frame.pack(side = "left", fill = "y")


class items_frame():
	def __init__(self, frame):
		self.frame = frame
		self.scrollbar_canvas = tk.Canvas(self.frame, bg = "pink", width = 1200)
		self.checkout_frame = tk.Frame(self.scrollbar_canvas, bg = "green", height = 1000 - 100) #self.y - topframe height

		self.log_folder = "logs//"
		self.pic_folder = "rz//"
		self.lager_file = "lager.txt"
		self.prices = "priser.txt"

		self.frame_list = []
		self.label_list = []
		self.lager_list = []
		self.add_button_func = []
		self.minus_button_func = []
		self.amount_list = []

		self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
		self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)
		
		self.checkout_frame.pack(side = "right")

		self.vsb.pack(side="right", fill="both")

		self.scrollbar_canvas.pack(side = "right", fill = "y")
		self.scrollbar_canvas.create_window((4,4), window = self.checkout_frame, anchor="nw", tags="self.checkout_frame")

		self.checkout_frame.bind("<Configure>", self.onFrameConfigure)

		self.inventory_price_list = self.pic_price_file(self.log_folder, self.prices)
		self.place_frame(self.inventory_price_list)

	def onFrameConfigure(self, event):
		self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

	def pic_price_file(self, dirr, file):
		self.inv_list = []
		with open(dirr + file, "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)

		return self.inv_list

	def place_frame(self, price_list):
		#print price_list
		self.column = 4
		self.item_in_frame = 5

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(price_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.item_frame = tk.Canvas(self.checkout_frame, bg = "black", height = 200, width = 200)
					self.item_frame.grid(row = row, column = column, padx = (57, 0), pady = (50, 0))
					self.frame_list.append(self.item_frame)
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.item_name = price_list[self.item_pos][0]
					self.item_price = price_list[self.item_pos][1]

					self.item_pos += 1
					for x in range(self.item_in_frame):
						if x == 0:
							#Text of the item
							self.place_labe_name(self.item_name, self.frame_position)
						elif x == 1:
							#THe add button
							self.place_button_add(self.item_name, self.item_price, self.frame_position)
						elif x == 2:
							#The - button
							self.place_button_minus(self.item_name, self.item_price, self.frame_position)
						elif x == 3:
							#The amount of items
							self.place_amount_label(self.item_name, self.frame_position)
						elif x == 4:
							#The inv num
							self.place_label_lager(self.item_name, self.frame_position)
					self.frame_position += 1
			except:
				pass

	def place_labe_name(self, name, frame_pos):
		self.tmp_label = tk.Label(self.frame_list[self.frame_position], text = self.item_name)
		self.tmp_label.place(relx = .5, rely = .05, anchor = "center")
		
		self.label_list.append(self.tmp_label)

	def place_label_lager(self, name, frame_pos):
		self.label_text = self.inventory(name, False).strip()

		self.label_var = tk.Label(self.frame_list[frame_pos], text = self.label_text)
		self.label_var.place(relx = .5, rely = .9, anchor = "center")

		self.lager_list.append(self.label_var)


	def place_amount_label(self, name, frame_pos):
		self.amount_var = tk.Label(self.frame_list[frame_pos], text = "")
		self.amount_var.place(relx = .8, rely = .7, anchor = "center")

		self.amount_list.append(self.amount_var)

	def place_button_add(self, name, price, frame_pos):
		self.button_add_place = tk.Button(self.frame_list[frame_pos], text = "ADD", bg = "red")#,  command = lambda : [self.change_amount(name, frame_pos, True), self.add_to_checkout(name, price, frame_pos)])
		#self.photo = ImageTk.PhotoImage(file = self.pic_folder + name + "_liten.png")
		#self.button_add_place.config(image = self.photo, width = 150, height = 150)
		#self.button_add_place.image = self.photo
		self.button_add_place.place(relx = .5, rely = .5, anchor = "center")

		self.add_button_func.append(self.button_add_place)

	def place_button_minus(self, name, price, frame_pos):
		self.button_minus_place = tk.Button(self.frame_list[frame_pos], text = "MINUS", bg = "red",  command = lambda : [self.change_amount(name, frame_pos, False), self.remove_from_checkout(name, price)])
		self.button_minus_place.place(relx = .5, rely = .7, anchor = "center")

		self.minus_button_func.append(self.button_minus_place)

	def inventory(self, name, remove):
		self.inventory_num_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open(self.log_folder + self.lager_file, "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inventory_num_list.append(self.tmp_var)
		f.close()

		if remove:
			self.ch_remove = "'[]"
			for j, x in enumerate(self.inventory_num_list):
				if x[0] in name:
					self.remove_inv_sum = self.inventory_num_list[j][1]
					self.new_sum = int(self.remove_inv_sum) - 1
					self.lager_list[j].config(text = str(self.new_sum))
					self.inventory_num_list[j][1] = str(self.new_sum) + "\n"
					with open(self.log_folder + self.lager_file, "w") as f:
						for x in self.inventory_num_list:
							x[1] = x[1].strip(" ")
							self.final_inv_string = str(x)
							for c in self.ch_remove:
								self.final_inv_string = self.final_inv_string.replace(c, "")
							f.write(self.final_inv_string.replace("\\n", "\n"))
		else:
			for x in self.inventory_num_list:
				if x[0] == name:
					return x[1]


if __name__ == "__main__":
	strt = main_frame()