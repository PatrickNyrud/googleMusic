import pygame
import math
import random
import decimal

x_screen = 1920
y_screen = 1080
screen = pygame.display.set_mode((x_screen, y_screen))
pygame.init()

class start:
	def main(self):
		self.running = True
		self.first = True
		self.clock = pygame.time.Clock()

		self.amout_of_rain = 450
		
		self.run()


	def run(self):	
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False


			screen.fill((0, 0, 0))
			# if self.first:
			# 	self.obj_li = []
			# 	self.first = False
			# 	for x in range(self.amout_of_rain):
			# 		self.obj_li.append(rain_drop())
			# 		self.obj_li[x].initilize()
			# else:
			# 	for x in range(self.amout_of_rain):
			# 		self.obj_li[x].update()

			if self.first:
				self.first = False
				self.shell = shell()
				self.shell.initilize()
			else:
				self.shell.update()

			pygame.display.flip()

			self.clock.tick(60)

class shell:
	def initilize(self):
		self.y_pos = y_screen
		self.x_pos = random.randint(1, x_screen)

		self.firework_shell = pygame.image.load("shell.png").convert()

	def update(self):
		self.y_pos -= 5
		
		screen.blit(self.firework_shell, (self.x_pos, self.y_pos))

class expload:
	def initilize(self):
		pass

	def update(self):
		pass


if __name__ == "__main__":
	st = start()
	st.main()