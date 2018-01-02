class lager:
	def __init__(self, remove):
		self.inv_list = []
		with open("logs//lager.txt", "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inv_list.append(self.tmp_var)
		f.close()

		for x, j in enumerate(self.inv_list):
			if j[0] == remove:
				self.new_value = int(j[1])
				self.new_value -= 1
				self.inv_list[x][0] = j[0] + ", "
				self.inv_list[x][1] = str(self.new_value) + "\n"
			else:
				self.inv_list[x][0] = j[0] + ","

			with open("logs//lager.txt", "w+") as f:
				for x in self.inv_list:
					for j in x:
						f.write(j)

if __name__ == "__main__":
	strt = lager("Atomic")