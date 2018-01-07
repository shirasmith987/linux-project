import gzip

#open all the medicare data from 2013-2015 of all the prescriptions and services 
f = gzip.open("prescriptions2013.gz", "rt")
h = gzip.open("prescriptions2014.gz", "rt")
j = gzip.open("prescriptions2015.gz", "rt")
k = gzip.open("services2013.gz", "rt")
l = gzip.open("services2014.gz", "rt")
m = gzip.open("services2015.gz", "rt")

g = open("smokingPresc.txt", "a+")

list1 = [f, h, j]
list2 = [k, l, m]

#for the prescriptions
for i in list1:
    for line in i:
        fields = line.split("\t")
        prescrip = fields[7]
        #cut out all lines that include smoking cessation drugs
        if prescrip == "CHANTIX" or prescrip == "ZYBAN" or prescrip == "WELLBUTRIN":
                g.write(line) 
    i.close()

for i in list2:
    for line in i:
        fields = line.split("\t")
        service = fields[17]
        #cut out all the lines that have mention of counseling to stop smoking
        if service == "Smoking and tobacco use intermediate counseling, greater than 3 minutes up to 10 minutes":
            g.write(line)
    i.close()
g.close()
