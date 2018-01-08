try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time

#Clean up things, the nova class
#Figure a way to update the storage list


class Nova():
	def __init__(self):
		self.x = 1200
		self.y = 800
		self.check_out_width = 200 #Tune this when change geo size
		self.top_frame_height = 20 #Tune this when change geo size
		root = tk.Tk()
		root.geometry(str(self.x) + "x" + str(self.y))

		self.top_frame = tk.Frame(root, bg = "black", height = self.top_frame_height, width = self.y)
		self.check_out = tk.Frame(root, background="red", width = self.check_out_width, height = self.x - self.top_frame_height)
		self.main_canvas = tk.Canvas(root, background="yellow")
		self.main_frame = tk.Frame(self.main_canvas, bg = "green")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.main_canvas.yview)
		self.main_canvas.configure(yscrollcommand=self.vsb.set)

		#-----------------------------TEMP STUFF-----------------------------#

		self.top = tk.Label(self.top_frame, text = "TOP")
		self.top.place(relx = .5, rely = .5, anchor = "center")

		self.check = tk.Label(self.check_out, text = "CHECK OUT")
		self.check.place(relx = .5, rely = .5, anchor = "center")

		self.main = tk.Label(self.main_frame, text = "MAIN")
		self.main.place(relx = .5, rely = .5, anchor = "center")

		#-----------------------------TEMP STUFF-----------------------------#

		self.top_frame.pack(side = "top", fill = "both")	
		self.check_out.pack(side = "left", expand = False) 
		self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.vsb.pack(side="right", fill="both")
		self.main_canvas.pack(side="left", fill="both", expand=True)
		self.main_canvas.create_window((4,4), window=self.main_frame, anchor="nw", tags="self.main_frame")

		self.main_frame.bind("<Configure>", self.onFrameConfigure)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.inv_list = [["Atomic", "199"], ["Super 10", "349"], ["Magnum", "449"], ["Bolero", "1199"], ["Circus", "1199"], ["Bizarre", "1199"]
		, ["Goldfish", "1199"], ["Orion", "1199"], ["Trapez", "1199"], ["Passion", "1199"], ["Tnt", "1199"], ["Thunderbird", "1199"]
		, ["Commando", "1199"], ["Shocker", "1199"], ["Kamikaze", "1199"]]
	

		self.place_frame()
		#self.place_text()

		root.mainloop()

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))


	def place_frame(self):
		self.frame_list = []
		self.add_button_func = []
		self.minus_button_func = []
		self.label_list = []
		self.amount_list = []
		#self.lager_list = []

		self.row = 2
		self.column = 3
		self.item_in_frame = 5

		self.item_pos = 0
		self.frame_position = 0
		for row in range((len(self.inv_list) / self.column) + 1):
			try: #for loop is longer than list, therefore we need a try to escape the error
				for column in range(self.column):
					self.frame = tk.Canvas(self.main_frame, bg = "black", height = 200, width = 200)
					self.frame.grid(row = row, column = column, padx = (50, 0), pady = (50, 0))
					self.frame_list.append(self.frame)
					self.item_name = self.inv_list[self.item_pos][0]
					self.item_price = self.inv_list[self.item_pos][1]
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
							self.add_button_func.append(self.place_button_add(self.item_name, self.item_price, self.frame_position))
						elif x == 2:
							#The - button
							self.minus_button_func.append(self.place_button_minus(self.item_name, self.item_price, self.frame_position))
							#print self.minus_button_func
						elif x == 3:
							#The amount of items
							self.place_amount_label(self.item_name, self.frame_position)
							#self.amount_list.append(self.place_amount_label(self.item_name, self.frame_position))
							#print self.amount_list
						elif x == 4:
							#The inv num
							self.place_lager_label(self.item_name, self.frame_position)
							#self.lager_list.append(self.place_lager_label(self.item_name, self.frame_position))
							#print self.lager_list
					self.frame_position += 1
			except:
				pass

	def place_amount_label(self, name, frame_pos):
		self.label_var = tk.Label(self.frame_list[frame_pos], text = "x2")
		self.label_var.place(relx = .8, rely = .7, anchor = "center")

		self.amount_list.append(self.label_var)

	def change_amount(self, name, frame_pos):
		self.change_var = self.amount_list[frame_pos]
		self.change_var.config(text = "hgi")

	def place_lager_label(self, name, frame_pos):
		self.lager_list = []
		self.label_text = self.lager(name, False, frame_pos).strip()
		self.lager_var = tk.Label(self.frame_list[frame_pos], text = self.label_text)
		self.lager_var.place(relx = .5, rely = .9, anchor = "center")

		self.lager_list.append(self.lager_var)

	def lager(self, name, remove, frame_pos):
		self.inv_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//lager.txt", "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)
		f.close()

		#Remove one from the list, Atomic 2 to Atomic 1
		#X is the number, and J is the name in the list
		for x, j in enumerate(self.inv_list):
			#print "J0 = " + j[0] + " : Name is " + name
			#added name == J[0] + "," because some items in the list have a , added at the end of its name
			if j[0] == name or name == j[0] + ",":
				if remove:
					self.new_value = int(j[1])
					self.new_value -= 1
					self.inv_list[x][0] = j[0] + ", "
					self.inv_list[x][1] = str(self.new_value) + "\n"
				else:
					#print self.inv_list[x]
					self.inv_list[x][0] = j[0] + ","
					self.return_inv_num = self.inv_list[x][1]
			else:
				self.inv_list[x][0] = j[0] + ","

			with open("logs//lager.txt", "w+") as f:
				for x in self.inv_list:
					for j in x:
						f.write(j)
		if remove:
			#self.place_lager_label()
			pass
		else:
			return self.return_inv_num


	def place_button_add(self, name, price, frame_pos):
		# self.btn = tk.Button(self.frame, height = 5, width = 15, command = lambda : self.add(name, price), bg = "white")
		# self.photo = ImageTk.PhotoImage(file = "rz/" + name + "_liten.png")
		# self.btn.config(image = self.photo, width = 150, height = 150)
		# self.btn.image = self.photo
		# self.btn.grid(row = y_pos, column = x_pos, padx = 50, pady = 50)
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "ADD", bg = "red",  command = lambda : [self.add_sum(name, price), self.change_amount(name, frame_pos)])
		self.button_place.place(relx = .5, rely = .5, anchor = "center")
		#self.text.grid(row = 0, column = 0)

	def place_button_minus(self, name, price, frame_pos):
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "MINUS", bg = "red",  command = lambda : self.lager(name, True, frame_pos))
		self.button_place.place(relx = .5, rely = .7, anchor = "center")


	def add_sum(self, name, price):
		print name + " " + price

	def minus_sum(self, name, price):
		print name + " " + price

if __name__ == "__main__":
	strt = Nova()