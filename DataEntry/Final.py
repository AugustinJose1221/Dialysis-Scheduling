import csv
import pandas as pd
import googlemaps
import numpy as np
gmaps = googlemaps.Client(key='AIzaSyDD3BrAMj8NXDunRffUiVkTy9WBfpimLq0') #AIzaSyB_NLGiCWcVh-jhQCqMIXFfPrmTdbfFV74 #AIzaSyDD3BrAMj8NXDunRffUiVkTy9WBfpimLq0
data = "Hospital_Dataset1.csv"
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
    h_list[x,3]=a[1][i+2:21]
    h_list[x,5]=a[0]
    h_list[x,6]=a[10]   #Bed number
    x+=1
mindist = 25
mindist1 = 0
index=[]
test1=[]
posx=0
posy=0
LatP =input("Enter the latitude :") #latitude
LongP =input("Enter the longitude :") #longitude
for i in range(0,x):
    t = float(h_list[i,2])-float(LatP)
    p = float(h_list[i,3])-float(LongP)
    if t<0.1 and t>-0.1:
        if p<0.1 and p>-0.1:
            LatD = h_list[i,2]
            LongD = h_list[i,3]
            distance = gmaps.distance_matrix([str(LatP) + " " + str(LongP)], [str(LatD) + " " + str(LongD)], mode='driving')['rows'][0]['elements'][0]
            h_list[i,4]=distance["distance"]["text"]
            h_list[i,7]=distance["distance"]["value"]/1000
            index.append(i)
            if (distance["distance"]["value"]/1000)<mindist:
                mindist = distance["distance"]["value"]/1000
                posx=i

if len(index)==0:
    print("No hospitals available ")
elif len(index)==1:
    print("The nearest hospital details")
    print("Name :",h_list[posx,0],"\nAddress :",h_list[posx,1],"\nDistance :",h_list[posx,4],"\nPatient Capacity",h_list[posx,6])
elif len(index)>=2:
    for b in index:
        test1.append(h_list[b,7])
    test1.sort()
    for b in index:
        if test1[1]==h_list[b,7]:
            posy=b
            break
    print("The nearest hospital details")
    print("ID :",h_list[posx,5],"\nName :",h_list[posx,0],"\nAddress :",h_list[posx,1],"\nDistance :",h_list[posx,4],"\nPatient Capacity :",h_list[posx,6])
    print("******************************************************************")
    print("ID :",h_list[posy,5],"\nName :",h_list[posy,0],"\nAddress :",h_list[posy,1],"\nDistance :",h_list[posy,4],"\nPatient Capacity :",h_list[posy,6])
PID=0
print("Enter 1 for the first hospital, 2 for second hospital")
choice = input("Enter your choice of hospital :")
ID = input("Enter the patient ID :")
PDay = input("Enter 0-6 for the choice of day of the week :")
PTime = input("Enter 0 for 5AM-9AM session\n1 for 9:30AM-1:30PM session\n2 for 2PM-6PM session\n3 for 6:30PM-10:30PM session\nEnter your choice :")
Tex = (int(PDay)*4)+int(PTime)+1
data = csv.reader(open('Hospital_Dataset2.csv'),delimiter=',')
if choice==1:
    PID=posx
elif choice==2:
    PID=posy
jx=0 
for i in data:
    if jx==0:
        jx=1
        continue
    if int(i[0])==int(h_list[PID,5]):
        if i[Tex]!=0:
            print("Bed available and booked")
            csvData=[[str(i[0]),str(ID),str(int(PDay)+1),str(PTime)]]
            with open('Requests.csv', 'a+', newline='') as csvFile:
                csv.writer(csvFile).writerows(csvData)
            csvFile.close()
            df = pd.read_csv("Hospital_Dataset2.csv")
            df.loc[df["ID"]==int(i[0]), str(Tex)]= int(i[Tex])-1
            df.to_csv("Hospital_Dataset2.csv", index=False)
            break
        else:
            print("All beds in that time slot is already booked")
    

            


