num = input("Enter sum in bank: ")
rng = input("Enter years: ")
rent = input("Enter rente: ")

print "Formula = " + str(num) + " * " + str(rent) + "^" + str(rng)

for x in range(rng):
	num *= rent

print num