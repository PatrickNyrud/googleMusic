import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

class top_frame:
    def initialize(self, frame, rt):
        self.root = rt
        self.frame = frame
        self.top_frame = tk.Frame(self.frame, bg = "red", height = 50)

        self.now_date = time.strftime("%d_%b_%Y")
        self.log_folder = "logs//"
        self.salgs_log = "salgs_log.txt"
        self.total_salg_sum = "total_salg_sum.txt"
        self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

        self.total_salg_label = tk.Label(self.top_frame, text = "", bg = "white")
        self.total_salg_dag_label = tk.Label(self.top_frame, text = "", bg = "white")

        self.time = tk.Label(self.top_frame, text = "", bg = "white")
        self.time.place(relx = .5, rely = .5, anchor = "center")

        self.total_salg_label.place(relx = .8, rely = .5, anchor = "center")
        self.total_salg_dag_label.place(relx = .2, rely = .5, anchor = "center")

        self.top_frame.pack(side = "top", fill = "x")

        self.display_total_sold()

    def update_time(self):
        self.now_time = time.strftime("%H:%M:%S")
        self.time.config(text = self.now_time)
        self.root.after(1000, self.update_time)

    def update_sum(self, dest, file, final_price):
        with open(dest + file, "r+") as f:
            self.current_sum = f.read()
            self.new_sum = final_price + int(self.current_sum)
            f.seek(0)
            f.write(str(self.new_sum))
        f.close()

    def log_sale(self, items, dest, file, final_price):
        with open(dest + file, "a") as f:
            f.write(str(time.strftime("%d %b %Y %H:%M")) + "\n" +str(items) + " " + str(final_price) + " kr\n\n")
        f.close()


    def display_total_sold(self):#self.log_folder + self.total_salg_sum
        if not os.path.isfile(self.log_folder + self.total_salg_sum_dag):
            with open(self.log_folder + self.total_salg_sum_dag, "w") as f:
                f.write("0")
            f.close()
        else:
            with open(self.log_folder + self.total_salg_sum_dag, "r+") as salg_dag, open(self.log_folder + self.total_salg_sum, "r") as salg_total:
                self.total_salg_label.config(text = salg_total.read())
                self.total_salg_dag_label.config(text = salg_dag.read())
            salg_dag.close()
            salg_total.close()

