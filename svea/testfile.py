import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import nova_top
import nova_checkout
import nova_item
import nova_config
import nova_salg_log
from PIL import Image, ImageTk

#--------------------------FUCKING IMPORTANT--------------------------#
#The green area needs to be as close to the scrollbar for it to scroll
#--------------------------FUCKING IMPORTANT--------------------------#

#------Minor mix

#------BUGS------#
#See if can fix click minus button too fast checkout bugs out

#------Addition------#
#Add customer side

#------Redo------#
#Redo all the images, make em look better

class main_frame:
    def __init__(self):
        self.x = 1600
        self.y = 800

        self.root = tk.Tk()
        self.root.geometry(str(self.x) + "x" + str(self.y))
        #self.root.attributes("-fullscreen", True)

        self.root.title("Nova")

        self.root.iconbitmap(os.getcwd() + "\\pics\\otherpic\\nova_logo.ico")

        self.note = ttk.Notebook(self.root)

        self.tab_sale = tk.Frame(self.note)
        self.tab_salg_log = tk.Frame(self.note)
        self.tab_config = tk.Frame(self.note)

        self.note.add(self.tab_sale, text = "Sale" + (" " * (20-4))) #lazy af
        self.note.add(self.tab_salg_log, text = "Salg log" + (" " * (20-8)))
        self.note.add(self.tab_config, text = "Config" + (" " * (20-6))) #lazy af

        self.note.pack()

        self.main_frame = tk.Frame(self.tab_sale, bg = "black")
        self.main_frame.pack(fill = "both", expand = True)

        self.tab_salg_start = nova_salg_log.salg_log(self.tab_salg_log)
        self.tab_config_start = nova_config.config(self.tab_config)

        self.top_class = nova_top.top_frame()
        self.checkout_class = nova_checkout.checkout_frame()
        self.items_class = nova_item.items_frame()

        self.top_class.initialize(self.main_frame, self.root)
        self.checkout_class.initialize(self.main_frame, self.items_class, self.top_class)
        self.items_class.initialize(self.main_frame, self.checkout_class)

        self.top_class.update_time()
        self.root.mainloop()

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
        self.items_object = nova_item.items_frame()
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
        
        self.button_list[0].destroy()
        self.button_list[1].destroy()
        self.only_inv_list.append(self.place_only_inv(0, "Atomic"))

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
        self.top_object.excel_log(remove_items)

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


class excel_log_pole:
    def __init__(self, items):
        self.dest = "logs//excel_logs//excel_pole.xlsx"
        self.work_book = openpyxl.load_workbook(self.dest)
        self.work_sheet = self.work_book.active

        self.obj = nova_item.items_frame()
        
        self.column_len = self.obj.pic_price_file("logs//", "lager.txt")
        
        for x in items: 
            self.write_workbook(x)
        
        self.save_excel()
    
    def get_columns(self, item):
        for x in range(1, len(self.column_len) + 1):
            #Gets the value of cell x
            self.column_value = self.work_sheet.cell(row = 1, column = x).value 
            #Checks name at cell x if its == to item
            if self.column_value == item:
                #Returns cell position
                return x
                #return self.work_sheet.cell(row = 1, column = x).column returns actuall name like AH
            else:
                pass

    def write_workbook(self, item):
        self.get_column = self.get_columns(item)
        self.column = self.work_sheet.cell(row = 2, column = self.get_column)
        self.column.value = self.column.value + 1

    #Save excel file
    def save_excel(self):  
        self.work_book.save(self.dest)


class excel_log_linear:
    def __init__(self, items):
        #18 rows
        #Sale at 1134, Super 10 x1
        self.dest = "logs//excel_logs//excel_linear.xlsx"
        self.work_book = openpyxl.load_workbook(self.dest)
        self.work_sheet = self.work_book.active

        self.obj = nova_item.items_frame()
        
        self.column_len = self.obj.pic_price_file("logs//", "lager.txt")

        for x in items:
            self.write_workbook(x)

        self.save_excel()

    def write_workbook(self, item):
        self.row = self.get_rows()
        self.column = self.get_columns(item)

        try:
            self.write = self.work_sheet.cell(row = self.row, column = self.column)
            self.write.value = self.write.value + 1
        except:
            pass

    def get_rows(self): 
        self.now = time.strftime("%H")
        for x in range(1, 18):
            self.row_value = self.work_sheet.cell(row = x, column = 1).value
            if self.now == self.row_value[0:2]:
                return x
            else:
                pass
                
    def get_columns(self, item):
        for x in range(1, len(self.column_len) + 1):
            #Gets the value of cell x
            self.column_value = self.work_sheet.cell(row = 1, column = x).value 
            #Checks name at cell x if its == to item
            if self.column_value == item:
                #Returns cell position
                return x
            else:
                pass
    
    def save_excel(self):  
        self.work_book.save(self.dest)


class salg_log:
    def __init__(self, frame):
        self.frame = frame
        self.scrollbar_canvas = tk.Canvas(self.frame, bg = "grey21", width = 1700)
        self.main_frame = tk.Frame(self.frame, width = 1500, bg = "grey21", height = self.file_len() * 40)

        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
        self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)

        self.text_font = tkFont.Font(family = "Helvetica", size = 20)

        self.main_frame.pack(fill = "both", expand = True)
    
        self.main_frame.pack_propagate(False)


        self.vsb.pack(side="right", fill="both")

        self.scrollbar_canvas.pack(side = "right", fill = "y", expand = True)
        self.scrollbar_canvas.create_window((4,4), window = self.main_frame, anchor="nw", tags="self.main_frame")

        self.main_frame.bind("<Configure>", self.onFrameConfigure)
        self.main_frame.bind("<MouseWheel>", self.OnMouseWheel)

        self.frame.bind("<Visibility>", self.draw_init)


    def onFrameConfigure(self, event):
        self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

    def OnMouseWheel(self,event):
        self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

    def draw_init(self, event):
        self.log_label_list = []

        self.main_frame.focus_set()

        for widget in self.main_frame.winfo_children():
                widget.destroy()

        self.display_log()

    def display_log(self):
        for j, line in enumerate(reversed(open("logs//salgs_log.txt").readlines())):
            self.log_label = tk.Label(self.main_frame, text = line.strip(), font = self.text_font, bg = "grey21", fg = "cornsilk2")
            self.log_label.pack(fill = "both", expand = 1)

            self.log_label_list.append(self.log_label)


    def file_len(self):
        with open("logs//salgs_log.txt", "r") as f:
            for j, x in enumerate(f):
                pass
        f.close()
        
        return j + 1



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
            f.write("\n\n" + str(items).translate(None, "[]'") + " | " + str(final_price) + " kr\n" + str(time.strftime("%d %b %Y %H:%M")))
        f.close()

    def excel_log(self, items):
        self.excel_pole = nova_excel_log.excel_log_pole(items)
        self.excel_linear = nova_excel_log.excel_log_linear(items)

    def display_total_sold(self):#self.log_folder + self.total_salg_sum
        if not os.path.isfile(self.log_folder + self.total_salg_sum_dag):
            with open(self.log_folder + self.total_salg_sum_dag, "w") as f:
                f.write("0")
            f.close()
        
        with open(self.log_folder + self.total_salg_sum_dag, "r+") as salg_dag, open(self.log_folder + self.total_salg_sum, "r") as salg_total:
            self.total_salg_label.config(text = "Total solgt: " + salg_total.read() + " Kr")
            self.total_salg_dag_label.config(text = "Total solgt idag: " + salg_dag.read() + " Kr")
        salg_dag.close()
        salg_total.close()

