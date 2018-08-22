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

x_screen = 1920
y_screen = 970
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()

class start:
	def main(self):
		self.running = True
		self.first = True
		self.clock = pygame.time.Clock()

		self.amout_of_rain = 250

		self.background_img = pygame.image.load("background.png").convert()
		
		self.run()


	def run(self):	
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False


			screen.fill((0, 0, 0))
			screen.blit(self.background_img, (0, 0))
			if self.first:
				self.obj_li = []
				self.first = False
				for x in range(self.amout_of_rain):
					self.obj_li.append(rain_drop())
					self.obj_li[x].initilize()
			else:
				for x in range(self.amout_of_rain):
					self.obj_li[x].update()


			pygame.display.flip()

			self.clock.tick(60)

class rain_drop:
	def initilize(self):
		self.img = pygame.image.load("rain.png").convert()

		self.fall_speed = float(decimal.Decimal(random.randrange(300, 600)) / 100)
		self.first = True

		self.x = random.randint(0, x_screen)
		self.y = -20

	def update(self):
		if self.y < y_screen:
			screen.blit(self.img, (self.x, self.y))
			self.fall_speed += .05
			self.y += self.fall_speed
		else:
			if self.first:
				self.first = False
				self.splsh = splash()
				self.splsh.initilize(self.x)
			else:
				if self.splsh.droplet():
					self.initilize()



class splash:
	def initilize(self, x_pos):
		self.img = pygame.image.load("raindrop.png").convert()

		self.image_list = []
		self.pos_list = []
		for x in range(2):
			self.image_list.append(self.img)
			pos = [x_pos, y_screen]
			self.pos_list.append(pos)

		self.reduce_speed = 1.5
		self.mv_speed = 5

	def droplet(self):
		for x in range(len(self.image_list)):
			screen.blit(self.image_list[x], (self.pos_list[x]))

		for j, x in enumerate(self.pos_list):
			if j == 0:
				x[0] += 5
				x[1] -= self.mv_speed
			if j == 1:
				x[0] -= 5
				x[1] -= self.mv_speed
				
		self.y_cor = self.pos_list[1]
		self.mv_speed -= self.reduce_speed

		if self.y_cor[1] > y_screen + 100:
			return True

if __name__ == "__main__":
	st = start()
	st.main()
