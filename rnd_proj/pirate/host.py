import os
import urllib2
import time
import re
import smtplib
import sys

file_dest = "config\\"
config = "config.txt"
keywords = "keywords.txt"
upcoming = "upcomming.txt"

class main:
	def __init__(self):
		isRunning = True
		while isRunning == True:
			now = time.strftime("%H:%M")
			date = time.strftime("%d %b %Y")
			if now == "18:00" or now == "20:00" or now == "22:00":
				self.check_site(file_dest, config, keywords, now, date)
				time.sleep(60)
			elif now == "20:30":
				self.check_release(file_dest, upcoming)
				time.sleep(60)
			else:
				os.system("cls")
				print now
				time.sleep(30)

	def check_site(self, dirr, file_m, file_k, time, day):
		#OPENS THE FILES
		movie_list = []
		keyword_list = []
		log_write = open("logs\\search_log.txt", "a")
		with open(dirr + file_m, "r") as movie_file, open(dirr + file_k, "r") as key_file:
			for x in movie_file:
				movie_list.append(x.strip())
			for x in key_file:
				keyword_list.append(x.strip())
			movie_file.close()
			key_file.close()
		for x in movie_list:
			x = x.replace(" ", "+")
			url_link = "http://1337x.to/search/" + x + "/1/" #.rstrip("\n") is for removing the new line so the link properly works
			log_write.write("\n\n" + time + " " + day + "\n" + url_link)
			film_req = urllib2.Request(url_link, headers={'User-Agent' : "Magic Browser"}) 
			film_read = urllib2.urlopen(film_req).read()
			for k in keyword_list: #Check every keywords in the list again the movie
				final_check = re.findall(k, film_read) 
				if len(final_check) > 1:
					#Checks if a msg has been sendt
					if os.path.isfile("logs\\" + x + "-" + k + ".txt"): 
						log_write.write("\nFile exists")
					else:
						#msg hasnt been sendt, creats a file and calls send_mail
						with open("logs\\" + x + "-" + k + ".txt", "w") as f:
							f.write("Message has been sendt for " + x + ", (found " + k + ")")
						f.close()
						self.send_mail("pirate", x, k)
				else:
					log_write.write("\nDidnt find stuff for " + k)
		url_link = "http://www.tv2.no/" #Decoy.....
		film_check = urllib2.urlopen(url_link).close()

	def check_release(self, dirr, file_m):
		upcoming_list = []
		log_write = open("logs\\search_log.txt", "a")
		with open(dirr + file_m, "r") as movie_file:
			for x in movie_file:
				upcoming_list.append(x.strip())

		now = time.strftime("%d-%m-%Y")
		for x in upcoming_list:
			x = x.split(",") #Splits the lines by ,
			if x[1].strip() == now: #Strips every whitespace
				log_write.write("\n\n" + x[0] + " has been released!")
				self.send_mail("\n\n" + "release", x[0], " ")
			else:
				log_write.write("\n\n" + x[0] + " has NOT been released!")

	def send_mail(self, msg_type, movie_name, movie_keyword):
		fromaddr = 'xx'
		toaddrs  = 'xx'
		if msg_type == "pirate":
			msg = "Found %s rip, (%s) Go check it out!" % (movie_name, movie_keyword)
			subject = "Found %s rip, (%s)" % (movie_name, movie_keyword)
		elif msg_type == "release":
			msg = "%s has been released, go add it to the list...!" % (movie_name)
			subject = "%s released...!" % (movie_name)
		else:
			pass
		username = 'xx'
		password = 'xx'

		message = 'Subject: {}\n\n{}'.format(subject, msg)

		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(username, password)
		server.sendmail(fromaddr, toaddrs, message)
		server.quit()


if __name__ == "__main__":
	start = main()