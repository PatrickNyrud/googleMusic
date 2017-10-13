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
--- add to yt_dl, strip any '' fro the file name
"""


class gui:
	def main(self):
		self.root = tkinter.Tk()
		self.root.configure(background = "white")
		self.root.geometry("700x350")

		self.text_font = tkFont.Font(family = "Helvetica", size = 20)

		self.text_field = Entry(self.root, bd = 2, justify = "center", font = self.text_font, relief = "groove")
		self.text_field.place(relx = .5, rely = .4, width = 600, anchor = "center")

		self.upload_status = Label(self.root, borderwidth = 0, bg = "white", width = 50, height = 1, justify = "center")
		self.upload_status.place(relx = .5, rely = .2, anchor = "center")

		self.button = Button(self.root, bg = "white", text = "ENTER", command = self.button_func)
		self.button.place(relx = .5, rely = .6, anchor = "center")

		self.root.mainloop()

	def initilize(self):
		self.up = googleUploader()
		self.up.login()

	def button_func(self):
		self.url = self.text_field.get()
		self.first_run = self.up.check_songs()
		self.up.yt_dl(self.url)
		self.second_run = self.up.check_songs()
		if self.second_run > self.first_run:
			self.upload_status.insert(END, "Song was uploaded!")
			self.upload_status.configure(fg = "green")
		else:
			self.upload_status.insert(END, "Song was NOT uploaded!")
			self.upload_status.configure(fg = "red")


class googleUploader:
	def login(self):
		self.mm = Musicmanager()
		self.mm.login()

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


	def check_songs(self):
		self.songs = self.mm.get_uploaded_songs()
		self.num = 0

		for x in self.songs:
			self.num += 1

		return self.num

	def google_upload(self, name):
		self.mm.upload(name, enable_matching=False, enable_transcoding=True, transcode_quality=u'320k')

	#For first time run
	# def google_strt(self):
	# 	mm = Musicmanager()
	#  	mm.perform_oauth()


if __name__ == "__main__":
	strt = gui()
	strt.initilize()
	strt.main()
	#te = googleUploader()
	#te.check_songs()


