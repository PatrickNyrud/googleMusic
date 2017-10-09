import os
import sys
import dropbox
from termcolor import colored
from colorama import init

file_dest = "e:\\proj\\"
config = "config.txt"
keywords = "keywords.txt"
upcomming = "upcomming.txt"
auth_key = "dropbox"

init()





def main():
	isRunning = True
	while isRunning:
		os.system("cls")
		print("----------WELCOME-----------\n\n"
			  "1. Edit Movies\n\n"
			  "2. Edit Keywords\n\n"
			  "3. Edit Upcomming\n\n"
			  "4. Exit\n\n"
			  "----------------------------")
		usr_choice = raw_input(">> ")
		if usr_choice == "1":
			edit_file(file_dest, config, "Movies")
		elif usr_choice == "2":
			edit_file(file_dest, keywords, "Keywords")
		elif usr_choice == "3":
			edit_file(file_dest, upcomming, "Releases")
		elif usr_choice == "4":
			os.system("cls")
			isRunning = False
			sys.exit(0)
		else:
			pass

def edit_file(dirr, file, title):
	isRunning = True
	while isRunning:
		os.system("cls")
		print("----------" + title + "----------\n")
		pos = 0
		with open(dirr + file, "r") as f:
			for lines in f:
				pos += 1
				print str(pos) + ". " + lines
		if update(dirr, file):
			print("----------" + ("-" * len(title)) + "----------" + colored(" Up to date", "green") + 
				  "\nAdd(1) or Remove(2) a movie or Upload(3) or Back(4)")
		else:
			print("----------" + ("-" * len(title)) + "----------" + colored(" Not up to date", "red") + 
				  "\nAdd(1) or Remove(2) a movie or Upload(3) or Back(4)")
		usr_choice = input(">> ")
		if usr_choice == 1:
			usr = raw_input(">> ")
			with open(dirr + file, "a") as f:
				f.write(usr + "\n")
			f.close()
		elif usr_choice == 2:
			usr = input(">> ")
			with open(dirr + file, "r") as f:
				movie_liste = list(f)
			f.close()
			del movie_liste[usr - 1]
			with open(dirr + file, "w") as f:
				for x in movie_liste:
					f.write(x)
			f.close()
		elif usr_choice == 3:
			client = dropbox.client.DropboxClient(auth_key)
			with open(dirr + file, "rb") as f:
				client.put_file("/python/" + file, f, overwrite = True)
		elif usr_choice == 4:
			isRunning = False
			main()

def update(dirr, file):
	client = dropbox.client.DropboxClient(auth_key)
	l = []
	f = client.get_file("/python/" + file)
	for x in f:
		l.append(x.strip())

	k = []
	with open(dirr + file, "r") as f:
		for x in f:
			k.append(x.strip())

	if l == k:
		return True
	else:
		return False


main()