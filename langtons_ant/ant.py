import Tkinter as tk
import time
import random

class board:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")

        self.canvas_list = []
        self.rec_list = []
        self.pos_list = []


        self.draw()
        self.pos = len(self.rec_list) / 2 + 5
        self.ant(self.pos)
        self.root.bind('<Return>', self.change)
        #(x0, y0, x1, y1, optins...)

        self.root.mainloop()

    def draw(self):
        self.colr = ["white", "black"]
        for x in range(10):
            for j in range(10):
                self.canvas = tk.Canvas(self.root, borderwidth = 1, width = 5, height = 5, highlightbackground = "black")
                self.rect = self.canvas.create_rectangle(0, 0, 61, 61, fill = "white")
                self.canvas.grid(row = x, column = j, padx = (10, 0), pady = (10, 0))
                
                self.pos_list.append(str(x) + ", " + str(j))
                self.canvas_list.append(self.canvas)
                self.rec_list.append(self.rect)

    def change(self, event):
        self.canvas_list[self.pos].itemconfig(self.rec_list[self.pos], fill = "black")

    def run(self):
        while 1:
            print "jes"

    def ant(self, pos):
        self.check_status = self.canvas_list[pos].itemcget(self.rec_list[pos], "fill")
        print self.pos_list[pos]
        if self.check_status == "white":
            print "border at " + str(pos) + " is white"
            self.positon = self.pos_list[pos]

        else:
            print "border is black"

if __name__ == "__main__":
    board()
