y={'Name':'Dhanushka','Age':38,'Address':'Mirigama'}
for p,q in y.items():
    print(p)
    #print(v)
    if p=='Address':
        print(f'value of Address is {y[p]}')

print('Name' in y)