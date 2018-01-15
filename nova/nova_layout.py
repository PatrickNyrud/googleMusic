try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time

#Clean up things, the nova class
#Compare to github nova layout, find out why no scroll github layout

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

class Nova():
	def __init__(self):
		self.x = 1000
		self.y = 1000
		self.check_out_width = 250 #Tune this when change geo size
		self.top_frame_height = 20 #Tune this when change geo size
		root = tk.Tk()
		root.geometry(str(self.x) + "x" + str(self.y))
		#root.attributes("-fullscreen", True)

		self.label_width = 30

		self.log_folder = "logs//"
		self.pic_folder = "rz//"
		self.prices = "priser.txt"
		self.salgs_log = "salgs_log.txt"
		self.tot_salg_sum = "total_salg_sum.txt"
		self.tot_salg_sum_dag = "total_salg_sum_dag.txt"

		self.top_frame = tk.Frame(root, bg = "black", height = self.top_frame_height, width = self.y)
		self.check_out = tk.Frame(root, background="green", width = self.check_out_width, height = self.x - self.top_frame_height)
		self.check_out.grid_propagate(False)
		self.main_canvas = tk.Canvas(root, background="yellow")
		self.main_frame = tk.Frame(self.main_canvas, bg = "red")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.main_canvas.yview)
		self.main_canvas.configure(yscrollcommand=self.vsb.set)

		#-----------------------------TEMP STUFF-----------------------------#

		self.top = tk.Label(self.top_frame, text = "TOP")
		self.top.place(relx = .5, rely = .5, anchor = "center")

		#-----------------------------TEMP STUFF-----------------------------#

		self.check_out_label = tk.Label(self.check_out, text = "", width = 30)
		self.check_out_label.grid(row = 0, column = 0, pady = (0, 50))

		self.top_frame.pack(side = "top", fill = "both")	
		self.check_out.pack(side = "left", fill = "both") 
		self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.vsb.pack(side="right", fill="both")
		self.main_canvas.pack(side="left", fill="both", expand=True)
		self.main_canvas.create_window((4,4), window=self.main_frame, anchor="nw", tags="self.main_frame")

		self.main_frame.bind("<Configure>", self.onFrameConfigure)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.inventory_price_list = self.pic_price_file(self.log_folder, self.prices)
	

		self.place_frame()
		#self.place_text()

		root.mainloop()

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

	def pic_price_file(self, dirr, file):
		self.inv_list = []
		with open(dirr + file, "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)

		return self.inv_list


	def place_frame(self):
		self.frame_list = []
		self.add_button_func = []
		self.minus_button_func = []
		self.label_list = []
		self.lager_list = []
		self.amount_list = []

		self.item_check_out = []
		#self.check_out_grid_list = []

		self.total_sum = 0

		self.column = 3
		self.item_in_frame = 5

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(self.inventory_price_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):

					#-------------------------------MAKE FUNC FOR THIS-------------------------------#
					self.frame = tk.Canvas(self.main_frame, bg = "black", height = 200, width = 200)
					self.frame.grid(row = row, column = column, padx = (57, 0), pady = (50, 0))
					self.frame_list.append(self.frame)
					#-------------------------------MAKE FUNC FOR THIS-------------------------------#

					self.item_name = self.inventory_price_list[self.item_pos][0]
					self.item_price = self.inventory_price_list[self.item_pos][1]

					self.item_pos += 1
					for x in range(self.item_in_frame):
						if x == 0:
							#Text of the item
							self.tmp_label = tk.Label(self.frame_list[self.frame_position], text = self.item_name)
							self.tmp_label.place(relx = .5, rely = .2, anchor = "center")
							self.label_list.append(self.tmp_label)
							pass
						elif x == 1:
							#THe add button
							
							#-----------------------------Change this to like place amount and place label-----------------------------#
							self.add_button_func.append(self.place_button_add(self.item_name, self.item_price, self.frame_position))
							#-----------------------------Change this to like place amount and place label-----------------------------#
						
						elif x == 2:
							#The - button

							#-----------------------------Change this to like place amount and place label-----------------------------#
							self.minus_button_func.append(self.place_button_minus(self.item_name, self.item_price, self.frame_position))
							#-----------------------------Change this to like place amount and place label-----------------------------#
							
						elif x == 3:
							#The amount of items
							self.place_amount_label(self.item_name, self.frame_position)
							#self.amount_list.append(self.place_amount_label(self.item_name, self.frame_position))
						elif x == 4:
							#The inv num
							self.place_label_lager(self.item_name, self.frame_position)
							#self.lager_list.append(self.place_label(self.item_name, self.frame_position))
					self.frame_position += 1
			except:
				pass

	def lager(self, name, remove):
		self.inventory_num_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//lager.txt", "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inventory_num_list.append(self.tmp_var)
		f.close()

		#Remove one from the list, Atomic 2 to Atomic 1
		#X is the number, and J is the name in the list
		for x, j in enumerate(self.inventory_num_list):
			#print "J0 = " + j[0] + " : Name is " + name
			#added name == J[0] + "," because some items in the list have a , added at the end
			if j[0] == name or name == j[0] + ",":
				if remove:
					self.new_value = int(j[1])
					self.new_value -= 1
					self.inventory_num_list[x][0] = j[0] + ", "
					self.inventory_num_list[x][1] = str(self.new_value) + "\n"
				else:
					#print self.inventory_num_list[x]
					self.inventory_num_list[x][0] = j[0] + ","
					#print self.inventory_num_list[x<][0]
					self.return_inv_num = self.inventory_num_list[x][1]
			else:
				self.inventory_num_list[x][0] = j[0] + ","

			with open("logs//lager.txt", "w+") as f:
				for x in self.inventory_num_list:
					for j in x:
						f.write(j)
		if not remove:
			#print self.return_inv_num
			return self.return_inv_num

	def place_label_lager(self, name, frame_pos):
		self.label_text = self.lager(name, False).strip()
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
		# self.btn = tk.Button(self.frame, height = 5, width = 15, command = lambda : self.add(name, price), bg = "white")
		# self.photo = ImageTk.PhotoImage(file = "rz/" + name + "_liten.png")
		# self.btn.config(image = self.photo, width = 150, height = 150)
		# self.btn.image = self.photo
		# self.btn.grid(row = y_pos, column = x_pos, padx = 50, pady = 50)
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "ADD", bg = "red",  command = lambda : [self.add_sum(name, price), self.change_amount(name, frame_pos, True), self.add_to_checkout(name, price, frame_pos)])
		self.button_place.place(relx = .5, rely = .5, anchor = "center")
		#self.text.grid(row = 0, column = 0)

	def place_button_minus(self, name, price, frame_pos):
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "MINUS", bg = "red",  command = lambda : [self.minus_sum(name, price), self.change_amount(name, frame_pos, False), self.remove_from_checkout(name, price, frame_pos)])
		self.button_place.place(relx = .5, rely = .7, anchor = "center")


	def add_sum(self, name, price):
		print "Added " + name + " " + price
		self.total_sum += int(price)
		self.check_out_label.config(text = str(self.total_sum))
		#print self.total_sum

	def add_to_checkout(self, name, price, frame_pos):
		self.check_out_grid_list = []

		self.tmp_text_var = name + " (" + price.strip() + ")"
		self.item_check_out.append(self.tmp_text_var)
		#self.check_out_label.config(text = name + " " + price)
		for j, x in enumerate(self.item_check_out):
			self.tmp_text_label = tk.Label(self.check_out, text = x, width = self.label_width)
			self.tmp_text_label.grid(row = j+1, column = 0)

			self.check_out_grid_list.append(self.tmp_text_label)

	def minus_sum(self, name, price):
		#print "Removed " + name + " " + price
		self.total_sum -= int(price)
		#print self.total_sum

	def remove_from_checkout(self, name, price, frame_pos):
		self.items_removed = []

		for j, widget in enumerate(self.check_out.winfo_children()):
			widget.destroy()

		for j, x in enumerate(self.item_check_out):
			if name not in self.items_removed:
				if name in x:
					del self.item_check_out[j]
					del self.check_out_grid_list[j]
					self.items_removed.append(name)
			else:
				print "already removed"

		self.check_out_label = tk.Label(self.check_out, text = self.total_sum, width = self.label_width)
		self.check_out_label.grid(row = 0, column = 0, pady = (0, 50))

		for j, x in enumerate(self.item_check_out):
			self.tmp_text_label = tk.Label(self.check_out, text = x, width = self.label_width)
			self.tmp_text_label.grid(row = j+1, column = 0)

			self.check_out_grid_list.append(self.tmp_text_label)

		#Works

if __name__ == "__main__":
	strt = Nova()