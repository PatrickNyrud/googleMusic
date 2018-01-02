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

		self.top_frame = tk.Frame(root, bg = "green", height = self.top_frame_height, width = self.y)
		self.check_out = tk.Frame(root, background="red", width = self.check_out_width, height = self.x - self.top_frame_height)
		self.main_frame = tk.Frame(root, background="yellow", width = self.x - self.check_out_width, height = self.x - self.top_frame_height)	

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
		self.check_out.pack(side = "left", expand = False) #Fill only x, set height
		self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)
	
		self.place_frame()
		self.place_text()

		root.mainloop()

	def place_frame(self):
		self.frame_list = []


		for row in range(4):
			for column in range(3):
				self.frame = tk.Canvas(self.main_frame, bg = "black", height = 100, width = 100)
				self.frame.grid(row = row, column = column, padx = (50, 0), pady = (50, 0))

				self.frame_list.append(self.frame)

	def place_text(self):
		self.text_x = 0
		for row in range(4):
			for column in range(3):
				self.text = tk.Label(self.frame_list[self.text_x], text = "Hey", bg = "red")
				self.text.place(relx = .5, rely = .5, anchor = "center")
				self.text_x += 1


if __name__ == "__main__":
	strt = Nova()