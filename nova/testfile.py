liste = ["Ato", "Super", "Ato", "Magnum"]
check = []

final = []

for x in liste:
	if x in check:
		pass
	else:
		check.append(x)
		tt = 0
		for j in liste:
			if x == j:
				tt += 1
		final.append(x + " x" + str(tt))
		
print final