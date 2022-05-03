import csv,os
from tkinter.messagebox import NO
import pandas as pd
import time,datetime
from csv import reader
import glob

columnNames = ['ID' , 'Name' , 'Date' , 'Time']
df = pd.read_csv("data.csv",names=columnNames)

totalStudents = df.ID 

studentData = {}

counter = 1

while counter < len(totalStudents):
    studentData[totalStudents[counter]] = 0
    counter+=1




check = []

base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir,"Attendance")
totalDays = 0
daysRecord = []
for root,dir,files in os.walk(image_dir):
    for file in files:
        if file.endswith("csv"):
            totalDays+=1
            path = os.path.join(root,file)
            ff = os.path.basename(path)
            os.chdir("C:/Users/Vartika/OneDrive/Desktop/new_project/Attendance")
            with open(ff,'rt') as csvfile:
                for line in csvfile.readlines():
                    full = line.split()
                    first = full[0]
                totalColumns = len(full)
                csvfile.seek(0)
                next(csvfile)
                reader = csv.reader(csvfile)
                usedColumns = [0]
                for row in reader:
                    content = list(row[i] for i in usedColumns)
                    data = [int(i) for i in content]
                    
                    check = check + data
                daysRecord.append(set(check))           


for i in daysRecord:
    print(i,"\n")

check = []
for days in daysRecord:
    for students in days:
        check.append(students)
       

for i in check:
    studentData[str(i)]+=1
        

print(studentData)
os.chdir('..')
with open('aggrAttendance.csv','w',newline='') as t,open('data.csv','r') as d:
    writer = csv.writer(t)
    writerTemp = csv.reader(d)
    next(writerTemp)
    writer.writerow(['ID','Name','Total Attended','Total Classes'])
    for (key,value) in studentData.items():
        for row in writerTemp:
            writer.writerow([key,row[1],value,totalDays])
            break
os.startfile(os.getcwd() + './aggrAttendance.csv')                     




