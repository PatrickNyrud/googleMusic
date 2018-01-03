try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time


class Nova():
	def __init__(self):
		self.x = 1000
		self.y = 1000
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

		#--------------------------------------------------SCROLLBAR--------------------------------------------------#



		#--------------------------------------------------SCROLLBAR--------------------------------------------------#


		self.top = tk.Label(self.top_frame, text = "TOP")
		self.top.place(relx = .5, rely = .5, anchor = "center")

		self.check = tk.Label(self.check_out, text = "CHECK OUT")
		self.check.place(relx = .5, rely = .5, anchor = "center")

		self.main = tk.Label(self.main_frame, text = "MAIN")
		self.main.place(relx = .5, rely = .5, anchor = "center")

		#self.top_frame.grid(row = 0, column = 0, columnspan = 2)
		#self.check_out.grid(row = 1, column = 0, sticky = "wens")
		#elf.main_frame.grid(row = 1, column = 1, sticky = "ens")

		self.top_frame.pack(side = "top", fill = "both")	
		self.check_out.pack(side = "left", expand = False) 
		self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.vsb.pack(side="right", fill="both")
		self.main_canvas.pack(side="left", fill="both", expand=True)
		self.main_canvas.create_window((4,4), window=self.main_frame, anchor="nw", 
									tags="self.main_frame")

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.inv_list = [["Atomic", "199"], ["Superti", "349"], ["Magnum", "449"], ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"]
		, ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"]
		, ["Phoenix", "1199"], ["Phoenix", "1199"], ["Phoenix", "1199"]]
	

		self.main_frame.bind("<Configure>", self.onFrameConfigure)

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
							pass
						elif x == 3:
							#The amount of items
							pass
						elif x == 4:
							#The inv num
							pass
					self.frame_position += 1
			except:
				pass

	def place_button_add(self, name, price, frame_pos):
		# self.btn = tk.Button(self.frame, height = 5, width = 15, command = lambda : self.add(name, price), bg = "white")
		# self.photo = ImageTk.PhotoImage(file = "rz/" + name + "_liten.png")
		# self.btn.config(image = self.photo, width = 150, height = 150)
		# self.btn.image = self.photo
		# self.btn.grid(row = y_pos, column = x_pos, padx = 50, pady = 50)
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "ADD", bg = "red",  command = lambda : self.add_sum(name, price))
		self.button_place.place(relx = .5, rely = .5, anchor = "center")
		#self.text.grid(row = 0, column = 0)

	def place_button_minus(self, name, price, frame_pos):
		self.button_place = tk.Button(self.frame_list[frame_pos], text = "MINUS", bg = "red",  command = lambda : self.minus_sum(name, price))
		self.button_place.place(relx = .5, rely = .7, anchor = "center")


	def add_sum(self, name, price):
		print name + " " + price

	def minus_sum(self, name, price):
		print name + " " + price

if __name__ == "__main__":
	strt = Nova()