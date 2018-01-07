all:	nycMeds.txt smokingPresc.txt docOrder.txt npiAndZips.txt zipsOrder.txt NYCzips plotPoints.txt finalGraph.pdf

clean:
	rm nycMeds.txt smokingPresc.txt docOrder.txt npiAndZips.txt zipsOrder.txt NYCzips plotPoints.txt finalGraph.pdf

finalGraph.pdf: graph.py plotPoints.txt
	python3 graph.py

plotPoints.txt: plotData.py zipsOrder.txt nycMeds.txt
	python3 plotData.py

nycMeds.txt: nycMeds.py docOrder.txt smokingPresc.txt zipsOrder.txt
	python3 nycMeds.py

smokingPresc.txt: medPrescriptions.py 
	python3 medPrescriptions.py

docOrder.txt: docOrder.py npiAndZips.txt zipsOrder.txt
	python3 docOrder.py

npiAndZips.txt: npiAndZips.py npi.gz
	python3 npiAndZips.py

zipsOrder.txt: zipsOrdered.py NYCzips
	python3 zipsOrdered.py

NYCzips:  zipCodes.awk
	gawk -f zipCodes.awk
