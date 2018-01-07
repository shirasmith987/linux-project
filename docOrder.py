import gzip
import sys

file2 = open("npiAndZips.txt", "rt")
docs = file2.readline()
g = open("docOrder.txt", "w")

#creating a list of doctors who's zips appear in the zips list
nums = []
while docs:
    fields = docs.split("|")
    zips = fields[1].strip()
    file1 = open("zipsOrder.txt", "rt")
    richest = file1.readline()
    while richest:
        fields2 = richest.split("|")
        a = fields2[2].strip()
        if zips == a:
            #add a tuple of the number on the zip list that indicates how wealthy the nieghtborhood is and the npi and zip
            nums.append((fields2[0], fields2[0] + "|" + fields[0] + "|" + fields[1]))
            
        richest = file1.readline()
    file1.close()
    docs = file2.readline()
file2.close()

#sort the list so it in in order of lowest income to highest
nums.sort()

#print out each key which is jus the number on the list, the npi, and the zip
for key in nums:
    g.write(key[1])
g.close()


            
