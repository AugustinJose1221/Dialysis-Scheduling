import csv
Name = input("Enter the patient name :")
Date = input("Enter the date :")
Day = input("Enter the day :")
STime = input("Enter the starting time :")
ETime = input("Enter the ending time :")

csvData = [[Name,Day,str(Date)+" "+STime,str(Date)+" "+ETime]]
with open('Testing1.csv', 'a+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData)
csvFile.close()   
