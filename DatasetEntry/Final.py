import csv
x = 0
slot = [['5:00','9:00',0],['9:30','13:30',0],['14:00','18:00',0],['18:30','22:30'],0]
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
once = []
twice = []
thrice = []
count = 0
y = 0
csvData=[['Patient Number','Day','Starting Time','Ending Time','Bed Number','Type']]
csvData1=[['Patient Number','Starting Time','Ending Time','Bed Number']]
with open('Schedule.csv', 'w+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData)
with open('Sunday.csv', 'w+', newline='') as Sunday:
    csv.writer(Sunday).writerows(csvData1)
with open('Monday.csv', 'w+', newline='') as Monday:
    csv.writer(Monday).writerows(csvData1)
with open('Tuesday.csv', 'w+', newline='') as Tuesday:
    csv.writer(Tuesday).writerows(csvData1)
with open('Wednesday.csv', 'w+', newline='') as Wednesday:
    csv.writer(Wednesday).writerows(csvData1)
with open('Thursday.csv', 'w+', newline='') as Thursday:
    csv.writer(Thursday).writerows(csvData1)
with open('Friday.csv', 'w+', newline='') as Friday:
    csv.writer(Friday).writerows(csvData1)
with open('Saturday.csv', 'w+', newline='') as Saturday:
    csv.writer(Saturday).writerows(csvData1)

data = csv.reader(open('Dataset.csv'),delimiter=',')
for i in data:
    if x==0:
        x=1
        continue
    if float(i[1])<8:
        #print(i[0]," : Once a week : ",i[1])
        once.append(i[0])
        count+=1
        if count >196:
            break
    elif float(i[1])<10:
        #print(i[0]," : Twice a week : ",i[1])        
        count+=2
        if count >195:
            break
        twice.append(i[0])
    elif float(i[1])<15:
        #print(i[0]," : Thrice a week : ",i[1])
        thrice.append(i[0])
        count+=3
        if count >194:
            break
    if float(i[1])<6:
        continue
n1=0
n2=0
n3=0
y=0
z=0
t=0
b=1
for k1 in thrice:
    n1=y
    n2=t
    n3=b
    print(k1," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Thrice a week")
    d=[[str(k1),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Thrice a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
y=n1
t=n2
b=n3+1
for k2 in twice:
    n1=y
    n2=t
    n3=b
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
    n1=y
    n2=t
    n3=b
    print(k2," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Twice a week")
    d=[[str(k2),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Twice a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1
y=n1
t=n2
b=n3+1
for k3 in once:
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
    n1=y
    n2=t
    n3=b
    print(k3," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Once a week")
    d=[[str(k3),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Once a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1
y=n1
t=n2
b=n3+1
for k4 in thrice:
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
    n1=y
    n2=t
    n3=b
    print(k4," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Thrice a week")
    d=[[str(k4),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Thrice a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1
y=n1
t=n2
b=n3+1
for k5 in twice:
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
    n1=y
    n2=t
    n3=b
    print(k5," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Twice a week")
    d=[[str(k5),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Twice a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1

y=n1
t=n2
b=n3+1
for k6 in thrice:
    if z%28==0:
        y+=1
    if z%7==0:
        t+=1
        if t==4:
            t=0
    if b==8:
        b=1
    n1=y
    n2=t
    n3=b
    print(k6," ",day[y]," ",slot[t][0]," ",slot[t][1]," ",b," Thrice a week")
    d=[[str(k6),str(day[y]),str(slot[t][0]),str(slot[t][1]),str(b),"Thrice a week"]]
    with open('Schedule.csv', 'a+', newline='') as csvFile:
        csv.writer(csvFile).writerows(d)
    z+=1
    b+=1

data1 = csv.reader(open('Schedule.csv'),delimiter=',')
x = 0
for i in data1:
    if x==0:
        x=1
        continue
    if i[1]=="Sunday":
        csvData1 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Sunday.csv', 'a+', newline='') as Sunday:
            csv.writer(Sunday).writerows(csvData1)
    if i[1]=="Monday":
        csvData2 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Monday.csv', 'a+', newline='') as Monday:
            csv.writer(Monday).writerows(csvData2)
    if i[1]=="Tuesday":
        csvData3 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Tuesday.csv', 'a+', newline='') as Tuesday:
            csv.writer(Tuesday).writerows(csvData3)
    if i[1]=="Wednesday":
        csvData4 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Wednesday.csv', 'a+', newline='') as Wednesday:
            csv.writer(Wednesday).writerows(csvData4)
    if i[1]=="Thursday":
        csvData5 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Thursday.csv', 'a+', newline='') as Thursday:
            csv.writer(Thursday).writerows(csvData5)
    if i[1]=="Friday":
        csvData6 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Friday.csv', 'a+', newline='') as Friday:
            csv.writer(Friday).writerows(csvData6)
    if i[1]=="Saturday":
        csvData7 =[[str(i[0]),str(i[2]),str(i[3]),str(i[4])]]
        with open('Saturday.csv', 'a+', newline='') as Saturday:
            csv.writer(Saturday).writerows(csvData7)
