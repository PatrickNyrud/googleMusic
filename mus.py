from __future__ import unicode_literals
import youtube_dl
import pafy
import os
import ast
from tkinter import *
import tkinter
import tkFont
from gmusicapi import Musicmanager

"""
###TODO###

- meh
-- semi important
--- important

- add to loadtime, check to see if load time can be reduced
- add to google_uploader, remove all the errors that pop up.
- add new class...?, a class for the utube uploader
-- add to yt_dl, strip any '' fro the file name
-- add to google_uploader, check if the file was actually uploaded.
--- add to gui, make a gui
"""


class gui:
	def main(self):
		print("Opening")
		self.root = tkinter.Tk()
		self.root.geometry("700x350")

		self.text_font = tkFont.Font(family = "Helvetica", size = 25)

		self.text_field = Entry(self.root, bd = 2, justify = "center", font = self.text_font, relief = "groove")
		self.text_field.place(relx = .5, rely = .5, anchor = "center")

		self.button = Button(self.root, text = "ENTER", command = self.button_func())
		self.button.place(relx = .5, rely = .6, anchor = "center")

		self.root.mainloop()

	def window(self):
		pass

	def button_func(self):
		print("Works")


class googleUploader:
	def main(self):
		self.isRunning = True

		self.mm = Musicmanager()
		self.mm.login()
		while self.isRunning:
			os.system("cls")
			print("###########################"
				  "\n1. Download Songs"
				  "\n2. List of songs"
				  "\n\n3. Exit")
			self.usr_choice = input(">> ")
			if self.usr_choice == 1:
				os.system("cls")
				self.ut_url = raw_input("Enter a youtube link: ")
				self.yt_dl(self.ut_url)
			elif self.usr_choice == 2:
				self.get_songs()
			elif self.usr_choice == 3:
				self.isRunning = False

	def yt_dl(self, url):
		self.video = pafy.new(url)
		self.vid_name = "dl_songs/" + self.video.title + ".mp3"
		if not os.path.exists("dl_songs"):
			os.makedirs("dl_songs")
		self.ydl_opts = {
			'format': 'bestaudio/best',
			'outtmpl': "/dl_songs/%(title)s.%(ext)s",
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		with youtube_dl.YoutubeDL(self.ydl_opts) as self.ydl:
			self.ydl.download([url])


		self.google_upload(self.vid_name)


	def get_songs(self):
		os.system("cls")

		self.dict_list = []
		self.num = 0
		self.songs = self.mm.get_uploaded_songs()

		for x in self.songs:
			te = ast.literal_eval(str(x))
			self.dict_list.append(te)
		print("#" * 100)
		for x in self.dict_list:
			self.num += 1
			print "\n" + str(self.num) + ". " + x["title"]
		print("\n" + "#" * 100)

		print("\n3. Back")
		self.usr_choice = input(">>")
		

	#For first time run
	# def google_strt(self):
	# 	mm = Musicmanager()
	#  	mm.perform_oauth()

	def google_upload(self, name):
		self.mm.upload(name, enable_matching=False, enable_transcoding=True, transcode_quality=u'320k')
		
		print("Song uploaded!")
		input(">> ")		

if __name__ == "__main__":
	st = googleUploader()
	st.main()
	#te = gui()
	#te.main()


