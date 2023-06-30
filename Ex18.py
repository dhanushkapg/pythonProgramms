y={'Name':'Dhanushka','Age':38,'Address':'Mirigama'}
print(y['Name'])
y['Age']=40
print(y)

x=(10,20,30)
print(x)
print(x[1])
del(y['Name'])
print(y)
for key in y:
    print(y[key])
print('-----')
for k,v in y.items():
    print(k)

#identify specific key in the dictionary
for k in y.items():
    if k =='Address':
        print(f'{y[k]} is the value')