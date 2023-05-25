openFile=open(r'C:\\Users\011382\Desktop\Temp\test.txt')
#print(openFile.readlines())
#print(openFile.readlines().sort())
getFileLine=openFile.readlines()

openFile.close()
print(getFileLine.sort())