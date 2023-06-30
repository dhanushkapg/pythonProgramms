

def calculateExp(list):
    '''
    
    :param list:
    :return:
    '''
   # list = []
    totalEx = 0
    for i in list:
        totalEx=totalEx+i

    return totalEx
list=[]
totalEx=0
tom_expList = [2100, 3400, 3500]
joe_expList = [200, 500, 700]
print(calculateExp(tom_expList))
print(calculateExp(joe_expList))

def calcTotal(a,b=4):
    print('a',a)
    print('b',b)
    return a+b
    print(a+b)
print(calcTotal(10,20))
#print(a)