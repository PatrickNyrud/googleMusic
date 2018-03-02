import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

#Move buttons to the bottom of checkout, always there statc

class checkout_frame:
    def initialize(self, frame, items_object, top_object):
        self.frame = frame
        self.items_object = items_object
        self.top_object = top_object

        self.items_check_out = []
        self.frame_pos_list = []

        self.now_date = time.strftime("%d_%b_%Y")
        self.log_folder = "logs//"
        self.salgs_log = "salgs_log.txt"
        self.total_salg_sum = "total_salg_sum.txt"
        self.total_salg_sum_dag = "total_salg_sum_" + self.now_date + ".txt"

        self.total_sum = 0

        self.text_font = tkFont.Font(family = "Helvetica", size = 18)
        
        self.label_width = 20

        self.item_frame = tk.Frame(self.frame, bg = "grey21", width = 290, height = 1000-50, highlightthickness = 2.0, highlightbackground = "grey37") #self.y - topframe height

        self.check_out_label = tk.Label(self.item_frame, bg = "grey21", fg = "cornsilk2", text = "0", font = self.text_font, width = self.label_width)
        self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (10, 50))
   
        self.return_label = tk.Label(self.item_frame, text = "", bg = "grey21", fg = "cornsilk2")
        self.return_label.grid(row = 1, column = 0, columnspan = 2, pady = (40, 0))

        self.return_entry = tk.Entry(self.item_frame, justify = "center", bg = "white", width = 35)
        self.return_entry.grid(row = 2, column = 0, columnspan = 2)
        self.return_entry.bind("<Return>", self.display_return_sum)

        self.check_out_button = tk.Button(self.item_frame, bg = "ivory2", width = 10, height = 2, text = "DONE", command = lambda : self.check_out_done(self.total_sum, self.items_check_out, self.final_string))
        self.check_out_button.grid(row = 3, column = 0, pady = (30, 0))

        self.reset_button = tk.Button(self.item_frame, bg = "ivory2", width = 10, height = 2, text = "RESET",  command = lambda : self.reset())
        self.reset_button.grid(row = 3, column = 1, pady = (30, 0))

        self.item_frame.grid_propagate(False)
        self.item_frame.pack(side = "left", fill = "y")

    def add_to_checkout(self, name, price, frame_pos):
        self.items_check_out.append(name)
        self.frame_pos_list.append(frame_pos)
        self.items_checked = []
        self.final_string = []
        self.check_out_grid_list = []

        self.total_sum += int(price)

        for x in self.items_check_out:
            if x in self.items_checked:
                pass
            else:
                self.items_checked.append(x)
                self.x_amount = 0
                for j in self.items_check_out:
                    if x == j:
                        self.x_amount += 1
                self.final_string.append(x + " x" + str(self.x_amount))


        for j, x in enumerate(self.final_string):
            self.tmp_lbl = tk.Label(self.item_frame, bg = "grey21", fg = "cornsilk2", text = x, font = self.text_font, width = self.label_width)
            self.tmp_lbl.grid(row = j + 1, column = 0, columnspan = 2)

            self.check_out_grid_list.append(self.tmp_lbl)

        self.check_out_label.config(text = str(self.total_sum) + " Kr")

        self.return_label.grid_configure(row = j + 2)
        self.return_entry.grid_configure(row = j + 3)
        self.check_out_button.grid_configure(row = j + 4)
        self.reset_button.grid_configure(row = j + 4)

    def remove_from_checkout(self, name, price):
        for widget in self.item_frame.winfo_children():
            widget.destroy()

        if len(self.items_check_out) > 0:
            #self.total_sum -= int(price)
            for j, x in enumerate(self.final_string):
                if name in x:
                    self.total_sum -= int(price)
                    del self.items_check_out[j]
                    self.change_string = list(self.final_string[j])
                    self.change_string[len(self.change_string) - 1] = str(int(self.change_string[len(self.change_string) - 1]) - 1)
                    if self.change_string[-1] > "0":
                        self.new_string = "".join(self.change_string)
                        self.final_string[j] = self.new_string
                    else:
                        del self.final_string[j]
                else: 
                    pass
        else:
            pass

        self.re_draw()

    def re_draw(self):
        j = 0
        self.check_out_label = tk.Label(self.item_frame, bg = "grey21", fg = "cornsilk2", text = self.total_sum, font = self.text_font, width = self.label_width)
        self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (10, 50))

        for j, x in enumerate(self.final_string):
            self.tmp_text_label = tk.Label(self.item_frame, bg = "grey21", fg = "cornsilk2", text = x, width = self.label_width, font = self.text_font)
            self.tmp_text_label.grid(row = j + 1, column = 0, columnspan = 2)

            self.check_out_grid_list.append(self.tmp_text_label)

        self.return_label = tk.Label(self.item_frame, text = "", bg = "grey21", fg = "cornsilk2")
        self.return_label.grid(row = 1, column = 0, columnspan = 2, pady = (40, 0))

        self.return_entry = tk.Entry(self.item_frame, justify = "center", bg = "white", width = 35)
        self.return_entry.grid(row = 2, column = 0, columnspan = 2)
        self.return_entry.bind("<Return>", self.display_return_sum)

        self.check_out_button = tk.Button(self.item_frame, bg = "ivory2", width = 10, height = 2, text = "DONE", command = lambda : self.check_out_done(self.total_sum, self.items_check_out, self.final_string))
        self.check_out_button.grid(row = 3, column = 0, pady = (30, 0))

        self.reset_button = tk.Button(self.item_frame, bg = "ivory2", width = 10, height = 2, text = "RESET",  command = lambda : self.reset())
        self.reset_button.grid(row = 3, column = 1, pady = (30, 0))

    def display_return_sum(self, event):
        self.return_sum = int(self.return_entry.get()) - self.total_sum
        self.return_label.config(text = str(self.return_sum) + " Tilbake")

    def check_out_done(self, final_price, remove_items, items):
        self.top_object.log_sale(items, self.log_folder, self.salgs_log, final_price)
        self.top_object.update_sum(self.log_folder, self.total_salg_sum, final_price)
        self.top_object.update_sum(self.log_folder, self.total_salg_sum_dag, final_price)
        self.top_object.display_total_sold()

        for x in remove_items:
            self.items_object.inventory(x, True)

        self.reset()


    def reset(self):
        for widget in self.item_frame.winfo_children():
            widget.destroy()

        self.items_object.reset_amount(self.frame_pos_list)

        self.frame_pos_list = []
        self.items_checked = []
        self.items_check_out = []
        self.check_out_grid_list = []
        self.final_string = []

        self.total_sum = 0

        self.re_draw()


