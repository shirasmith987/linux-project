
import matplotlib.pyplot as plt
import random
import math

fig = plt.figure()

#51 plot points for 51 zips in nyc
n = 51

f = open("plotPoints.txt", "rt")
line = f.readline()

x = []
y = []

while line:
    fields = line.split("|")
    #the x axis is the income of that zipcode
    x += [fields[0]]
    #the y axis is the prescriptions per capita
    y += [fields[1]]
    line = f.readline()

f.close()

colors = [random.random() for i in range(n)]

areas = [math.pi*0.1 * 600 for i in range(n)]

plt.xticks(rotation=90)
plt.scatter(x, y, c = colors, s = areas, alpha = 1)

plt.ylabel('Prescriptions per capita')
            
plt.xlabel('NYC incomes')


fig.savefig("finalGraph.pdf")
