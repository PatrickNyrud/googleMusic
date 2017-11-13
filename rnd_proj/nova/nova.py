import tkinter as tk
from PIL import ImageTk

#Resize images on buttons
#Check out button next to reset
#Pop up window with every item

class Nova(tk.Frame):
	def __init__(self, root):

		tk.Frame.__init__(self, root)
		self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
		self.frame = tk.Frame(self.canvas, background="#ffffff")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.vsb.pack(side="right", fill="both")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
									tags="self.frame")

		self.total_sum = []
		self.items = []

		self.frame.bind("<Configure>", self.onFrameConfigure)

		self.add_imgs()


	def add_imgs(self):
		self.inv_list = [["Atomic", "199"], ["Superti", "329"], ["Magnum", "499"], ["xtrem", "1599"], ["Flashlight", "599"]
		, ["Phoenix", "599"], ["Bolero", "599"], ["Circus", "599"], ["Bizarre", "599"], ["Goldfish", "599"]
		, ["Orion", "599"], ["Trapez", "599"], ["Passion", "599"], ["Tnt", "599"], ["Tbird", "599"]
		, ["Commando", "599"], ["Shocker", "599"], ["Gladiator", "599"], ["Crossfire", "599"], ["Firestorm", "599"]
		, ["Dragonstep", "599"], ["Hellfire", "599"], ["Diablo", "599"], ["Kickass", "599"], ["Vipblackline", "599"], ["Monster", "599"]
		, ["Eagle", "599"], ["Monsterpack", "599"], ["Nighthawk", "599"], ["Strobe", "599"], ["Thunderbolt", "599"]
		, ["Topflight", "599"], ["Partymix", "599"], ["Smatt", "599"], ["Stjerneskudd", "599"], ["Stjerneskuddmini", "599"]
		, ["Stormlighter", "599"], ["Tikroner", "599"], ["Lyxfontene", "599"], ["Handfakkel", "599"], ["Fargefontene", "599"]]
		self.func_list = []
		self.y_pos = 0
		self.img_pos = -1
		for row in range((len(self.inv_list) / 3) + 1):
			self.y_pos += 1
			self.x_pos = 0
			try:
				for colums in range(3):
					self.img_pos += 1
					self.x_pos += 1
					self.func_list.append(self.populate(self.inv_list[self.img_pos][0], self.inv_list[self.img_pos][1], self.x_pos, self.y_pos))
			except:
				pass


		self.checkout_button = tk.Button(self.frame, text = "CHECK OUT", height = 10, width = 20, command = lambda : self.check_out())
		self.checkout_button.grid(row = self.y_pos + 1, column = 2, pady = 50)

		self.reset_button = tk.Button(self.frame, text = "RESET", height = 10, width = 20, command = lambda : self.reset())
		self.reset_button.grid(row = self.y_pos + 1, column = self.x_pos, pady = 50)

	def populate(self, name, price, x_pos, y_pos):
		self.btn = tk.Button(self.frame, height = 1, width = 5, command = lambda : self.add(name, price))
		self.photo = ImageTk.PhotoImage(file = name + "_liten.jpg")
		self.btn.config(image = self.photo, width = 150, height = 150)
		self.btn.image = self.photo
		self.btn.grid(row = y_pos, column = x_pos, padx = 50, pady = 50)

	def add(self, name, price):
		self.tmp = 0
		print name + " " + price
		self.total_sum.append(int(price))
		self.items.append(name)
		for x in self.total_sum:
			self.tmp += x

		print self.tmp

	def reset(self):
		del self.total_sum[:]

	def check_out(self):
		self.main = tk.Toplevel(self)
		self.main.geometry("300x300")
		self.main.title("Check Out")
		self.sum = tk.Label(self.main, text = str(self.tmp))
		self.sum.place(relx = .5, rely = .5, anchor = "center")

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1000x1000")
	Nova(root).pack(side="top", fill="both", expand=True)
	root.mainloop()