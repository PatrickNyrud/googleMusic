import Tkinter as tk
from tkinter import ttk
import tkFont
import pirate_overview
import os

#To scale the window try width * 1.5 or some shit like that

class overview_window:
    def __init__(self, frame):
        self.frame = frame
        
        self.scrollbar_canvas = tk.Canvas(self.frame, bg = "grey21", width = 1200, height = 900)
        self.checkout_frame = tk.Frame(self.scrollbar_canvas, bg = "grey21") 

        self.text_font = tkFont.Font(family = "Helvetica", size = 20)
        self.title_font = tkFont.Font(family = "Helvetica", size = 35)
        
        self.vsb = tk.Scrollbar(self.frame, orient="vertical", command=self.scrollbar_canvas.yview)
        self.scrollbar_canvas.configure(yscrollcommand=self.vsb.set)
        
        self.checkout_frame.pack(side = "right")

        self.pirate_func = pirate_overview_funcs()

        self.vsb.pack(side="right", fill="both")

        self.scrollbar_canvas.pack(side = "right", fill = "y")
        self.scrollbar_canvas.create_window((4,4), window = self.checkout_frame, anchor="nw", tags="self.checkout_frame")

        self.checkout_frame.bind("<Configure>", self.onFrameConfigure)
        self.checkout_frame.bind("<MouseWheel>", self.OnMouseWheel)

        self.frame.bind("<Visibility>", self.draw_func)

    def onFrameConfigure(self, event):
        self.scrollbar_canvas.configure(scrollregion=self.scrollbar_canvas.bbox("all"))

    def OnMouseWheel(self,event):
        self.scrollbar_canvas.yview_scroll(-1*(event.delta/120), "units")

    def draw_func(self, event):
        self.widget_window_list = []
        self.title_label_list = []
        self.search_label_list = []
        self.found_label_list = []
        self.last_search_list = []
        self.remove_button_list = []

        self.checkout_frame.focus_set()
        
        #Amount of movies
        self.widget_amount = 3

        for x in range(self.widget_amount):
            #Place window
            self.widget_window_list.append(self.place_frame(x))
            self.widget_window_list[x].grid_propagate(False)
            #Place title label
            self.title_label_list.append(self.place_title_label(x))
            #Place search for label
            self.search_label_list.append(self.place_searchfor_label(x))
            #Place Found label
            self.found_label_list.append(self.place_found_label(x))
            #Place last search label
            self.last_search_list.append(self.place_last_search_label(x))
            #Place remove button
            self.remove_button_list.append(self.place_remove_button(x))


    def place_frame(self, frame_pos):
        self.widget_frame = tk.Frame(self.checkout_frame, bg = "blue", highlightthickness = 5, highlightbackground = "gray6", width = 800, height = 250)
        self.widget_frame.grid(row = frame_pos, column = 0, padx = (100, 0), pady = (50, 0))

        return self.widget_frame

    def place_title_label(self, frame_pos):
        self.title_label = tk.Label(self.widget_window_list[frame_pos], font = self.title_font, text = "Star Wars: The Last Jedi")
        self.title_label.grid(row = 0, column = 0, sticky = "w", padx = (10, 0), pady = (10, 0))

        return self.title_label

    def place_searchfor_label(self, frame_pos):
        self.keywords = self.pirate_func.get_keywords()

        self.search_label = tk.Label(self.widget_window_list[frame_pos], font = self.text_font, text = "Searching for: " + self.keywords)
        self.search_label.grid(row = 1, column = 0, sticky = "w", padx = (10, 0))

        return self.search_label

    def place_found_label(self, frame_pos):
        self.found_label = self.pirate_func.get_found("star_wars_the_last_jedi")

        self.found_label = tk.Label(self.widget_window_list[frame_pos], font = self.text_font, text = "Found: " + self.found_label)
        self.found_label.grid(row = 2, column = 0, sticky = "w", padx = (10, 0))

        return self.found_label

    def place_last_search_label(self, frame_pos):
        self.last_search_string = self.pirate_func.get_last_search("star_wars_the_last_jedi")

        self.last_search_label = tk.Label(self.widget_window_list[frame_pos], font = self.text_font, text = "Last search: " + self.last_search_string)
        self.last_search_label.grid(row = 3, column = 0, sticky = "w", pady = (25, 0), padx = (10, 0))

        return self.last_search_label

    def place_remove_button(self, frame_pos):
        self.remove_button = tk.Button(self.widget_window_list[frame_pos], font = self.text_font, text = "REMOVE")
        self.remove_button.grid(row = 2, column = 1, padx = (50, 0 ))

        return self.remove_button

class pirate_overview_funcs:
    def __init__(self):
        self.movie_dirr = "logs//movies//"
        self.config_keyword = "logs//config//keywords.txt"
        self.config_movie = "logs//config//movies.txt"

    def get_keywords(self):
        self.keyword_string = ""
        with open(self.config_keyword, "r") as f:
            for x in f:
                self.keyword_string += x.strip("\n") + ", "

        f.close()

        return self.keyword_string

    def get_found(self, name):
        self.found_string = ""

        self.list_found = os.listdir(self.movie_dirr + "//" + name + "//found//")
        for x in self.list_found:
            self.found_string += x.strip(".txt") + " "

        return self.found_string

    def get_last_search(self, name):
        with open(self.movie_dirr + name + "//last_search.txt", "r") as f:
            return f.readline()
            


