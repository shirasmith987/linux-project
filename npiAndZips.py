import gzip

f = gzip.open("npi.gz", "rt")
line = f.readline()
#line = f.readline()
g = open("npiAndZips.txt", "w")

#extracting teh nyc doctors 
while line:
    fields = line.split("|")
    #this is the 9 number zip, so cutting out the last 4 digits
    zips = fields[24][0:5]

    if zips > "10000" and zips < "10300":
        g.write(fields[0] + "|" + zips + "\n")
    line = f.readline()
f.close()
g.close()
