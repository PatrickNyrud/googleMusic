import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
try:
	from nova_config import nova_config
except Exception as e:
	pass
from PIL import ImageTk

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

#Change items_frame width when change sizes

#Redo all the images, make em look better
#Add miletones, such as 10000kr 20000kr osv.
#Log when sold out
#Add monster single
#Add nova for 12, 99kr
#Add pictures to buttons?=
#Redo the change amount func
#See if can fix click minus button too fast checkout bugs out

class main_frame:
	def __init__(self):
		self.x = 1600
		self.y = 800

		self.root = tk.Tk()
		self.root.geometry(str(self.x) + "x" + str(self.y))

		self.note = ttk.Notebook(self.root)

		self.tab_sale = tk.Frame(self.note)
		self.tab_config = tk.Frame(self.note)

		self.note.add(self.tab_sale, text = "Sale")
		self.note.add(self.tab_config, text = "Config")
	
		self.note.pack()

		#self.tab_sale.bind("<Visibility>", self.on_visibility)

		self.main_frame = tk.Frame(self.tab_sale, bg = "black")
		self.main_frame.pack(fill = "both", expand = True)
		
		self.tab_config_start = nova_config(self.tab_config)

		self.top_class = top_frame()
		self.checkout_class = checkout_frame()
		self.items_class = items_frame()

		self.top_class.initialize(self.main_frame, self.root)
		self.checkout_class.initialize(self.main_frame, self.items_class, self.top_class)
		self.items_class.initialize(self.main_frame, self.checkout_class)

		self.top_class.update_time()
		self.root.mainloop()

	def on_visibility(self, event):
		print "focus"

class top_frame:
	def initialize(self, frame, rt):
		self.root = rt
		self.frame = frame
		self.top_frame = tk.Frame(self.frame, bg = "red", height = 50)

		self.now_date = time.strftime("%d_%b_%Y")
		self.log_folder = "logs//"
		self.salgs_log = "salgs_log.txt"
		self.total_salg_sum = "total_salg_sum.txt"
		self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

		self.total_salg_label = tk.Label(self.top_frame, text = "")
		self.total_salg_dag_label = tk.Label(self.top_frame, text = "")

		self.time = tk.Label(self.top_frame, text = "")
		self.time.place(relx = .5, rely = .5, anchor = "center")

		self.total_salg_label.place(relx = .8, rely = .5, anchor = "center")
		self.total_salg_dag_label.place(relx = .2, rely = .5, anchor = "center")

		self.top_frame.pack(side = "top", fill = "x")

		self.display_total_sold()

	def update_time(self):
		self.now_time = time.strftime("%H:%M:%S")
		self.time.config(text = self.now_time)
		self.root.after(1000, self.update_time)

	def update_sum(self, dest, file, final_price):
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


	def display_total_sold(self):#self.log_folder + self.total_salg_sum
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

class checkout_frame:
	def initialize(self, frame, items_object, top_object):
		self.frame = frame
		self.items_object = items_object
		self.top_object = top_object

		self.items_check_out = []
		self.frame_pos_list = []

		self.now_date = time.strftime("%d_%b_%Y")
		self.log_folder = "logs//"
		self.salgs_log = "salgs_log.txt"
		self.total_salg_sum = "total_salg_sum.txt"
		self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

		self.total_sum = 0

		self.label_width = 30

		self.item_frame = tk.Frame(self.frame, bg = "yellow", width = 200, height = 1000 - 100) #self.y - topframe height

		self.check_out_label = tk.Label(self.item_frame, bg = "white", text = "0", width = self.label_width)
		self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

		self.check_out_button = tk.Button(self.item_frame, bg = "white", text = "DONE",  command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
		self.check_out_button.grid(row = 1, column = 0, pady = (20, 0))

		self.reset_button = tk.Button(self.item_frame, bg = "white", text = "RESET",  command = lambda : self.reset())
		self.reset_button.grid(row = 1, column = 1, pady = (20, 0))

		self.item_frame.grid_propagate(False)
		self.item_frame.pack(side = "left", fill = "y")

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
			self.tmp_lbl = tk.Label(self.item_frame, bg = "white", text = x, width = self.label_width)
			self.tmp_lbl.grid(row = j + 1, column = 0, columnspan = 2)

			self.check_out_grid_list.append(self.tmp_lbl)

		self.check_out_label.config(text = str(self.total_sum))

		self.check_out_button.grid_configure(row = j + 2)
		self.reset_button.grid_configure(row = j + 2)

	def remove_from_checkout(self, name, price):
		for widget in self.item_frame.winfo_children():
			widget.destroy()

		if len(self.items_check_out) > 0:
			#self.total_sum -= int(price)
			for j, x in enumerate(self.final_string):
				if name in x:
					self.total_sum -= int(price)
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
		self.check_out_label = tk.Label(self.item_frame, bg = "white", text = self.total_sum, width = self.label_width)
		self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

		for j, x in enumerate(self.final_string):
			self.tmp_text_label = tk.Label(self.item_frame, bg = "white", text = x, width = self.label_width)
			self.tmp_text_label.grid(row = j + 1, column = 0, columnspan = 2)

			self.check_out_grid_list.append(self.tmp_text_label)

		self.check_out_button = tk.Button(self.item_frame, bg = "white", text = "DONE",  command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
		self.check_out_button.grid(row = j + 2, column = 0, pady = (20, 0))

		self.reset_button = tk.Button(self.item_frame, bg = "white", text = "RESET",  command = lambda : self.reset())
		self.reset_button.grid(row = j + 2, column = 1, pady = (20, 0))

	def check_out_done(self, final_price, items):
		self.top_object.log_sale(items, self.log_folder, self.salgs_log, final_price)
		self.top_object.update_sum(self.log_folder, self.total_salg_sum, final_price)
		self.top_object.update_sum(self.log_folder, self.total_salg_sum_dag, final_price)
		self.top_object.display_total_sold()

		for x in items:
			self.items_object.inventory(x, True)

		self.reset()


	def reset(self):
		for widget in self.item_frame.winfo_children():
			widget.destroy()

		self.items_object.reset_amount(self.frame_pos_list)

		self.frame_pos_list = []
		self.items_checked = []
		self.items_check_out = []
		self.check_out_grid_list = []
		self.final_string = []

		self.total_sum = 0

		self.re_draw()

class items_frame():
	def initialize(self, frame, checkout_object):
		self.frame = frame
		self.scrollbar_canvas = tk.Canvas(self.frame, bg = "pink", width = 1700)
		self.checkout_frame = tk.Frame(self.scrollbar_canvas, bg = "green", height = 1000 - 100) #self.y - topframe height

		self.log_folder = "logs//"
		self.pic_folder = "pics//"
		self.lager_file = "lager.txt"
		self.prices = "priser.txt"

		self.checkout_object = checkout_object

		self.btn_font = tkFont.Font(family = "Helvetica", size = 25)
		self.text_font = tkFont.Font(family = "Helvetica", size = 15)
		self.amount_font = tkFont.Font(family = "Helvetica", size = 10)

		self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
		self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)
		
		self.checkout_frame.pack(side = "right")

		self.vsb.pack(side="right", fill="both")

		self.scrollbar_canvas.pack(side = "right", fill = "y")
		self.scrollbar_canvas.create_window((4,4), window = self.checkout_frame, anchor="nw", tags="self.checkout_frame")

		self.checkout_frame.bind("<Configure>", self.onFrameConfigure)
		self.checkout_frame.bind("<MouseWheel>", self.OnMouseWheel)

		self.frame.bind("<Visibility>", self.draw_main_items)

	def draw_main_items(self, event):
		self.frame_list = []
		self.label_list = []
		self.lager_list = []
		self.add_button_func = []
		self.minus_button_func = []
		self.amount_list = []

		self.checkout_frame.focus_set()

		for widget in self.checkout_frame.winfo_children():
			widget.destroy()

		self.inventory_price_list = self.pic_price_file(self.log_folder, self.prices)
		self.place_frame(self.inventory_price_list)

	def onFrameConfigure(self, event):
		self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

	def OnMouseWheel(self,event):
		self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

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
					self.item_frame = tk.Canvas(self.checkout_frame, bg = "white", height = 250, width = 250, highlightthickness = 5, highlightbackground = "black")
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
				self.t = tk.Label(self.frame_list[self.frame_position], bg = "white", text = "PLACE NOVA LOGO HERE?")
				self.t.place(relx = .5, rely = .5, anchor = "center")

	def place_labe_name(self, name, frame_pos):
		self.tmp_label = tk.Label(self.frame_list[self.frame_position], font = self.text_font, bg = "white", text = self.item_name.upper())
		self.tmp_label.place(relx = .5, rely = .1, anchor = "center")
		
		self.label_list.append(self.tmp_label)

	def place_label_lager(self, name, frame_pos):
		self.label_text = self.inventory(name, False).strip()

		self.label_var = tk.Label(self.frame_list[frame_pos], bg = "white", text = "P" + "\xc3\xa5".decode("utf-8") +" lager (" + self.label_text + ")")
		self.label_var.place(relx = .5, rely = .9, anchor = "center")

		self.lager_list.append(self.label_var)


	def place_amount_label(self, name, frame_pos):
		self.amount_var = tk.Label(self.frame_list[frame_pos], font = self.amount_font, bg = "white", text = "")
		self.amount_var.place(relx = .8, rely = .45, anchor = "center")

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

	def reset_amount(self, frame_pos):
		for x in frame_pos:
			self.amount_list[int(x)].config(text = "")

	def place_button_add(self, name, price, frame_pos):
		self.button_add_place = tk.Button(self.frame_list[frame_pos], bg = "white", text = "ADD", borderwidth = 2, command = lambda : [self.change_amount(name, frame_pos, True), self.checkout_object.add_to_checkout(name, price, frame_pos)])
		self.photo = ImageTk.PhotoImage(file = self.pic_folder + name + "_liten.png")
		self.button_add_place.config(image = self.photo, width = 150, height = 150)
		self.button_add_place.image = self.photo
		self.button_add_place.place(relx = .35, rely = .5, anchor = "center")

		self.add_button_func.append(self.button_add_place)

	def place_button_minus(self, name, price, frame_pos):
		self.button_minus_place = tk.Button(self.frame_list[frame_pos], text = "-", width = 3, font = self.btn_font, bg = "white",  command = lambda : [self.change_amount(name, frame_pos, False), self.checkout_object.remove_from_checkout(name, price)])
		self.button_minus_place.place(relx = .8, rely = .67, anchor = "center")

		self.minus_button_func.append(self.button_minus_place)

	def inventory(self, name, remove):
		self.inventory_num_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//lager.txt", "r") as f:#self.log_folder + self.lager_file
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
					self.lager_list[j].config(text = "P" + "\xc3\xa5".decode("utf-8") +" lager (" + str(self.new_sum) + ")")
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
					return x[1].strip()

if __name__ == "__main__":
	strt = main_frame()