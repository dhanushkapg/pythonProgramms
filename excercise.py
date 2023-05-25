openGeustFile=open(r"C:\\Users\011382\Desktop\Temp\guest.txt",'w')
listofGuests=['Dhanushka','Prasanna','Gunasinghe']
for gList in listofGuests:
    openGeustFile.write(gList)
    openGeustFile.write("\n")

openGeustFile.close()
readGuestFile=open(r"C:\\Users\011382\Desktop\Temp\guest.txt")
print(readGuestFile.read())