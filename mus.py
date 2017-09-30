from __future__ import unicode_literals
import youtube_dl
import pafy
import os
from gmusicapi import Musicmanager

class gui:
	def main(self):
		pass

	def window(self):
		pass


class googleUploader:
	def main(self):
		self.ut_url = raw_input("Enter a youtube link: ")
		self.yt_dl(self.ut_url)

	def yt_dl(self, url):
		self.video = pafy.new(url)
		self.vid_name = self.video.title + ".mp3"

		self.ydl_opts = {
			'format': 'bestaudio/best',
			'outtmpl': "%(title)s.%(ext)s",
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
			}],
		}
		with youtube_dl.YoutubeDL(self.ydl_opts) as self.ydl:
			self.ydl.download([url])


		self.google_mngr(self.vid_name)

	# def google_strt():
	# 	mm = Musicmanager()
	# 	mm.perform_oauth()

	def google_mngr(self, name):
		self.mm = Musicmanager()
		self.mm.login()

		self.mm.upload(name, enable_matching=False, enable_transcoding=True, transcode_quality=u'320k')
		

if __name__ == "__main__":
	st = googleUploader()
	st.main()