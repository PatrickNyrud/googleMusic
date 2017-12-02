try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
from PIL import ImageTk


class Nova(tk.Frame):
	def __init__(self, root):

		tk.Frame.__init__(self, root)
		self.top_frame = tk.Frame(root, bg = "yellow")
		self.canvas = tk.Canvas(root, borderwidth=0, background="red")
		self.frame = tk.Frame(self.canvas, background="black")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.display_text = tkFont.Font(family = "Helvetica", size = 20)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.lbl = tk.Label(self.top_frame, text = "0", font = self.display_text)
		self.lbl.pack()

		self.top_frame.pack(side = "top", fill = "both")
		self.vsb.pack(side="right", fill="both")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
									tags="self.frame")

		self.total_sum = []
		self.items = []
		self.tmp_sum = 0

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
		for row in range((len(self.inv_list) / 3) + 1): #+1 if num of colums is odd, no +1 if its even
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
		self.btn = tk.Button(self.frame, height = 1, text = name, width = 5, command = lambda : self.add(name, price))
		#self.photo = ImageTk.PhotoImage(file = "rz/" + name + "_liten.png")
		#self.btn.config(image = self.photo, width = 150, height = 150)
		#self.btn.image = self.photo
		self.btn.grid(row = y_pos, column = x_pos, padx = 50, pady = 50)

	def add(self, name, price):
		print name + " " + price
		self.items.append([name, price])

		self.tmp_sum += int(price)

		print self.tmp_sum

		self.lbl.config(text = self.tmp_sum)


	def reset(self):
		self.tmp_sum = 0
		del self.total_sum[:]
		del self.items[:]
		self.lbl.config(text = "0")

	def check_out(self):
		self.main = tk.Toplevel(self)
		self.main.geometry("300x400")
		self.main.title("Check Out")

		self.checkd_items = []
		self.final_items_text = []
		for x in self.items:
			if x in self.checkd_items:
				pass
			else:
				self.checkd_items.append(x)
				self.ttsum = 0
				for j in self.items:
					if x == j:
						self.ttsum += 1
				self.final_items_text.append("\n" + x[0] + " x" + str(self.ttsum) + " (" + x[1] + " kr)")

		for x, j in enumerate(self.final_items_text):
			self.item_text = tk.Label(self.main, text = j, font = self.window_text)
			self.item_text.grid(row = x, column = 1)

		if len(self.final_items_text) >= 7:
			self.row_place = 1
			self.btn_place = x + 1
		else:
			self.row_place = x + 1
			self.btn_place = x + 2

		self.sum = tk.Label(self.main, text = str(self.tmp_sum) + " kr", font = self.window_text)
		self.sum.grid(row = self.row_place, column = 2)

		self.main.grid_rowconfigure(x + 1, minsize=80)

		self.exit = tk.Button(self.main, text = "EXIT", bg = "white", height = 2, width = 10)
		self.exit.grid(row = self.btn_place, column = 2)

		self.reset()

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
	root = tk.Tk()
	#root.geometry("1000x1000")
	root.attributes("-fullscreen", True)
	Nova(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
