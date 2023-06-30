i=1
l=[]
while(i<=5):
    y=1
    for y in range(i):
        l.append('*')
        #print('*')
        y=y+1
    print(*l)
    l = []
    print('\n')
    i=i+1
