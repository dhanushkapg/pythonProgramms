list1=['Dhanushka','Prasanna','Gunasinghe']
print(list1[0])
list1.append('Dilini')
list1[0]='Nuwan'

print(list1)

tuple1=('Dhanushka','Prasanna','Gunasinghe')
print(tuple1[0])
idx=tuple1.index('Prasanna')
print(idx)
newtuple=tuple1[:idx]+tuple1[idx+1:] #remove item from tuple we have to slice tuple into two
#parts
print(newtuple)


dictionary1={'name':'Dhanushka','age':40,'Address':'Mirigama'}
print(dictionary1)
print(dictionary1['name'])


dictionary1['Gender']='Male'
print(dictionary1)
del dictionary1['Address'] # delete dictionary item
print(dictionary1)



QUANTITY=500
print(QUANTITY)


for i in range(0,5):
    print(i)

    '''
    this is multi line comment  
    '''
"""
ddd
"""


'''
'''



