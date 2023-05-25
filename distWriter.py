import csv
a=[{'Name':'Dhanushka','Age':31,'Address':'Mirigama'},{'Name':'Oshani','Age':31,'Address':'Mirigama'}]
# dictionary inside list
#[{},{},{}]
keys=['Name','Age','Address']
with open(r'C:\Users\011382\Desktop\Temp\guest.csv','w') as guestFile: # open file
    distWriterObj=csv.DictWriter(guestFile,fieldnames=keys) # create object from csv dict writer  object created file
    # file and assign dictionary keys as headers
    distWriterObj.writeheader() # hearder writign
    distWriterObj.writerows(a) # write all dictionary elements as rows
