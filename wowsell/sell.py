import json

#I acution list opp alle filer sa man ser hvilke som er aktive
#Om man har to for soul dust, 1 "soul dust" og 2 "soul dust2"
#{'Item' : '', 'Price' : '', 'Amount' : '', "Auction_length" : "", "Lost_deposit" : ""}
class investment:
	def __init__(self):
		#self.buy()
		self.auction()

	def buy(self):
		buy_dict = {
						"Bought" : {
							"Item" : "",
							"Price" : "",
							"Amount" : "",
						},
						"Auction" : {
							"Item" : " ",
							"Price" : " ",
							"Amount" : " ",
							"Length" : " ",
							"Lost_deposit" : " ",
						}
					}

		for x in buy_dict["Bought"]:
			print x
			inpt = raw_input(">> ")
			buy_dict["Bought"][x] = inpt

		with open(buy_dict["Bought"]["Item"] + ".json", "w") as f:
			json.dump(buy_dict, f)
		f.close()

	def auction(self):
		auction = raw_input("What would you like to sell?\n>> ")
	
		with open('Dust.json', 'r') as f: 
			auction_data = json.load(f)
		
		


	def sold(self):
		pass


if __name__ == "__main__":
	strt = investment()