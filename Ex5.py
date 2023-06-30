expenses = [2200,2350,2600,2130,2190]
print(expenses[1]-expenses[0])
for i in expenses[:2]:
    i=i+1
print(i)

for i in expenses:
    if i==2000:
        print('True')
    else:
        print('False')

expenses.append(1980)
print(expenses)

expenses[3]=expenses[3]-200
print(expenses)


heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
#print(heros)
#heros.remove('thor') and heros.remove('hulk') and heros.insert(1,'doctor ') and heros.insert(2,'strange ')
heros[1:3]=['doctor','strange']

print(heros)

heros=sorted(heros)

print(heros)
