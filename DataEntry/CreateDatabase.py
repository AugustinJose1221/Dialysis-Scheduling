import csv
csvData=[['14464','8.7294441, 76.7330601','Varkala','Sivagiri Sreenarayana Medical Mission Hospital','0','0','0','Varkala','Kerala','Thiruvananthapuram','8','695141'],['14558','8.3566671, 76.9280601','Trivandrum Medical College,Medical College PO, Thiruvananthapuram, Kerala','Government Medical College, Thiruvananthapuram','Public Government','Hospital','Allopathic','Trivandrum Medical College, Medical College PO','Kerala','Thiruvananthapuram','18','695011'],['14517','8.5744441, 76.8683301','Kazhakuttom','C.S.I. Mission Hospital','0','0','0','Kazhakuttom','Kerala','Thiruvananthapuram','8','695101'],['14475','8.5163890, 76.9402801','Vrindhavan Gardens','Sree Uthradam Thirunal Hospital, Thiruvananthapuram','0','0','0','Palace View Road,Pattom','Kerala','Thiruvananthapuram','7','695004']]
with open('Hospital_Dataset1.csv', 'w+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData)
csvFile.close()
csvData1=[['ID','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28'],['14464','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8'],['14558','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18'],['14517','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8'],['14475','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7']]
with open('Hospital_Dataset2.csv', 'w+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData1)
csvFile.close()
csvData3=[['Hospital ID','Patient ID','Day','Starting Time']]
with open('Requests.csv', 'w+', newline='') as csvFile:
    csv.writer(csvFile).writerows(csvData3)
csvFile.close()
#14464,"8.7294441, 76.7330601",Sivagiri Sreenarayana Medical Mission Hospital,0,0,0,Varkala,Kerala,Thiruvananthapuram,8,695141
#14558,"8.5241391, 76.9366376","Trivandrum Medical College,Medical College PO, Thiruvananthapuram, Kerala.","Government Medical College, Thiruvananthapuram",Public/ Government,Hospital,Allopathic,"Trivandrum Medical College, Medical College PO",Kerala,Thiruvananthapuram,18,695011
#14517,"8.5241391, 76.9366376",Kazhakuttom,C.S.I. Mission Hospital,0,0,0,Kazhakuttom,Kerala,Thiruvananthapuram,8,695101
#14475,"8.5163890, 76.9402801","Sree Uthradam Thirunal Hospital, Thiruvananthapuram",Vrindhavan Gardens,0,0,0,"Palace View Road,Pattom",Kerala,Thiruvananthapuram,7,695004

