try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time


class Nova():
	def __init__(self):
		root = tk.Tk()
		root.geometry("1000x1000")

		self.main_frame = tk.Frame(root, background="yellow")	

		#self.top_frame.pack(side = "top", fill = "both")	
		#self.check_out.pack(side = "left", expand = False) #Fill only x, set height
		self.main_frame.pack(side="top", fill="both", expand=True)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)
	
		#self.place_frame()

		root.mainloop()

	def place_frame(self):
		self.frame_list = []

		#self.y = -.1
		for row in range(4):
			#self.y += .1
			#self.x = -.1
			for column in range(3):
				#self.x += .1
				self.frame = tk.Canvas(self.main_frame, bg = "black", height = 10, width = 10)
				#self.frame.place(relx = self.x, rely =  self.y)
				self.frame.grid(row = row, column = column)

				self.frame_list.append(self.frame)


if __name__ == "__main__":
	strt = Nova()