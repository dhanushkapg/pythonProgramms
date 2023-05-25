import csv
with open(r'C:\Users\011382\Desktop\Temp\guest.csv','r') as f:
    getDictReader=csv.DictReader(f)
    for i in getDictReader:
        print('Name : {}, Mobile:{} and Town:{}'.format(i['name'],i['telnumber'],i['town']))
