import pygame
import math
import random
import decimal

class start:
	def main(self):
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		self.RED = (255, 0, 0)

		self.WIDTH = 20
		self.HEIGHT = 20

		self.MARGIN = 5

		self.amout_of_boxes = 20
		
		# Create a 2 dimensional array. A two dimensional
		# array is simply a list of lists.
		self.grid = []
		for row in range(self.amout_of_boxes):
		    # Add an empty array that will hold each cell
		    # in this row
			self.grid.append([])
			for column in range(self.amout_of_boxes):
				self.grid[row].append(0)  # Append a cell

		# Set row 1, cell 5 to one. (Remember rows and
		# column numbers start at zero.)
		self.grid[random.randint(1, self.amout_of_boxes)][random.randint(1, self.amout_of_boxes)] = 1
		self.grid[random.randint(1, self.amout_of_boxes)][random.randint(1, self.amout_of_boxes)] = 2
		
		self.green_score = 0
		self.red_score = 0

		pygame.init()
		
		self.screen = pygame.display.set_mode((900, 505))
		
		pygame.display.set_caption("Array Backed Grid")
		
		self.done = False
		
		self.clock = pygame.time.Clock()

		self.run()


	def run(self):	
		while not self.done:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:  
					self.done = True 
			self.screen.fill(self.BLACK)
		
			for row in range(self.amout_of_boxes):
				for column in range(self.amout_of_boxes):
					self.color = self.WHITE
					if self.grid[row][column] == 1:
						self.color = self.GREEN
						self.update(row, column, 1)
					elif self.grid[row][column] == 2:
						self.color = self.RED
						self.update(row, column, 2)
					self.x = (self.MARGIN + self.WIDTH) * column + self.MARGIN
					self.y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN
					pygame.draw.rect(self.screen, self.color, 
								[self.x, self.y, self.WIDTH, self.HEIGHT])

			pygame.display.flip()

			self.clock.tick(60)


	def update(self, row, column, num):
		self.infect_zone = [[row - 1, column], [row + 1, column],
							[row, column +1], [row, column - 1]]
		
		self.infect_chance = random.randint(1, 100)
		if self.infect_chance >= 99:
			self.direction = self.infect_zone[random.randint(0, 3)]
			if self.direction[0] < 0 or self.direction[0] > self.amout_of_boxes - 1:
				pass
			elif self.direction[1] < 0 or self.direction[1] > self.amout_of_boxes - 1:
				pass
			elif self.grid[self.direction[0]][self.direction[1]] != 0 and self.grid[self.direction[0]][self.direction[1]] != num:
				self.grid[self.direction[0]][self.direction[1]] = num

			elif self.grid[self.direction[0]][self.direction[1]] == 0:
				self.grid[self.direction[0]][self.direction[1]] = num

				print "Cell " + str(self.direction) + " has been conquered"

	def score_display(self):
		for row in range(self.amout_of_boxes):
			for column in range(self.amout_of_boxes):
				if self.grid[row][column] == 1:
					self.green_score += 1
				elif self.grid[row][column] == 2:
					self.red_score += 1
				else:
					pass
		self.myfont = pygame.font.SysFont("monospace", 15)
		self.green_text = self.myfont.render("Number of GREEN tiles: " + str(self.green_score), 1, self.GREEN)
		self.red_text = self.myfont.render("Number of RED tiles: " + str(self.red_score), 1, self.RED)
		self.screen.blit(self.green_text, (self.x + 50, 100))
		self.screen.blit(self.red_text, (self.x + 50, 120))

if __name__ == "__main__":
	st = start()
	st.main()