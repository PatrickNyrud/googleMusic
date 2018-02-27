import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

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

        self.label_width = 30

        self.item_frame = tk.Frame(self.frame, bg = "yellow", width = 200, height = 1000 - 100) #self.y - topframe height

        self.check_out_label = tk.Label(self.item_frame, bg = "white", text = "0", width = self.label_width)
        self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

        self.check_out_button = tk.Button(self.item_frame, bg = "white", text = "DONE", command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
        self.check_out_button.grid(row = 1, column = 0, pady = (20, 0))

        self.reset_button = tk.Button(self.item_frame, bg = "white", text = "RESET",  command = lambda : self.reset())
        self.reset_button.grid(row = 1, column = 1, pady = (20, 0))

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
            self.tmp_lbl = tk.Label(self.item_frame, bg = "white", text = x, width = self.label_width)
            self.tmp_lbl.grid(row = j + 1, column = 0, columnspan = 2)

            self.check_out_grid_list.append(self.tmp_lbl)

        self.check_out_label.config(text = str(self.total_sum))

        self.check_out_button.grid_configure(row = j + 2)
        self.reset_button.grid_configure(row = j + 2)

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
        self.check_out_label = tk.Label(self.item_frame, bg = "white", text = self.total_sum, width = self.label_width)
        self.check_out_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 50))

        for j, x in enumerate(self.final_string):
            self.tmp_text_label = tk.Label(self.item_frame, bg = "white", text = x, width = self.label_width)
            self.tmp_text_label.grid(row = j + 1, column = 0, columnspan = 2)

            self.check_out_grid_list.append(self.tmp_text_label)

        self.check_out_button = tk.Button(self.item_frame, bg = "white", text = "DONE",  command = lambda : self.check_out_done(self.total_sum, self.items_check_out))
        self.check_out_button.grid(row = j + 2, column = 0, pady = (20, 0))

        self.reset_button = tk.Button(self.item_frame, bg = "white", text = "RESET",  command = lambda : self.reset())
        self.reset_button.grid(row = j + 2, column = 1, pady = (20, 0))

    def check_out_done(self, final_price, items):
        self.top_object.log_sale(items, self.log_folder, self.salgs_log, final_price)
        self.top_object.update_sum(self.log_folder, self.total_salg_sum, final_price)
        self.top_object.update_sum(self.log_folder, self.total_salg_sum_dag, final_price)
        self.top_object.display_total_sold()

        for x in items:
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


