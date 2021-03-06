# linux-project
smoking cessation drug data analysis

In this project, I attempted to show a correlation between the amount of prescriptions of smoking cessation drugs and the average income of a specific zip code. 
I hypothesized that doctors in wealthier neighborhoods were more likely to prescribe smoking cessation drugs and services to their wealthier clientele. 
(This was assuming that doctors worked in or nearby the zip code documented with their NPI AND that people went to doctors nearby the zip code they live in which would then indicate their financial status.) 
The analyzation would compare the amount of prescriptions of smoking cessation drugs prescribed by doctors in each neighborhood to try to conclude whether the number was higher for wealthier neighborhoods. 
The data sets I used to analyze this included income per zip code, doctor’s NPIs per zip code and most importantly, the Medicare Data from 2013-2015 that documents the number of prescriptions of each kind of drug supported by Medicare by each doctor indicated by their NPI.

Since I chose to analyze only the cases in New York City, the first step was to cut out the NYC zip codes from the zip code/ income data and organize them in order of incomes. 
Next, I did the same thing with the doctor’s NPI list which required first cutting out the NPIs which had NYC zip codes and then matching that list with the zip code list to organize the doctors by income, as well. The next step brought in the Medicare data. 
Here, I parsed out only the lines that mentioned any instance of a smoking cessation drug or service. 
The specific ones I included were Chantix, Zyban, Wellbutrin, and any instance of “Smoking and tobacco use intermediate counseling, greater than 3 minutes up to 10 minutes.” 
This step included going through six data sets (prescriptions and services from three different years.) 
Once I had all these data sets, I was ready for the final step. In the nycMeds.py script, I looped through each line of the smoking prescriptions in NYC list and compared it with each line of the NYC doctors and NPIs until I found a matching zip code. 
Once a zip code matched, I added that instance to a list of tuples of the zip code and the specific number of cases of that doctor’s prescriptions.
 After that completed, I created a dictionary out of this list of tuples to tally up the total number of cases per zip code. 
Then, I went through the dictionary again with the average income per zip code to calculate prescriptions per capita. 
After this step, I was ready to aggregate all the data into a list of points to plot. 
This meant creating a final list of plot points including any zip code that appeared to have zero instances of prescriptions after which I was ready to plot them on a graph.

The outcome of the project did not yield any significant correlation between the average income of a zip code and the number of prescriptions of smoking cessation drugs per capita. 
The graph indicates a completely random occurrence of prescriptions in each neighborhood. 
The instances of zero cases prescribed are found across the income axis, and the rest of the points do not seem to be linearly increasing, at all. 
However, this does not mean that there is in fact no correlation. 
Perhaps this cannot be proven within one city, or perhaps it is incorrect to assume that doctors’ NPIs reflect their demographic of patients or that the average income of a neighborhood reflects the patient population of doctors in that area. 
These are all things to consider for further analysis of this topic. 
However, I felt that this exercise was still a valid attempt at testing this hypothesis and that the results may just be proof to the fact that this hypothesis may in fact be too far-fetched. 
Nonetheless, I enjoyed doing this project and felt it was a worthy effort.

