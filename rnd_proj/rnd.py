
liste = [["Atomic", "199"], ["Commando", "499"], ["Crossfire", "599"]]



def pr(name, price):
	print name + " " + price

for x in range(len(liste)):
	pr(liste[x][0], liste[x][1])