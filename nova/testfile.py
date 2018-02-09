class test_class:
	def inventory(self, name, remove):
		self.inventory_num_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//lager.txt", "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.inventory_num_list.append(self.tmp_var)
		f.close()

		if remove:
			self.ch_remove = "'[]"
			for j, x in enumerate(self.inventory_num_list):
				if x[0] in name:
					self.remove_inv_sum = self.inventory_num_list[j][1]
					self.new_sum = int(self.remove_inv_sum) - 1
					self.inventory_num_list[j][1] = str(self.new_sum) + "\n"
					with open("logs//lager.txt", "w") as f:
						for x in self.inventory_num_list:
							x[1] = x[1].strip(" ")
							self.final_string = str(x)
							for c in self.ch_remove:
								self.final_string = self.final_string.replace(c, "")
							f.write(self.final_string.replace("\\n", "\n"))
		else:
			for x in self.inventory_num_list:
				if x[0] == name:
					return x[1]

tt = test_class()
tt.inventory("Orion", True)