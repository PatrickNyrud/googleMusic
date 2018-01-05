def lager(name, remove):
    inv_list = []
    #Appends [["Atomic", 2], ["Superti", 2]] and so on to the list
    with open("logs//lager.txt", "r") as f:
        for x in f:
            tmp_var = x.split(",")
            inv_list.append(tmp_var)
    f.close()

    #Remove one from the list, Atomic 2 to Atomic 1
    #X is the number, and J is the name in the list
    for x, j in enumerate(inv_list):
        #print "j is " + j[0] + " and name is " + name
        if j[0] == name:
            if remove:
                new_value = int(j[1])
                new_value -= 1
                inv_list[x][0] = j[0] + ", "
                inv_list[x][1] = str(new_value) + "\n"
            else:
                #print inv_list[x]
                inv_list[x][0] = j[0] + ","
                return_inv_num = inv_list[x][1]
        else:
            inv_list[x][0] = j[0] + ","

        with open("logs//lager.txt", "w+") as f:
            for x in inv_list:
                for j in x:
                    f.write(j)
    if not remove:
        return return_inv_num

inv_list = [["Atomic", "199"], ["Super 10", "349"], ["Magnum", "449"], ["Bolero", "1199"], ["Circus", "1199"], ["Bizarre", "1199"]
        , ["Goldfish", "1199"], ["Orion", "1199"], ["Trapez", "1199"], ["Passion", "1199"], ["Tnt", "1199"], ["Thunderbird", "1199"]
        , ["Commando", "1199"], ["Shocker", "1199"], ["Kamikaze", "1199"]]

for x in inv_list:
    var = x[0]
    print lager(var, False)