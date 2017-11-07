from tkinter import *
import tkinter
import tkFont

root = tkinter.Tk()
root.configure(background = "white")
root.geometry("1000x1000")

dicboi = {"Atomic" : "199", "Commando" : "499", "Crossfire" : "599"}

class frame:
	def __init__(self):
		self.obj_li = []
		self.img_list = ["Atomic", "Commando", "Crossfire"]
		self.y_pos = 0
		for j in range(3):
			self.y_pos += .25
			self.x_pos = 0
			for x in range(3):
				self.x_pos += .25
				self.obj_li.append(img_button(self.x_pos, self.y_pos, self.img_list[x]))

class img_button:
	def __init__(self, x_pos, y_pos, image_name):
		self.btn = Button(root, height = 1, width = 5, command = lambda : self.add(image_name))
		self.btn.place(relx = x_pos, rely = y_pos)

	def add(self, art):
		print "added " + dicboi[art]

if __name__ == "__main__":
	strt = frame()
	root.mainloop()


"""EUREKA"""