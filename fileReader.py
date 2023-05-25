#getFile = open("C:\\Users\011382\Desktop\Temp\test.txt", "r")
#print(getFile.read())

#f = open("C:\\Users\011382\Desktop\Temp\test.txt", "r")
#print(f.read())

#f=open(r"C:\\Users\011382\Desktop\Temp\test.txt","r")
#print(f.readlines())
#print('*****')
with open(r"C:\\Users\011382\Desktop\Temp\test.txt") as f:
    for line in f:
        print(line.upper().strip())



#f=open(r"C:\\Users\011382\Desktop\Temp\test.txt","r")
#print(f.readlines())