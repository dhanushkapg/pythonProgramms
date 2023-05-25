import os
if (os.path.isfile(r'C:\Users\011382\Desktop\Temp\test2.txt')==True):
    print('File Exist')
else:
    print('File not Exist')

print(os.path.getsize(r'C:\Users\011382\Desktop\Temp\test2.txt')) # get file size

print(os.path.getmtime(r'C:\Users\011382\Desktop\Temp\test2.txt')) #last modified time