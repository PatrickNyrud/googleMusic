try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time


class Nova():
	def __init__(self):
		self.x = 400
		self.y = 400
		self.check_out_width = 80 #Tune this when change geo size
		self.top_frame_height = 20 #Tune this when change geo size
		root = tk.Tk()
		root.geometry(str(self.x) + "x" + str(self.y))

		self.top_frame = tk.Frame(root, bg = "green", height = self.top_frame_height, width = self.y)
		self.check_out = tk.Frame(root, background="red", width = self.check_out_width)
		self.main_frame = tk.Frame(root, background="yellow", width = self.x - self.check_out_width, height = self.x - self.top_frame_height)	

		self.top = tk.Label(self.top_frame, text = "TOP")
		self.top.place(relx = .5, rely = .5, anchor = "center")

		self.check = tk.Label(self.check_out, text = "CHECK OUT")
		self.check.place(relx = .5, rely = .5, anchor = "center")

		self.main = tk.Label(self.main_frame, text = "MAIN")
		self.main.place(relx = .5, rely = .5, anchor = "center")

		self.top_frame.grid(row = 0, column = 0, columnspan = 2)
		self.check_out.grid(row = 1, column = 0, sticky = "wens")
		self.main_frame.grid(row = 1, column = 1, sticky = "ens")

		#self.top_frame.pack(side = "top", fill = "both")	
		#self.check_out.pack(side = "left", expand = False) #Fill only x, set height
		#self.main_frame.pack(side = "right", fill = "both", expand = True)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)
	
		root.mainloop()

if __name__ == "__main__":
	strt = Nova()