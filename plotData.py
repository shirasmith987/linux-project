
g = open("zipsOrder.txt", "rt")

line = g.readline()
#creating a list of all the data points to plot
h = open("plotPoints.txt", "w")

#for each line of the zips
while line:
    fields = line.split("|")
    zips = fields[2].strip()
    f = open("nycMeds.txt", "rt")
    line2 = f.readline()
    count = 0
    #go through the data of the prescriptions per capita per zipcode
    while line2:
        fields2 = line2.split("|")
        z = fields2[0].strip()
        #if the zip is in the list
        if zips == z:
            #add that point to the data points
            h.write(fields[1].strip() + "|" + fields2[1].strip() + "|" + zips + "\n")
            
            count += 1
        line2 = f.readline()
    #if the zip is not found in the prescriptions per capita list, conclude that the instances found was zero and add that to the list
    if count == 0:
           h.write(fields[1].strip() + "|0.0|" + zips + "\n")

    line = g.readline()

f.close()
g.close()
h.close()
