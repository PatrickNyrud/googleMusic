import pygame
import math
import random
import decimal

x_screen = 1920
y_screen = 1080
screen = pygame.display.set_mode((x_screen, y_screen), pygame.FULLSCREEN)
pygame.init()

class start:
	def main(self):
		self.running = True
		self.first = True
		self.clock = pygame.time.Clock()

		self.amout_of_shell = 20
		
		self.run()


	def run(self):	
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False


			screen.fill((0, 0, 0))
			if self.first:
				self.obj_li = []
				self.first = False
				for x in range(self.amout_of_shell):
					self.obj_li.append(shell())
					self.obj_li[x].initilize()
			else:
				for x in range(self.amout_of_shell):
					self.obj_li[x].update()

			pygame.display.flip()

			self.clock.tick(60)

class shell:
	def initilize(self):
		self.y_pos = y_screen
		self.x_pos = random.randint(1, x_screen)
		self.first = True

		self.shell_list = ["shell.png", "shell_b.png", "shell_g.png", 
							"shell_p.png", "shell_r.png", "shell_y.png"]

		self.exp_height = random.randint(35, 300)

		self.shell_image = self.shell_list[random.randint(0, 5)]

		self.vel = float(decimal.Decimal(random.randrange(800, 900)) / 100)
		self.reduce_speed = float(decimal.Decimal(random.randrange(2, 4)) / 100)

		self.firework_shell = pygame.image.load(self.shell_image).convert()

	def update(self):
		if self.y_pos <= self.exp_height:
			if self.first:
				self.first = False
				self.exp = expload()
				self.exp.initilize(self.x_pos, self.y_pos, self.shell_image)
			else:
				if self.exp.update():
					self.initilize()
		else:
			self.y_pos -= self.vel
			self.vel -= self.reduce_speed
			
			screen.blit(self.firework_shell, (self.x_pos, self.y_pos))

class expload:
	def initilize(self, x_pos, y_pos, image):
		self.img = pygame.image.load(image).convert()

		self.image_list = []
		self.pos_list = []
		for x in range(8):
			self.image_list.append(self.img)
			pos = [x_pos, y_pos]
			self.pos_list.append(pos)

		self.alpha_level = 128

		self.exp_speed = 2
		self.reduce_speed = .02

	def update(self):
		for x in range(len(self.image_list)):
			self.image_list[x].set_alpha(self.alpha_level)
			screen.blit(self.image_list[x], (self.pos_list[x]))

		for j, x in enumerate(self.pos_list):
			if j == 0:
				x[0] -= self.exp_speed
			elif j == 1:
				x[0] += self.exp_speed
			elif j == 2:
				x[1] -= self.exp_speed
			elif j == 3:
				x[1] += self.exp_speed
			elif j == 4:
				x[0] -= self.exp_speed - .5
				x[1] -= self.exp_speed - .5
			elif j == 5:
				x[0] += self.exp_speed - .5
				x[1] -= self.exp_speed - .5
			elif j == 6:
				x[0] -= self.exp_speed - .5
				x[1] += self.exp_speed - .5
			elif j == 7:
				x[0] += self.exp_speed - .5
				x[1] += self.exp_speed - .5

		self.alpha_level -= 1.8

		self.exp_speed -= self.reduce_speed
		if self.alpha_level  < 0:
			return True

if __name__ == "__main__":
	st = start()
	st.main()