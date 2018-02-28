import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

#Change so display sum shows like 50 000, 1 000, 14 000, 500 000 osv

class top_frame:
    def initialize(self, frame, rt):
        self.root = rt
        self.frame = frame
        self.top_frame = tk.Frame(self.frame, bg = "gray14", height = 50)

        self.now_date = time.strftime("%d_%b_%Y")
        self.log_folder = "logs//"
        self.salgs_log = "salgs_log.txt"
        self.total_salg_sum = "total_salg_sum.txt"
        self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

        self.time_font = tkFont.Font(family = "Helvetica", size = 30)
        self.text_font = tkFont.Font(family = "Helvetica", size = 10)
        
        self.total_salg_label = tk.Label(self.top_frame, text = "", bg = "grey14", fg = "cornsilk2", font = self.text_font)
        self.total_salg_dag_label = tk.Label(self.top_frame, text = "", bg = "grey14", fg = "cornsilk2", font = self.text_font)

        self.time = tk.Label(self.top_frame, text = "", bg = "grey14", fg = "cornsilk2", font = self.time_font)
        self.time.place(relx = .5, rely = .5, anchor = "center")

        self.total_salg_label.place(relx = .8, rely = .3, anchor = "w")
        self.total_salg_dag_label.place(relx = .8, rely = .7, anchor = "w")

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
            f.write("\n\n" + str(items) + " " + str(final_price) + "kr\n" + str(time.strftime("%d %b %Y %H:%M")))
            #f.write(str(time.strftime("%d %b %Y %H:%M")) + "\n" +str(items) + " " + str(final_price) + " kr\n\n")
        f.close()


    def display_total_sold(self):#self.log_folder + self.total_salg_sum
        if not os.path.isfile(self.log_folder + self.total_salg_sum_dag):
            with open(self.log_folder + self.total_salg_sum_dag, "w") as f:
                f.write("0 Kr")
            f.close()
        else:
            with open(self.log_folder + self.total_salg_sum_dag, "r+") as salg_dag, open(self.log_folder + self.total_salg_sum, "r") as salg_total:
                self.total_salg_label.config(text = "Total solgt: " + salg_total.read() + " Kr")
                self.total_salg_dag_label.config(text = "Total solgt idag: " + salg_dag.read() + " Kr")
            salg_dag.close()
            salg_total.close()

