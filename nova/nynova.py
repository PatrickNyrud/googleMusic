try:
        import tkinter as tk
except:
        import Tkinter as tk
import tkFont
import time
from PIL import ImageTk

"""
CLEAN UP PROGRAM, such as open file in init, make a seperate program for it
Bigger text in check out
Add splitt screen, check out left of items in main window
self.inv_liste to a file, like in nova_lager.py
Add milestone for 5000kr, 10000kr osv
"""

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

		self.log_folder = "logs//"
		self.pic_folder = "rz//"
		self.prices = "priser.txt"
		self.salgs_log = "salgs_log.txt"
		self.tot_salg_sum = "total_salg_sum.txt"
		self.tot_salg_sum_dag = "total_salg_sum_dag.txt"

		with open("logs//total_salg_sum_dag.txt", "r") as f, open("logs//total_salg_sum.txt", "r") as f_two:
			self.dag_totsum = f.read()
			self.tot_sum = f_two.read()
		f.close()

		self.nomove_tot_sum_dag = tk.Label(self.top_frame, text = "(" + self.dag_totsum + " kr idag)", bg = "white")
		self.nomove_tot_sum_dag.place(relx = .8, rely = .2, anchor = "center")

		self.nomove_tot_sum_total = tk.Label(self.top_frame, text = "(" + self.tot_sum + " kr totalt)", bg = "white")
		self.nomove_tot_sum_total.place(relx = .8, rely = .6, anchor = "center")

		self.nomove_r = tk.Button(self.top_frame, text = "RESET", height = 3, width = 15, bg = "white", command = lambda : self.reset(False))
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

	def open_file(self, dirr, file):
		self.inv_list = []
		with open(dirr + file, "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)

		return self.inv_list


	def add_imgs(self):
		self.inventory_list = self.open_file(self.log_folder, self.prices)
		self.func_list = []
		self.y_pos = 0
		self.img_pos = -1
		for row in range((len(self.inventory_list) / 6) + 1): #+1 if the len(self.inventory_list) / 6 is not a whole number (6.83)
			self.y_pos += 1
			self.x_pos = 0
			try:
				for colums in range(6):
					self.img_pos += 1
					self.x_pos += 1
					self.func_list.append(self.populate(self.inventory_list[self.img_pos][0], self.inventory_list[self.img_pos][1], self.x_pos, self.y_pos))
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

		self.reset_button = tk.Button(self.frame, text = "RESET", height = 10, width = 20, command = lambda : self.reset(False), bg = "white")
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


	def reset(self, write):
		if write:
			now = time.strftime("%H:%M %d %b %Y")
			with open("logs//salgs_log.txt", "a") as f:
				f.write("\n\nSalg kl " + now + "\n" + str(self.items) + ": " + str(self.tmp_sum) + " kr")
			f.close()
		self.tmp_sum = 0
		del self.total_sum[:]
		del self.items[:]
		self.lbl.config(text = "0")

	def check_out(self):
		self.main = tk.Toplevel(self, bg = "white")
		self.main.geometry("350x700")
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
				self.final_items_text.append("\n" + x[0] + " x" + str(self.ttsum) + " (" + x[1].strip() + " kr)")

		for x, j in enumerate(self.final_items_text):
			self.item_text = tk.Label(self.itmframe, bg = "White", text = j, font = self.window_text)
			self.item_text.grid(row = x, column = 1)

		self.row_place = 1
		self.btn_place = x + 2

		self.sum = tk.Label(self.sumframe, bg = "white", text = str(self.tmp_sum) + " kr", font = self.window_text)
		self.sum.grid(row = self.row_place, column = 2)

		self.main.grid_rowconfigure(x + 1, minsize=80)

		self.give_back_sum = tk.Label(self.itmframe, bg = "white", font = self.window_text)
		self.give_back_sum.grid(row = self.btn_place - 1, column = 1, pady = (50, 0))

		self.return_entry = tk.Entry(self.itmframe, bg = "white", text = "Test", justify = "center", font = self.window_text)
		self.return_entry.grid(row = self.btn_place, column = 1, padx = (0, 10), ipady = 5)
		self.return_entry.delete(0, "end")

		self.get_return_button = tk.Button(self.itmframe, bg = "white", text = "Enter", height = 1, font = self.window_text, width = 10, command = lambda : self.return_sum(self.return_entry.get()))
		self.get_return_button.grid(row = self.btn_place, column = 2)

		self.done = tk.Button(self.itmframe, text = "DONE", bg = "white", height = 2, width = 10, font = self.window_text, command = lambda : [self.window_destroy(self.main), self.total_sale(self.tmp_sum), self.reset(True)])
		self.done.grid(row = self.btn_place + 2, column = 1, pady = (30, 0))

		self.tilbake = tk.Button(self.itmframe, text = "BACK", bg = "white", height = 2, width = 10, font = self.window_text, command = lambda : self.window_destroy(self.main))
		self.tilbake.grid(row = self.btn_place + 2, column = 2, pady = (30, 0))



		self.sumframe.pack()
		self.itmframe.pack()

		self.pot_return_sum = self.tmp_sum

	def total_sale(self, fin_sum):
		with open("logs//total_salg_sum.txt", "r") as f:
			self.read_sum = f.read()
			print self.read_sum
		f.close()
		with open("logs//total_salg_sum.txt", "w") as f:
			self.read_sum = int(self.read_sum)
			self.read_sum += int(fin_sum)
			self.nomove_tot_sum_dag.config(text = "(" + str(self.read_sum) + ")")
			f.write(str(self.read_sum))
		f.close()

	def return_sum(self, numbr):
		self.back_sum = (int(numbr) - self.pot_return_sum)
		self.give_back_sum.configure(text = str(self.back_sum) + " kr tilbake")


	def onFrameConfigure(self, event):
		'''Reset the scroll region to encompass the inner frame'''
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def window_destroy(self, window):
		window.destroy()


if __name__ == "__main__":
	root = tk.Tk()
	root.geometry("1920x1080")
	#root.attributes("-fullscreen", True)
	Nova(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
