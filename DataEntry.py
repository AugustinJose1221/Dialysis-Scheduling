import csv
csvData=[['Name','Day','Starting Time','Ending Time']]
with open('Testing1.csv', 'w+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData)
csvFile.close()
