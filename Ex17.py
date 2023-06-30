def calcArea(w,h,shape='trangle'):
    if shape=='trangle':
        area=1/2*w*h
        return area
    elif shape=='square':
        area=w*h
        return area
    else:
        return('wrong selection')

print(calcArea(12,30))

def printPattern(i):
    n=1
    while(n<=i):
        list=[]
        for p in range(n):
            list.append('*')
        print(*list)
        print('\n')
        n=n+1
printPattern(10)


