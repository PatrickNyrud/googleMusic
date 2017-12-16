import pygame
import math
import random
import decimal

######NOTES - TO DO#######
#
#Play random song from dir
#pygame multple channels?
#Fix it
#
##########################

# x_screen = 3440
# y_screen = 1440
# screen = pygame.display.set_mode((1400, 400))
# pygame.init()

# class start:
# 	def __init__(self):
# 		self.running = True
# 		self.clock = pygame.time.Clock()
		
# 		self.run()


# 	def run(self):	
# 		while self.running:
# 			for event in pygame.event.get():
# 				if event.type == pygame.QUIT:
# 					self.running = False


# 			screen.fill((0, 0, 0))
# 			#screen.blit(self.background_img, (0, 0))
			
# 			pygame.display.flip()

# 			self.clock.tick(60)

class Fish:
	def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
		self.first_name = first_name
		self.last_name = last_name
		self.skeleton = skeleton
		self.eyelids = eyelids

	def swim(self):
		print("The fish is swimming.")

	def swim_backwards(self):
		print("The fish can swim backwards.")

class Torsk(Fish):
	pass

class Shill(Fish, object):
	def __init__(self, first_name, one):
		self.one = one
		super(Shill, self).__init__(first_name)

	def food(self):
		#print self.first_name
		print self.first_name
		print self.one


peder = Torsk("Peder")
pat = Shill("Pet", "one")

print peder.skeleton
pat.food()