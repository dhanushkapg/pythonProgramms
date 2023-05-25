import csv
import os
f=open(r'C:\Users\011382\Desktop\Temp\guest.csv')
#print(f.read())
a=[]
readCSV=csv.reader(f) # read CSV
#for id in range(0,2):
#id=0
#for i in readCSV:
  #  a.insert(id,i)
   # id=id+1
#print(a)

for d in readCSV:
    name,telNum,twn=d
    #print(name)
    print('Name {},phone {},town {}'.format(name,telNum,twn))


