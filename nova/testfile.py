class test_class:
	def inventory(self, name, remove):
		self.inventory_num_list = []
		#Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
		with open("logs//lager.txt", "r") as f:
			for x in f:
				self.tmp_var = x.split(",")
				self.tmp_var[1] = self.tmp_var[1].strip()
				self.inventory_num_list.append(self.tmp_var)

		f.close()

		#print self.inventory_num_list

		if remove:
			#In progress
			for x in self.inventory_num_list:
				print x
		else:
			#Done Works
			for x in self.inventory_num_list:
				if x[0] == name:
					return x[1]

		# #Remove one from the list, Atomic 2 to Atomic 1
		# #X is the number, and J is the name in the list
		# for x, j in enumerate(self.inventory_num_list):
		# 	#added name == J[0] + "," because some items in the list have a , added at the end
		# 	if j[0] == name or name == j[0] + "," or name == "Super 10 (349)":
		# 		if remove:
		# 			self.new_value = int(j[1])
		# 			self.new_value -= 1
		# 			self.inventory_num_list[x][0] = j[0] + ", "
		# 			self.inventory_num_list[x][1] = str(self.new_value) + "\n"
		# 		else:
		# 			self.inventory_num_list[x][0] = j[0] + ","
		# 			self.return_inv_num = self.inventory_num_list[x][1]
		# 	else:
		# 		self.inventory_num_list[x][0] = j[0] + ","

		# 	with open("logs//lager.txt", "w+") as f:
		# 		for x in self.inventory_num_list:
		# 			for j in x:
		# 				f.write(j)
		# if not remove:
		# 	return self.return_inv_num

tt = test_class()
tt.inventory("Orion", False)