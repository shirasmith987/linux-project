file1 = open("./NYCzips")
g = open("zipsOrder.txt", "w")

#organizing zips- incomes low to high and assigning a number to each
lines = file1.readline()
i = 1
while lines:
    g.write(str(i).rjust(2, '0') + "|" + lines)
    i+=1
    lines = file1.readline()
    
file1.close()
g.close()
