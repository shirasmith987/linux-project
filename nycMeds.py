

f = open("smokingPresc.txt", "rt")

g = open("nycMeds.txt", "w")

pres = f.readline()

#list of zip with # of cases
z = []
#each line of prescriptions
while pres:
    fields = pres.split("\t")
    npi1 = fields[0].strip()
    h = open("docOrder.txt", "rt")
    docs = h.readline()
    #look through each line of npis
    while docs:
        fields2 = docs.split("|")
        npi2 = fields2[1].strip()
        #if you find a matching npi in the npi list
        if npi1 == npi2:
            #if it's a line from the prescriptions data
            if len(fields) < 22:
                #add a tuple of the zip and the amount of cases for that doctor
                z.append((fields2[2].strip(), fields[10].strip()))
                #if it's a line from the services data
            else:
                z.append((fields2[2].strip(), fields[19].strip()))
        docs = h.readline()
    h.close()
    pres = f.readline()

f.close()
#dictionary to count all cases in each zip
b = {}
#each tuple in z is zip and case for that specific line
for key in z:
    if key[0] in b:
        b[key[0]] = b[key[0]] + int(key[1])
    else:
        b[key[0]] = int(key[1])

#go through organized dictionary and divide cases by population        
for key in b:
    
    p = open("zipsOrder.txt", "rt")
    line = p.readline()
    #dividing each total amount of cases by the population in that zip
    while line:
        fields = line.split("|")
        pop = fields[3].strip()
        zips = fields[2].strip()
        if key == zips:
            b[key] = (int(b[key]))/(int(pop))
        line = p.readline()
    p.close()

#now we have a dictionary of the zip with the cases of prescriptions/services per capita of that zipcode
for key in b:
    g.write(str(key) + "|" + str(b[key]) + "\n")
g.close()
