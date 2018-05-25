# -*- coding: utf-8 -*-

import Tkinter as tk
from tkinter import ttk
import tkFont
import os
import urllib2
from bs4 import BeautifulSoup

class idle_search:
    def __init__(self, name):
        self.movie_dirr = "logs//movies//"
        self.config_keyword = "logs//config//keywords.txt"

        self.search(name)

    def get_keywords(self):
        self.keyword_string = ""
        with open(self.config_keyword, "r") as f:
            for x in f:
                self.keyword_string += x.strip("\n") + ", "

        f.close()

        self.keyword_list = self.keyword_string.split(",")
        del self.keyword_list[-1]

        return self.keyword_list

    def search(self, name):
        self.keywords = self.get_keywords()
        self.search_url = "http://1337x.to/search/" + name.replace("_", "+") + "/1/"
        
        self.film_req = urllib2.Request("https://www.tv2.no", headers={'User-Agent' : "Magic Browser"})
        self.film_read = urllib2.urlopen(self.film_req).read()

        self.parse = BeautifulSoup(self.film_read, "html.parser") 

        self.get_div = self.parse.find("div", attrs={"class" : "promo-d-cont"})
        print self.get_div.text.strip().encode(encoding = "UTF-8")


if __name__ == "__main__":
    te = idle_search("star_wars_the_last_jedi")
