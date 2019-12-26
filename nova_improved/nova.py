import Tkinter as tk
from tkinter import ttk
import tkFont
import time
import os
import json
from PIL import Image, ImageTk

#------Minor mix

#------BUGS------#

#------Addition------#
#Add customer side
#Search func
#Categories
#price pr item checkout
#static Checkout buttons
#Stats tab
#--Biggest sale osv
#--Dag 1 4523
#--Dag 2 23000 osv
#Fix fucking scroll
#Find way to reduce scroll time
#Add "(+3%) fra i fjor"

class main_frame:
    def __init__(self):
        self.x = 1600
        self.y = 800

        self.root = tk.Tk()
        self.root.geometry(str(self.x) + "x" + str(self.y))
        #self.root.attributes("-fullscreen", True)

        self.root.title("Nova")

        #self.root.iconbitmap(os.getcwd() + "\\pics\\otherpic\\nova_logo.ico")

        self.note = ttk.Notebook(self.root)

        self.tab_sale = tk.Frame(self.note)

        self.note.add(self.tab_sale, text = "Sale" + (" " * (20-4))) #lazy af

        self.note.pack()

        self.main_frame = tk.Frame(self.tab_sale, bg = "black")
        self.main_frame.pack(fill = "both", expand = True)

        self.items_start = items(self.main_frame)
        self.top_start = top(self.main_frame)
        self.checkout_start = checkout(self.main_frame)

        self.root.mainloop()

class top:
    def __init__(self, frame):
        self.frame = frame
        self.main_frame = tk.Frame(self.frame, bg = "green", width = 1000, height = 100)
        self.main_frame.grid(row = 0, column = 0, columnspan = 2)

#-----------------------------------------------------------------------------------------#
class items:
    def __init__(self, frame):
        self.frame = frame
        self.main_frame = tk.Frame(self.frame, bg = "red", width = 1000, height = 1000)
        self.main_frame.grid(row = 1, column = 1)

        self.frame_list = []

        self.main_frame.grid_propagate(False)

        self.note = ttk.Notebook(self.main_frame)

        self.tab_all = draw(self.note, "All")
        self.tab_rakett = draw(self.note, "Rakettbatteri")
        self.tab_effekt = draw(self.note, "Effektbatteri")


class draw:
    def __init__(self, note, tab_type):
        self.note = note

        self.tab = tk.Frame(self.note)

        self.note.add(self.tab, text = tab_type)

        self.note.pack()

        self.main_frame = tk.Frame(self.tab, bg ="red", width = 1000, height = 973)
        self.main_frame.grid(row = 0, column = 0)
        self.main_frame.grid_propagate(False)

        self.support_functions = support_functions()

        self.draw_frame(tab_type, self.main_frame)

    def draw_frame(self, tab_type, frame):
        self.frame = frame
        self.items = self.load_items(tab_type)

        self.name = self.items[0]
        self.price = self.items[1]
        self.inventory = self.items[2]

        self.frame_list = []
        self.name_list = []
        self.button_list = []
        self.inv_list = []

        self.columns = 4

        self.frame_position = 0

        self.name = self.items[0]
        self.price = self.items[1]
        self.inventory = self.items[2]

        for x in range(len(self.name) / self.columns):
            for j in range(4):
                self.frame_list.append(self.place_frame(self.frame_position, self.frame, x, j))
                self.name_list.append(self.place_label(self.name[self.frame_position], self.frame_position, 0, 0))
                self.button_list.append(self.place_add_button(self.name[self.frame_position], self.frame_position))
                self.inv_list.append(self.place_label("Paa lager (20)", self.frame_position, 2, 0))
                self.frame_position += 1

    def place_frame(self, frame_position, frame, row, column):
        self.frame = frame
        self.items_frame = tk.Frame(self.frame, bg = "black", width = 100, height = 100)
        self.items_frame.grid(row = row, column = column, padx = (5, 0), pady = (5, 0))
        self.items_frame.grid_propagate(False)

        return self.items_frame

    def place_label(self, name, frame_position, rw, cm):
        self.label = tk.Label(self.frame_list[frame_position], text = name)
        self.label.grid(row = rw, column = cm)

        return self.label

    def place_add_button(self, name, frame_position):
        self.button = tk.Button(self.frame_list[frame_position], text = name)
        self.button.grid(row = 1, column = 0)

        return self.button



    def load_items(self, tab_type):
        if tab_type == "All":
            self.name = self.support_functions.load("name")
            self.price = self.support_functions.load("price")
            self.inventory = self.support_functions.load("inventory")
        elif tab_type == "Rakettbatteri":
            self.name = self.support_functions.load(tab_type, True, "name")
            self.price = self.support_functions.load(tab_type, True, "price")
            self.inventory = self.support_functions.load(tab_type, True, "inventory")
        elif tab_type == "Effektbatteri":
            self.name = self.support_functions.load(tab_type, True, "name")
            self.price = self.support_functions.load(tab_type, True, "price")
            self.inventory = self.support_functions.load(tab_type, True, "inventory")

        return (self.name, self.price, self.inventory)

class support_functions:
    def load(self, search_arg, search_type = False, *args):
        self.firework_list = []
        #Opens file in json format or dict idk
        with open("inventory.json", "r") as read_file:
            data = json.load(read_file)

        for x in range(len(data["firework"])):
            if search_type:
                if data["firework"][x]["type"] == search_arg:
                    #fixes string http://www.informit.com/articles/article.aspx?p=2314818
                    self.fix_arg = values_str = ', '.join(str(x) for x in args)
                    self.firework_list.append(data["firework"][x][self.fix_arg])
            else:
                self.firework_list.append(data["firework"][x][search_arg])

        return self.firework_list

    def write(name, type_change, amount):
        with open("inventory.json", "r") as read_file:
            data = json.load(read_file)

        for x in range(len(data["firework"])):
            if data["firework"][x]["name"] == name:
                print data["firework"][x]["name"]
                tmp = data["firework"][x][type_change]
                data["firework"][x][type_change] = amount
        #tmp = data["firework"][1]["inventory"]
        #data["firework"][1]["inventory"] = "100"

        with open("inventory.json", "w") as jsonFile:
            json.dump(data, jsonFile)
#-----------------------------------------------------------------------------------------#

class checkout:
    def __init__(self, frame):
        self.frame = frame
        self.main_frame = tk.Frame(self.frame, bg = "yellow", width = 250, height = 1000)
        self.main_frame.grid(row = 1, column = 0)


if __name__ == "__main__":
    strt = main_frame()