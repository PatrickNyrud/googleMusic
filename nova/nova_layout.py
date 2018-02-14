import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import ImageTk

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

#Have a overveiw on second monitor
#Have a second page for edit of inv and prices

#Edit self.check_out_width
#Edit self.top_frame_height
#Edit self.label_width
#Edit all the place relx rely in the frames where buttons are


class Nova():
	def __init__(self):
		self.x = 1200
		self.y = 1000
		self.check_out_width = 250 #Tune this when change geometry size
		self.top_frame_height = 20 #Tune this when change geometry size
		self.root = tk.Tk()
		self.root.geometry(str(self.x) + "x" + str(self.y))
		#self.root.attributes("-fullscreen", True)

		note = ttk.Notebook(self.root)

		tab1 = tk.Frame(note)

		self.label_width = 30

		self.now_date = time.strftime("%d_%b_%Y")

		self.log_folder = "logs//"
		self.pic_folder = "rz//"
		self.lager_file = "lager.txt"
		self.prices = "priser.txt"
		self.salgs_log = "salgs_log.txt"
		self.total_salg_sum = "total_salg_sum.txt"
		self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

		self.frame_list = []
		self.add_button_func = []
		self.minus_button_func = []
		self.label_list = []
		self.lager_list = []
		self.amount_list = []
		self.frame_pos_list = []

		self.items_check_out = []
		self.total_sum = 0

		self.top_frame = tk.Frame(tab1, bg = "black", height = self.top_frame_height, width = self.y)
		self.check_out = tk.Frame(tab1, background="green", width = self.check_out_width, height = self.x - self.top_frame_height)
		self.check_out.grid_propagate(False)
		self.main_canvas = tk.Canvas(tab1, background="yellow", width = self.x)
		self.main_frame = tk.Frame(self.main_canvas, bg = "red")
		self.vsb = tk.Scrollbar(tab1, orient="vertical", command=self.main_canvas.yview)
		self.main_canvas.configure(yscrollcommand=self.vsb.set)

		#-----------------------------TOP STUFF-----------------------------#
		self.total_salg_label = tk.Label(self.top_frame, text = "")
		self.total_salg_dag_label = tk.Label(self.top_frame, text = "")

		self.top = tk.Label(self.top_frame, text = "")
		self.top.place(relx = .5, rely = .5, anchor = "center")

		self.total_salg_label.place(relx = .8, rely = .5, anchor = "center")
		self.total_salg_dag_label.place(relx = .2, rely = .5, anchor = "center")
		#-----------------------------TOP STUFF-----------------------------#

		#-----------------------------CHECK OUT STUFF-----------------------------#
		self.check_out_label = tk.Label(self.check_out, text = "0", width = self.label_width)
		self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

		self.check_out_button = tk.Button(self.check_out, text = "DONE",  command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
		self.check_out_button.grid(row = 1, column = 0, pady = (20, 0))

		self.reset_button = tk.Button(self.check_out, text = "RESET",  command = lambda : self.reset())
		self.reset_button.grid(row = 1, column = 1, pady = (20, 0))
		#-----------------------------CHECK OUT STUFF-----------------------------#

		note.add(tab1, text = "Tab One")
		#note.add(tab2, text = "Tab Two")
		new = tabTwo(note)
		note.pack()
		self.top_frame.pack(side = "top", fill = "both")	
		self.check_out.pack(side = "left", fill = "both") 
		self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.vsb.pack(side="right", fill="both")
		self.main_canvas.pack(side="left", fill="both", expand=True)
		self.main_canvas.create_window((4,4), window=self.main_frame, anchor="nw", tags="self.main_frame")

		self.main_frame.bind("<Configure>", self.onFrameConfigure)

		#self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		#self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.inventory_price_list = self.pic_price_file(self.log_folder, self.prices)
	
		self.update_time()
		self.display_total_sold()
		self.place_frame(self.inventory_price_list)

		self.root.mainloop()

	def onFrameConfigure(self, event):
		self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

	def update_time(self):
		self.now_time = time.strftime("%H:%M:%S")
		self.top.config(text = self.now_time)
		self.root.after(1000, self.update_time)

	def pic_price_file(self, dirr, file):
		self.inv_list = []
		with open(dirr + file, "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)

		return self.inv_list


	def place_frame(self, price_list):
		self.column = 4
		self.item_in_frame = 5

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(price_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.frame = tk.Canvas(self.main_frame, bg = "black", height = 200, width = 200)
					self.frame.grid(row = row, column = column, padx = (57, 0), pady = (50, 0))
					self.frame_list.append(self.frame)
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

	def change_amount(self, name, frame_pos, add):
		self.change_var = self.amount_list[frame_pos]
		self.change_text = self.change_var.cget("text")
		if add:
			if len(self.change_text) < 2:
				self.change_var.config(text = "x1")
			else:
				self.change_text_int = int(self.change_text.strip("x"))
				self.change_text_int += 1
				self.change_var.config(text = "x" + str(self.change_text_int))
		else:
			if self.change_text == "x1" or self.change_text == "":
				self.change_var.config(text = "")
			else:
				self.change_text_int = int(self.change_text.strip("x"))
				self.change_text_int -= 1
				self.change_var.config(text = "x" + str(self.change_text_int))


	def place_button_add(self, name, price, frame_pos):
		self.button_add_place = tk.Button(self.frame_list[frame_pos], text = "ADD", bg = "red",  command = lambda : [self.change_amount(name, frame_pos, True), self.add_to_checkout(name, price, frame_pos)])
		self.photo = ImageTk.PhotoImage(file = self.pic_folder + name + "_liten.png")
		self.button_add_place.config(image = self.photo, width = 150, height = 150)
		self.button_add_place.image = self.photo
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

	def add_to_checkout(self, name, price, frame_pos):
		self.items_check_out.append(name)
		self.frame_pos_list.append(frame_pos)
		self.items_checked = []
		self.final_string = []
		self.check_out_grid_list = []

		self.total_sum += int(price)

		for x in self.items_check_out:
			if x in self.items_checked:
				pass
			else:
				self.items_checked.append(x)
				self.x_amount = 0
				for j in self.items_check_out:
					if x == j:
						self.x_amount += 1
				self.final_string.append(x + " x" + str(self.x_amount))

		for j, x in enumerate(self.final_string):
			self.tmp_lbl = tk.Label(self.check_out, text = x, width = self.label_width)
			self.tmp_lbl.grid(row = j + 1, column = 0, columnspan = 2)

			self.check_out_grid_list.append(self.tmp_lbl)

		self.check_out_label.config(text = str(self.total_sum))

		self.check_out_button.grid_configure(row = j + 2)
		self.reset_button.grid_configure(row = j + 2)


	def remove_from_checkout(self, name, price):
		for widget in self.check_out.winfo_children():
			widget.destroy()

		if len(self.items_check_out) > 0:
			self.total_sum -= int(price)
			for j, x in enumerate(self.final_string):
				if name in x:
					del self.items_check_out[j]
					self.change_string = list(self.final_string[j])
					self.change_string[len(self.change_string) - 1] = str(int(self.change_string[len(self.change_string) - 1]) - 1)
					if self.change_string[-1] > "0":
						self.new_string = "".join(self.change_string)
						self.final_string[j] = self.new_string
					else:
						del self.final_string[j]
				else: 
					pass
		else:
			pass

		self.re_draw()

	def re_draw(self):
		j = 0
		self.check_out_label = tk.Label(self.check_out, text = self.total_sum, width = self.label_width)
		self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

		for j, x in enumerate(self.final_string):
			self.tmp_text_label = tk.Label(self.check_out, text = x, width = self.label_width)
			self.tmp_text_label.grid(row = j + 1, column = 0, columnspan = 2)

			self.check_out_grid_list.append(self.tmp_text_label)

		self.check_out_button = tk.Button(self.check_out, text = "DONE",  command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
		self.check_out_button.grid(row = j + 2, column = 0, pady = (20, 0))

		self.reset_button = tk.Button(self.check_out, text = "RESET",  command = lambda : self.reset())
		self.reset_button.grid(row = j + 2, column = 1, pady = (20, 0))

	def check_out_done(self, final_price, items):
		self.items_check_out = []
		self.check_out_grid_list = []
		self.final_string = []

		self.total_sum = 0

		for widget in self.check_out.winfo_children():
			widget.destroy()

		for x in self.frame_pos_list:
			self.change_amount_text = self.amount_list[int(x)]
			self.change_amount_text.config(text = "")

		self.change_file(self.log_folder, self.total_salg_sum, final_price)
		self.change_file(self.log_folder, self.total_salg_sum_dag, final_price)

		self.log_sale(items, self.log_folder, self.salgs_log, final_price)
		for x in items:
			self.inventory(x, True)

		self.re_draw()

		self.display_total_sold()

	def reset(self):
		for widget in self.check_out.winfo_children():
			widget.destroy()

		for x in self.frame_pos_list:
			self.amount_list[int(x)].config(text = "")

		self.frame_pos_list = []
		self.items_checked = []
		self.items_check_out = []
		self.check_out_grid_list = []
		self.final_string = []

		self.total_sum = 0

		self.re_draw()

	def change_file(self, dest, file, final_price):
		with open(dest + file, "r+") as f:
			self.current_sum = f.read()
			self.new_sum = final_price + int(self.current_sum)
			f.seek(0)
			f.write(str(self.new_sum))
		f.close()

	def log_sale(self, items, dest, file, final_price):
		with open(dest + file, "a") as f:
			f.write(str(time.strftime("%d %b %Y %H:%M")) + "\n" +str(items) + " " + str(final_price) + " kr\n\n")
		f.close()


	def display_total_sold(self):
		if not os.path.isfile(self.log_folder + self.total_salg_sum_dag):
			with open(self.log_folder + self.total_salg_sum_dag, "w") as f:
				f.write("0")
			f.close()
		else:
			with open(self.log_folder + self.total_salg_sum_dag, "r+") as salg_dag, open(self.log_folder + self.total_salg_sum, "r") as salg_total:
				self.total_salg_label.config(text = salg_total.read())
				self.total_salg_dag_label.config(text = salg_dag.read())
			salg_dag.close()
			salg_total.close()

class tabTwo:
	def __init__(self, frame):
		tab2 = tk.Frame(frame)
		frame.add(tab2, text = "Tab 2")
		#lbl = tk.Label(tb2, text = "cunt")
		#lbl.place(relx = .5, rely = .5, anchor = "center")


if __name__ == "__main__":
	strt = Nova()