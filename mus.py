from __future__ import unicode_literals
import youtube_dl
from gmusicapi import Musicmanager

def yt_dl():
	ydl_opts = {
	    'format': 'bestaudio/best',
	    'outtmpl': "%(title)s.%(ext)s",
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(['https://www.youtube.com/watch?v=JAr2rUbgPzE'])

def google_manger():
	mm = Musicmanager()
	mm.perform_oauth()

if __name__ == "__main__":
	#main()
	google_manger() 