

class investment:
	def __init__(self):
		self.buy()

	def buy(self):
		buy_dict = {"Item" : "", "Price" : "", "Amount" : ""}
		for x in buy_dict:
			print x
			inpt = raw_input(">> ")
			buy_dict[x] = inpt


		with open(buy_dict["Item"] + ".txt", "w") as f:
			f.write(buy_dict)
		f.close()

		print buy_dict

	def auction(self):
		pass

	def sold(self):
		pass


if __name__ == "__main__":
	strt = investment()