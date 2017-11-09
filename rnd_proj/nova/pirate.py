import tkinter as tk
from PIL import ImageTk

#Resize images on buttons

class Example(tk.Frame):
	def __init__(self, root):

		tk.Frame.__init__(self, root)
		self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
		self.frame = tk.Frame(self.canvas, background="#ffffff")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
									tags="self.frame")

		self.frame.bind("<Configure>", self.onFrameConfigure)

		self.add_imgs()

	def add_imgs(self):
		self.inv_list = [["Atomic", "199"], ["Commando", "499"], ["Crossfire", "599"]]
		self.func_list = []
		self.y_pos = 0
		for row in range(50):
			self.y_pos += 1
			self.x_pos = 0
			for colums in range(3):
				self.x_pos += 1
				self.func_list.append(self.populate(self.inv_list[colums][0], self.inv_list[colums][1], self.x_pos, self.y_pos))

	def populate(self, name, price, x_pos, y_pos):
		self.btn = tk.Button(self.frame, height = 1, width = 5, command = lambda : self.add(name, price))
		self.photo = ImageTk.PhotoImage(file = name + "_liten.jpg")
		self.btn.config(image = self.photo, width = 50, height = 50)
		self.btn.image = self.photo
		self.btn.grid(row = y_pos, column = x_pos)

	def add(self, name, price):
		print name + " " + price

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1000x1000")
	Example(root).pack(side="top", fill="both", expand=True)
	root.mainloop()