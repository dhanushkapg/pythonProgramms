customerName = ['Marion Weaver', 'Alberto Mendoza', 'Katharine Tyler', 'Isaac Steele']
print(customerName[-1])
print(customerName[1:3])
customerName.append('Dhanushka')

customerName.insert(2,'Prasanna')

print(customerName)


list1=[2,4,6]
list2=[4,6,2]
print(list2.remove(6))
print(list2)

if (list1==list2):
    print('True')
else:
    print('False')
print('----------------')
if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
   print(1)
   print(2)
   if 'a' in 'qux':
      print(3)
print(4)


d = {'a': 0, 'b': 1, 'c': 0}
print(d['a'])


d = {'a': 0, 'b': 1, 'c': 0}

if d['a'] > 0:
   print('yeah!')
elif d['b'] > 0:
   print('yeah!')
elif d['c'] > 0:
   print('ok')
elif d['d'] > 0:
   print('ok')
else:
   print('not ok')

a = ['foo', 'bar', 'baz', 'qux', 'corge']

while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')






frequency = []
frequency[0] = 'Monday'
frequency[1] = 'friday'
print(frequency[0])