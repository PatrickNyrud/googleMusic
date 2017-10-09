import os
import urllib2
import time
import re
import dropbox
import smtplib
import sys

file_dest = "e:\\proj\\"
config = "config.txt"
keywords = "keywords.txt"
upcoming = "upcomming.txt"
auth_key = "dropbox"


def main():
	isRunning = True
	while isRunning == True:
		os.system("cls")
		print((" " * 15) + "Main Menu\n"
			"----------------------------------------\n\n"
			"1. Check movies\n\n"
			"2. Exit\n"
			"\n----------------------------------------")
		usr = input(">> ")
		if usr == 1:
			idle_run()
		elif usr == 2:
			os.system("cls")
			isRunning = False
			sys.exit(0)

def idle_run():
	while 1:
		try:
			now = time.strftime("%H:%M")
			if now == "15:24":
				check_site(file_dest, config, keywords)
				time.sleep(60)
			elif now == "15:23":
				check_release(upcoming)
				time.sleep(60)
			else:
				os.system("cls")
				print now
				time.sleep(30)
		except KeyboardInterrupt:
			main()

def check_site(dirr, file_m, file_k):
	client = dropbox.client.DropboxClient(auth_key)
	#OPENS THE FILES
	movie_list = []
	keyword_list = []
	m_li = client.get_file("/python/" + file_m)
	k_li = client.get_file("/python/" + file_k)
	for x in m_li:
		movie_list.append(x.strip())
	for x in k_li:
		keyword_list.append(x.strip())
	for x in movie_list:
		x = x.replace(" ", "+")
		url_link = "http://1337x.to/search/" + x + "/1/" #.rstrip("\n") is for removing the new line so the link properly works
		print "\n" + url_link 
		film_check = urllib2.urlopen(url_link).read()
		for k in keyword_list: #Check every keywords in the list again the movie
			final_check = re.findall(k, film_check) 
			if len(final_check) > 1:
				#Checks if a msg has been sendt
				if os.path.isfile(x + "-" + k + ".txt"): 
					print("File exists\n")
				else:
					#msg hasnt been sendt, creats a file and calls send_mail
					with open(x + "-" + k + ".txt", "w") as f:
						f.write("Message has been sendt for " + x + ", (found " + k + ")")
					f.close()
					send_mail("pirate", x, k)
			else:
				print("Didnt find stuff for " + k)
	url_link = "http://www.tv2.no/" #Decoy.....
	film_check = urllib2.urlopen(url_link).close()

def check_release(file_m):
	client = dropbox.client.DropboxClient(auth_key)
	#Opens the movie list config
	upcoming_list = []
	u_li = client.get_file("/python/" + file_m)
	for x in u_li:
		upcoming_list.append(x.strip())

	now = time.strftime("%d-%m-%Y")
	for x in upcoming_list:
		x = x.split(",") #Splits the lines by ,
		if x[1].strip() == now: #Strips every whitespace
			print x[0] + " has been released!"
			send_mail("release", x[0], " ")
		else:
			print x[0] + " has NOT been released!"

def send_mail(msg_type, movie_name, movie_keyword):
	fromaddr = 'xxxx1996'
	toaddrs  = 'xxxx96'
	if msg_type == "pirate":
		msg = "Found %s rip, (%s) Go check it out!" % (movie_name, movie_keyword)
		subject = "Found %s rip, (%s)" % (movie_name, movie_keyword)
	elif msg_type == "release":
		msg = "%s has been released, go add it to the list...!" % (movie_name)
		subject = "%s released...!" % (movie_name)
	else:
		pass
	username = 'xxxx1996'
	password = 'xx'

	message = 'Subject: {}\n\n{}'.format(subject, msg)

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()


main()