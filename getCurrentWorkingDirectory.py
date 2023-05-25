import os
print(os.getcwd()) # get current working directory

os.chdir(r'C:\Users\011382\Desktop\Temp') #change working directory
print(os.getcwd())#get current working directory
os.mkdir(r'C:\Users\011382\Desktop\Temp\newDirectory') #make new directory
os.renames('newDirectory','newFolder')
os.mkdir(r'C:\Users\011382\Desktop\Temp\newDirectory')
f = open(r'C:\Users\011382\Desktop\Temp\newDirectory\myfile.txt', 'w')
f.write("Dhanushka")
print(os.listdir(r'C:\Users\011382\Desktop\Temp\newDirectory')) #list all files inside directory
os.rmdir(r'C:\Users\011382\Desktop\Temp\newFolder') # remove directory
os.getcwd()

