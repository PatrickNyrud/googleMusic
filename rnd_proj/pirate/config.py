import os
import sys


class config:	
	def __init__(self):
		self.file_dest = "config\\"
		self.config = "config.txt"
		self.keywords = "keywords.txt"
		self.upcomming = "upcomming.txt"

		self.isRunning = True
		while self.isRunning:
			os.system("cls")
			print("----------WELCOME-----------\n\n"
				  "1. Edit Movies\n\n"
				  "2. Edit Keywords\n\n"
				  "3. Edit Upcomming\n\n"
				  "4. Exit\n\n"
				  "----------------------------")
			self.usr_choice = raw_input(">> ")
			if self.usr_choice == "1":
				self.edit_file(self.file_dest, self.config, "Movies")
			elif self.usr_choice == "2":
				self.edit_file(self.file_dest, self.keywords, "Keywords")
			elif self.usr_choice == "3":
				self.edit_file(self.file_dest, self.upcomming, "Releases")
			elif self.usr_choice == "4":
				os.system("cls")
				self.isRunning = False
				sys.exit(0)
			else:
				pass


	def edit_file(self, dirr, file, title):
		self.editTrue = True
		while self.editTrue:
			os.system("cls")
			print("----------" + title + "----------\n")
			self.pos = 0
			with open(dirr + file, "r") as f:
				for lines in f:
					self.pos += 1
					print str(self.pos) + ". " + lines
			print("----------" + ("-" * len(title)) + "----------" + 
				  "\nAdd(1) or Remove(2) a movie or Back(3)")
			self.ussr_choice = input(">> ")
			if self.ussr_choice == 1:
				self.usr = raw_input(">> ")
				with open(dirr + file, "a") as f:
					f.write(self.usr + "\n")
				f.close()
			elif self.ussr_choice == 2:
				self.usr = input(">> ")
				with open(dirr + file, "r") as f:
					self.movie_liste = list(f)
				f.close()
				del self.movie_liste[self.usr - 1]
				with open(dirr + file, "w") as f:
					for x in self.movie_liste:
						f.write(x)
				f.close()
			elif self.ussr_choice == 3:
				self.editTrue = False


if __name__ == "__main__":
	self.start = config()