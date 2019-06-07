import csv
import googlemaps
import numpy as np
gmaps = googlemaps.Client(key='XXXXXXXXXXXXXXXXXXXX')        #API Key
data = "example.csv"                                        #Dataset
h_list={}
x=0
with open(data, 'r') as file:
    reader = csv.reader(file)
    hospital_list = list(reader)
for a in hospital_list:
    if a[1][0]=='N':
        #print("\n")
        continue
    for i in range(0,15):
        if a[1][i]==',':
            break
    h_list[x,0]=a[3]
    h_list[x,1]=a[2]
    h_list[x,2]=a[1][0:i]
    h_list[x,3]=a[1][i+1:21]
    h_list[x,5]=a[0]
    x+=1
LatP = input("Your Latitude :")
LongP = input("Your Longitude :")
for i in range(0,x):
    t = float(h_list[i,2])-float(LatP)
    p = float(h_list[i,3])-float(LongP)
    if t<0.1 and t>-0.1:
        if p<0.1 and p>-0.1:
            LatD = h_list[i,2]
            LongD = h_list[i,3]
            distance = gmaps.distance_matrix([str(LatP) + " " + str(LongP)], [str(LatD) + " " + str(LongD)], mode='driving')['rows'][0]['elements'][0]
            h_list[i,4]=distance["distance"]["text"]
            print("Name :",h_list[i,0],"\nAddress :",h_list[i,1],"\nDistance :",h_list[i,4],"\n")


