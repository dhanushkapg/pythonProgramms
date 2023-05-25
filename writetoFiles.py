#filetowrite=open('C:\\Users\011382\Desktop\Temp\test.txt','w')
#filetowrite.write("This is my Address")
#filetowrite.close()
with open(r'C:\\Users\011382\Desktop\Temp\test.txt','a') as wFile:
    wFile.write("This is my Address")
    wFile.write("Laxmee ")
    wFile.write("Maladeniya ")
    wFile.write("Mirigama ")

filetowrite=open(r"C:\\Users\011382\Desktop\Temp\test.txt")

print(filetowrite.readlines())
filetowrite.close()
