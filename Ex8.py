srilankan=['rice','rotti','bread']
indian=['samosa','naan','dhall']

meal=input('please enter meal ')

if meal in srilankan:
    print('this is srilankan meal')
elif meal in indian:
    print('this is indian meal')
else:
    print('meal is not srilankan or indian')