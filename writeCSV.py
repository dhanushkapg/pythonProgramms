import csv
a=[['Dhanushka','0718175098','Mirigama'],['Oshani','0718546190','Mirigama']]
#f=open(r'C:\Users\011382\Desktop\Temp\guest.csv','w')
#for i in f:
with open(r'C:\Users\011382\Desktop\Temp\guest.csv','w') as f:
    getwriter=csv.writer(f)
    getwriter.writerows(a)

