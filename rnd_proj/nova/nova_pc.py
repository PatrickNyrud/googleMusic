try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
from PIL import ImageTk


class Nova(tk.Frame):
	def __init__(self, root):

		tk.Frame.__init__(self, root)
		self.top_frame = tk.Frame(root, bg = "white")
		self.canvas = tk.Canvas(root, borderwidth=0, background="white")
		self.frame = tk.Frame(self.canvas, background="white")
		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)

		self.display_text = tkFont.Font(family = "Helvetica", size = 35)
		self.window_text = tkFont.Font(family = "Helvetica", size = 12)

		self.lbl = tk.Label(self.top_frame, bg = "white", text = "0", font = self.display_text)
		self.lbl.pack()

		self.nomove_co = tk.Button(self.top_frame, text = "CHECK OUT", height = 3, width = 15, bg = "white", command = lambda : self.check_out())
		self.nomove_co.place(relx = .1, rely = .5, anchor = "center")

		self.nomove_r = tk.Button(self.top_frame, text = "RESET", height = 3, width = 15, bg = "white", command = lambda : self.reset())
		self.nomove_r.place(relx = .9, rely = .5, anchor = "center")


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
		self.inv_list = [["Atomic99", "99"], ["Atomic", "199"], ["Superti", "349"], ["Magnum", "449"], ["xtrem", "1499"], ["Flashlight", "749"]
		, ["Phoenix", "1199"], ["Bolero", "399"], ["Circus", "199"], ["Bizarre", "199"], ["Goldfish", "329"], ["Orion", "279"]
		, ["Trapez", "549"], ["Passion", "349"], ["Tnt", "99"], ["Tbird", "399"], ["Commando", "499"], ["Shocker", "599"], ["Kamikaze", "399"]
		, ["Gladiator", "799"], ["Crossfire", "599"], ["Blackspider", "749"], ["Firestorm", "599"], ["Hellfire", "999"], ["Aceshigh", "2499"]
		, ["Kickass", "1199"], ["Supernova", "1499"], ["Vipblackline", "1999"], ["Monster", "199"], ["Eagle", "249"], ["Monsterpack", "479"]
		, ["Nighthawk", "239"], ["Strobe", "599"], ["Thunderbolt", "399"], ["Nitrobag", "549"], ["Bigbag", "999"], ["Topflight", "999"]
		, ["Partymix", "199"], ["Stormlighter", "29"], ["Stjerneskudd", "49"], ["Stjerneskuddmini", "20"], ["Tjuefemkroner", "25"]
		, ["Tikroner", "10"], ["Glowstick", "5"], ["Lyxfontene", "69"], ["Handfakkel", "49"], ["Fargefontene", "99"]]
		self.func_list = []
		self.y_pos = 0
		self.img_pos = -1
		for row in range((len(self.inv_list) / 6) + 1): #+1 if the len(self.inv_list) / 6 is not a whole number (6.83)
			self.y_pos += 1
			self.x_pos = 0
			try:
				for colums in range(6):
					self.img_pos += 1
					self.x_pos += 1
					self.func_list.append(self.populate(self.inv_list[self.img_pos][0], self.inv_list[self.img_pos][1], self.x_pos, self.y_pos))
			except:
				pass


		self.checkout_button = tk.Button(self.frame, text = "CHECK OUT", height = 10, width = 20, command = lambda : self.check_out(), bg = "white")
		self.checkout_button.grid(row = self.y_pos + 1, column = 1, pady = 50)

		self.five_off = tk.Button(self.frame, text = "5% OFF", height = 10, width = 20, command = lambda : self.rabatt(1.05, "5%"), bg = "white")
		self.five_off.grid(row = self.y_pos + 1, column = 2, pady = 50)

		self.ten_off = tk.Button(self.frame, text = "10% OFF", height = 10, width = 20, command = lambda : self.rabatt(1.10, "10%"), bg = "white")
		self.ten_off.grid(row = self.y_pos + 1, column = 3, pady = 50)

		self.fifteen_off = tk.Button(self.frame, text = "15% OFF", height = 10, width = 20, command = lambda : self.rabatt(1.15, "15%"), bg = "white")
		self.fifteen_off.grid(row = self.y_pos + 1, column = 4, pady = 50)

		self.twenty_off = tk.Button(self.frame, text = "20% OFF", height = 10, width = 20, command = lambda : self.rabatt(1.20, "20%"), bg = "white")
		self.twenty_off.grid(row = self.y_pos + 1, column = 5, pady = 50)

		self.reset_button = tk.Button(self.frame, text = "RESET", height = 10, width = 20, command = lambda : self.reset(), bg = "white")
		self.reset_button.grid(row = self.y_pos + 1, column = 6, pady = 50)

	def rabatt(self, precent, name):
		self.tmp_sum = self.tmp_sum / precent

		self.items.append([name, "0"])

		self.lbl.config(text = self.tmp_sum)

	def populate(self, name, price, x_pos, y_pos):
		self.btn = tk.Button(self.frame, height = 5, width = 15, command = lambda : self.add(name, price), bg = "white")
		self.photo = ImageTk.PhotoImage(file = "rz/" + name + "_liten.png")
		self.btn.config(image = self.photo, width = 150, height = 150)
		self.btn.image = self.photo
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
		self.main = tk.Toplevel(self, bg = "white")
		self.main.geometry("300x400")
		self.main.title("Check Out")

		self.sumframe = tk.Frame(self.main)
		self.itmframe = tk.Frame(self.main, bg = "white")

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
			self.item_text = tk.Label(self.itmframe, bg = "White", text = j, font = self.window_text)
			self.item_text.grid(row = x, column = 1)

		if len(self.final_items_text) >= 7:
			self.row_place = 1
			self.btn_place = x + 1
		else:
			self.row_place = x + 1
			self.btn_place = x + 2

		self.sum = tk.Label(self.sumframe, bg = "white", text = str(self.tmp_sum) + " kr", font = self.window_text)
		self.sum.grid(row = self.row_place, column = 2)

		self.main.grid_rowconfigure(x + 1, minsize=80)

		self.exit = tk.Button(self.itmframe, text = "EXIT", bg = "white", height = 2, width = 10, command = lambda : self.window_destroy(self.main))
		self.exit.grid(row = self.btn_place, column = 2)

		self.sumframe.pack()
		self.itmframe.pack()

		self.reset()

	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def window_destroy(self, window):
		window.destroy()


if __name__ == "__main__":
	root = tk.Tk()
	#root.geometry("1000x1000")
	root.attributes("-fullscreen", True)
	Nova(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
