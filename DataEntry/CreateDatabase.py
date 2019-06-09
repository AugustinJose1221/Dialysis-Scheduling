import csv
csvData=[['14464','8.4913890, 76.9447201','Thiruvananthapuram,Government Ayurveda College Hospital Thiruvanantha','Public Government','0','0','0','Thiruvananthapuram','Kerala','Thiruvananthapuram','8','695002'],['14558','8.3566671, 76.9280601','Trivandrum Medical College,Medical College PO, Thiruvananthapuram, Kerala','Government Medical College, Thiruvananthapuram','Public Government','Hospital','Allopathic','Trivandrum Medical College, Medical College PO','Kerala','Thiruvananthapuram','18','695011'],['14517','8.5744441, 76.8683301','Kazhakuttom','C.S.I. Mission Hospital','0','0','0','Kazhakuttom','Kerala','Thiruvananthapuram','8','695101'],['14475','8.1672221, 77.4319401','Beach Road,Nagercoil','Blessing Hospital','0','0','0','Beach Road,Nagercoil','Kerala','Thiruvananthapuram','4','695005']]
with open('Hospital_Dataset1.csv', 'w+', newline='') as csvFile:    #Creating database with hospital details
    csv.writer(csvFile).writerows(csvData)
csvFile.close()
csvData1=[['ID','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28'],['14464','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8'],['14558','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18','18'],['14517','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8','8'],['14475','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4']]
with open('Hospital_Dataset2.csv', 'w+', newline='') as csvFile:    #Creating database with booked bed data
    csv.writer(csvFile).writerows(csvData1)
csvFile.close()
csvData3=[['Hospital ID','Patient ID','Day','Starting Time']]
with open('Requests.csv', 'w+', newline='') as csvFile:     #Creating database with each booking details
    csv.writer(csvFile).writerows(csvData3)
csvFile.close()
#Hospital data:
#14464,"8.5241391, 76.9366376",Thiruvananthapuram,Government Ayurveda College Hospital Thiruvanantha,Public/ Government,0,0,Thiruvananthapuram,Kerala,Thiruvananthapuram,8,695002
#14558,"8.5241391, 76.9366376","Trivandrum Medical College,\nMedical College PO, Thiruvananthapuram, Kerala.","Government Medical College, Thiruvananthapuram",Public/ Government,Hospital,Allopathic,"Trivandrum Medical College, Medical College PO",Kerala,Thiruvananthapuram,18,695011
#14517,"8.5241391, 76.9366376",Kazhakuttom,C.S.I. Mission Hospital,0,0,0,Kazhakuttom,Kerala,Thiruvananthapuram,8,695101
#14475,"8.5241391, 76.9366376","Beach Road,Nagercoil",Blessing Hospital,0,0,0,"Beach Road,Nagercoil",Kerala,Thiruvananthapuram,4,695005

