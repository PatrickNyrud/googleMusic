import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
from PIL import Image, ImageTk

class items_frame():
    def initialize(self, frame, checkout_object):
        self.frame = frame
        self.scrollbar_canvas = tk.Canvas(self.frame, bg = "grey21", width = 1700)
        self.checkout_frame = tk.Frame(self.scrollbar_canvas, bg = "grey21", height = 1000 - 100) #self.y - topframe height

        self.log_folder = "logs//"
        self.pic_folder = "pics//svea_new//"
        self.lager_file = "lager.txt"
        self.prices = "priser.txt"

        self.in_frame_color = "AntiqueWhite1"

        self.checkout_object = checkout_object

        self.btn_font = tkFont.Font(family = "Helvetica", size = 25)
        self.text_font = tkFont.Font(family = "Helvetica", size = 15)
        self.amount_font = tkFont.Font(family = "Helvetica", size = 10)

        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
        self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)
        
        self.checkout_frame.pack(side = "right")

        self.vsb.pack(side="right", fill="both")

        self.scrollbar_canvas.pack(side = "right", fill = "y")
        self.scrollbar_canvas.create_window((4,4), window = self.checkout_frame, anchor="nw", tags="self.checkout_frame")

        self.checkout_frame.bind("<Configure>", self.onFrameConfigure)
        self.checkout_frame.bind("<MouseWheel>", self.OnMouseWheel)

        self.frame.bind("<Visibility>", self.draw_init)

    def onFrameConfigure(self, event):
        self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

    def OnMouseWheel(self,event):
        self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")


    def draw_init(self, event):
        self.frame_list = []
        self.label_list = []
        self.lager_list = []
        self.add_button_func = []
        self.minus_button_func = []
        self.amount_list = []

        self.checkout_frame.focus_set()

        for widget in self.checkout_frame.winfo_children():
            widget.destroy()

        self.inventory_price_list = self.pic_price_file(self.log_folder, self.prices)
        self.main_draw_func(self.inventory_price_list)

    def pic_price_file(self, dirr, file):
        self.inv_list = []
        with open(dirr + file, "r") as f:
            for x in f:
                self.tmp_var = x.split(",")
                self.inv_list.append(self.tmp_var)

        return self.inv_list

    def main_draw_func(self, price_list):
        self.column = 4
        self.item_in_frame = 5

        self.item_pos = 0
        self.frame_position = 0
        for row in range((len(price_list) / self.column) + 1):
            try: #for loop is longer than list, therefore we need a try to escape the error
                for column in range(self.column):
                    self.frame_list.append(self.place_frame(row, column))
                    self.item_name = price_list[self.item_pos][0]
                    self.item_price = price_list[self.item_pos][1]
                    self.item_pos += 1
                    for x in range(self.item_in_frame):
                        if x == 0:
                            #Text of the item
                            self.label_list.append(self.place_label_name(self.item_name, self.frame_position))
                            #self.place_labe_name(self.item_name, self.frame_position)
                        elif x == 1:
                            #THe add button
                            self.add_button_func.append(self.place_button_add(self.item_name, self.item_price, self.frame_position))
                        elif x == 2:
                            #The - button
                            self.minus_button_func.append(self.place_button_minus(self.item_name, self.item_price, self.frame_position))
                        elif x == 3:
                            #The amount of items
                            self.amount_list.append(self.place_amount_label(self.item_name, self.frame_position))
                        elif x == 4:
                            #The inv num
                            self.lager_list.append(self.place_label_lager(self.item_name, self.frame_position)) 
                    self.frame_position += 1
            except:
                pass


    def place_frame(self, rw, clm):
        self.item_frame = tk.Canvas(self.checkout_frame, bg = self.in_frame_color, height = 250, width = 250, highlightthickness = 5, highlightbackground = "gray6")
        self.item_frame.grid(row = rw, column = clm, padx = (42, 0), pady = (50, 0))
        
        return self.item_frame

    def place_label_name(self, name, frame_pos):
        self.tmp_label = tk.Label(self.frame_list[self.frame_position], font = self.text_font, bg = self.in_frame_color, text = self.item_name.upper())
        self.tmp_label.place(relx = .5, rely = .1, anchor = "center")
        
        return self.tmp_label

    def place_label_lager(self, name, frame_pos):
        self.label_text = self.inventory(name, False).strip()

        self.label_var = tk.Label(self.frame_list[frame_pos], bg = self.in_frame_color, text = "P" + "\xc3\xa5".decode("utf-8") +" lager (" + self.label_text + ")")
        self.label_var.place(relx = .5, rely = .9, anchor = "center")

        return self.label_var

    def place_amount_label(self, name, frame_pos):
        self.amount_var = tk.Label(self.frame_list[frame_pos], font = self.amount_font, bg = self.in_frame_color, text = "")
        self.amount_var.place(relx = .8, rely = .45, anchor = "center")

        return self.amount_var

    def change_amount(self, name, frame_pos, add):
        self.change_var = self.amount_list[frame_pos]
        self.change_text = self.change_var.cget("text")
        if add:
            if len(self.change_text) < 2:
                self.change_var.config(text = "x1")
            else:
                self.change_text_int = int(self.change_text.strip("x"))
                self.change_text_int += 1
                self.change_var.config(text = "x" + str(self.change_text_int))
        else:
            if self.change_text == "x1" or self.change_text == "":
                self.change_var.config(text = "")
            else:
                self.change_text_int = int(self.change_text.strip("x"))
                self.change_text_int -= 1
                self.change_var.config(text = "x" + str(self.change_text_int))

    def reset_amount(self, frame_pos):
        for x in frame_pos:
            self.amount_list[int(x)].config(text = "")

    def place_button_add(self, name, price, frame_pos):
        self.button_add_place = tk.Button(self.frame_list[frame_pos], bg = "white", text = "ADD", borderwidth = 2, command = lambda : [self.change_amount(name, frame_pos, True), self.checkout_object.add_to_checkout(name, price, frame_pos)])
        self.photo = ImageTk.PhotoImage(file = self.pic_folder + name + ".jpg")
        self.button_add_place.config(image = self.photo, width = 150, height = 150)
        self.button_add_place.image = self.photo
        self.button_add_place.place(relx = .35, rely = .5, anchor = "center")

        return self.button_add_place

    def place_button_minus(self, name, price, frame_pos):
        self.button_minus_place = tk.Button(self.frame_list[frame_pos], text = "-", width = 3, font = self.btn_font, bg = "ivory2",  command = lambda : [self.change_amount(name, frame_pos, False), self.checkout_object.remove_from_checkout(name, price)])
        self.button_minus_place.place(relx = .8, rely = .67, anchor = "center")

        return self.button_minus_place

    def inventory(self, name, remove):
        self.inventory_num_list = []
        #Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
        with open("logs//lager.txt", "r") as f:#self.log_folder + self.lager_file
            for x in f:
                self.tmp_var = x.split(",")
                self.inventory_num_list.append(self.tmp_var)
        f.close()

        if remove:
            self.ch_remove = "'[]"
            for j, x in enumerate(self.inventory_num_list):
                if x[0] in name:
                    self.remove_inv_sum = self.inventory_num_list[j][1]
                    if int(self.remove_inv_sum) > 0:
                        self.new_sum = int(self.remove_inv_sum) - 1
                        if self.new_sum == 0:
                            self.sold_out(name)
                        self.lager_list[j].config(text = "P" + "\xc3\xa5".decode("utf-8") +" lager (" + str(self.new_sum) + ")")
                        self.inventory_num_list[j][1] = str(self.new_sum) + "\n"
                        with open(self.log_folder + self.lager_file, "w") as f:
                            for x in self.inventory_num_list:
                                x[1] = x[1].strip(" ")
                                self.final_inv_string = str(x)
                                for c in self.ch_remove:
                                    self.final_inv_string = self.final_inv_string.replace(c, "")
                                f.write(self.final_inv_string.replace("\\n", "\n"))
                    else:
                        pass
        else:
            for x in self.inventory_num_list:
                if x[0] == name:
                    return x[1].strip()

    def sold_out(self, name):
        self.time_date = time.strftime("%d %b %Y %H:%M")
        with open("logs//sold_out.txt", "a") as f:
            f.write("Sold out of " + name + " at " + self.time_date + "\n\n")
        f.close()


