import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import svea_item

class config:
    def __init__(self, frame):
        self.frame = frame
        self.scrollbar_canvas = tk.Canvas(self.frame, bg = "grey21", width = 1700)
        self.main_frame = tk.Frame(self.frame, bg = "grey21", width = 50, height = 50)

        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
        self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)

        self.text_font = tkFont.Font(family = "Helvetica", size = 12)

        self.main_frame.pack(fill = "both", expand = True)

        self.vsb.pack(side="right", fill="both")

        self.scrollbar_canvas.pack(side = "right", fill = "y")
        self.scrollbar_canvas.create_window((4,4), window = self.main_frame, anchor="nw", tags="self.main_frame")

        self.main_frame.bind("<Configure>", self.onFrameConfigure)
        self.main_frame.bind("<MouseWheel>", self.OnMouseWheel)

        self.frame.bind("<Visibility>", self.draw_init)


    def draw_init(self, event):
        self.frame_list = []
        self.name_list = []
        self.price_list = []
        self.price_name_list = []
        self.inventory_list = []
        self.only_inv_list = []
        self.inv_name_list = []
        self.button_list = []

        self.main_frame.focus_set()

        for widget in self.main_frame.winfo_children():
                widget.destroy()

        self.main_draw_func()

    def onFrameConfigure(self, event):
        self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

    def OnMouseWheel(self,event):
        self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

    def main_draw_func(self):
        self.items_object = svea_item.items_frame()
        self.inv_list = self.items_object.pic_price_file("logs//", "priser.txt")

        self.column =6
        self.item_in_frame = 6

        self.item_pos = 0
        self.frame_position = 0
        for row in range((len(self.inv_list) / self.column) + 1):
            try: #for loop is longer than list, therefore we need a try to escape the error
                for column in range(self.column):
                    self.frame_list.append(self.place_frame(row, column))
                    self.item_pos += 1
                    for x in range(self.item_in_frame):
                        if x == 0:
                            self.name_list.append(self.place_name_label(self.frame_position, self.inv_list[self.frame_position][0], 0, 2))
                        elif x == 1:
                            self.price_name_list.append(self.place_label(self.frame_position, "Pris: ", 1, 1, 10, 60))
                        elif x == 2:
                            self.price_list.append(self.place_entry(self.frame_position, self.inv_list[self.frame_position][1].strip(), 1, 2, 0, 60))
                        elif x == 3:
                            self.inv_name_list.append(self.place_label(self.frame_position, "Antall:", 2, 1, 10, 10))
                        elif x == 4:
                            self.label_text = self.items_object.inventory(self.inv_list[self.frame_position][0], False)
                            self.inventory_list.append(self.place_entry(self.frame_position, self.label_text, 2, 2, 0, 10))
                        elif x == 5:
                            self.button_list.append(self.place_button(self.frame_position, self.inv_list[self.frame_position][0]))
                    self.frame_position += 1
            except:
                self.t = tk.Label(self.frame_list[self.frame_position], bg = "white", text = "PLACE SOME SHIT HERE?")
                self.t.place(relx = .5, rely = .5, anchor = "center")

    def place_only_inv(self, frame_pos, name):
        self.only_inv = tk.Button(self.frame_list[frame_pos], bg = "ivory2", text = "UPDATE", font = self.text_font, command = lambda : self.edit_only_inv(frame_pos, name))
        self.only_inv.place(relx = .5, rely = .8, anchor = "center")

        return self.only_inv

    def place_frame(self, rw, clm):
        self.item_frame = tk.Canvas(self.main_frame, bg = "AntiqueWhite1", height = 180, width = 180, highlightthickness = 5, highlightbackground = "black", highlightcolor = "black")
        self.item_frame.grid_propagate(False)
        self.item_frame.grid(row = rw, column = clm, padx = (60, 0), pady = (50, 0))
        
        return self.item_frame

    def place_name_label(self, frame_pos, lbl_text, rw, col):
        self.name_label = tk.Label(self.frame_list[frame_pos], font = self.text_font, text = lbl_text, bg = "AntiqueWhite1")
        self.name_label.place(relx = .5, rely = .15, anchor = "center")

        return self.name_label

    def place_label(self, frame_pos, lbl_text, rw, col, pdx, pdy):
        self.generic_label = tk.Label(self.frame_list[frame_pos], font = self.text_font, text = lbl_text, bg = "AntiqueWhite1", anchor = "w")
        self.generic_label.grid(row = rw, column = col, padx = (pdx, 0), pady = (pdy, 0))

        return self.generic_label

    def place_entry(self, frame_pos, lbl_text, rw, col, pdx, pdy):
        self.entry = tk.Entry(self.frame_list[frame_pos], font = self.text_font, width = 12)
        self.entry.grid(row = rw, column = col, pady = (pdy, 0))
        self.entry.insert(0, lbl_text)

        return self.entry

    def place_button(self, frame_pos, name):
        self.btn = tk.Button(self.frame_list[frame_pos], font = self.text_font, text = "UPDATE", bg = "ivory2", command = lambda : self.get_nums(frame_pos, name))
        self.btn.place(relx = .5, rely = .8, anchor = "center")

        return self.btn

    def get_nums(self, pos, name):
        self.inv_get = self.inventory_list[pos]
        self.price_get = self.price_list[pos]

        self.button_list[pos].config(fg = "green")
        self.main_frame.focus_set()
        
        self.change_num_file(name, int(self.price_get.get()), "priser.txt")
        self.change_num_file(name, int(self.inv_get.get()), "lager.txt")

    def edit_only_inv(self, frame_pos, name):
        self.inv_get = self.inventory_list[frame_pos]

        self.only_inv_list[frame_pos].config(fg = "green")
        self.main_frame.focus_set()

        self.change_num_file(name, int(self.inv_get.get()), "lager.txt")

    def change_num_file(self, name, change_sum, file):
        self.inventory_num_list = []
        self.change_sum = change_sum
        #Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
        with open("logs//" + file, "r") as f:#self.log_folder + self.lager_file
            for x in f:
                self.tmp_var = x.split(",")
                self.inventory_num_list.append(self.tmp_var)
        f.close()

        self.ch_remove = "'[]"
        for j, x in enumerate(self.inventory_num_list):
            if x[0] in name:
                self.remove_inv_sum = self.inventory_num_list[j][1]
                self.new_sum = self.change_sum
                self.inventory_num_list[j][1] = str(self.new_sum) + "\n"
                with open("logs//" + file, "w") as f:
                    for x in self.inventory_num_list:
                        x[1] = x[1].strip(" ")
                        self.final_inv_string = str(x)
                        for c in self.ch_remove:
                            self.final_inv_string = self.final_inv_string.replace(c, "")
                        f.write(self.final_inv_string.replace("\\n", "\n"))
