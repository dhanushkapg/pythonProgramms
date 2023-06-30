info=[600,630,620]
ril=[1430,1490,1567]
mtl=[234,180,160]
myDictionary={"info":info,"ril":ril,"mtl":mtl}
command=input('enter command')
if command=='print':
    for k,v in myDictionary.items():
        print(k,"======>",myDictionary[k],'avg:',sum(myDictionary[k])/len(myDictionary[k]))
if command=='add':
    flag=0
    getStock=input('get Stock Name')
    for k,v in myDictionary.items():
        #print(myDictionary[k])
        if getStock==k:
            flag=1
            break
        else:
            flag=0

    if flag==1:
        print(myDictionary[getStock])
        getAmount=input('Please enter Amount')
        myDictionary[getStock].append(int(getAmount))
        print(myDictionary[getStock])
    else:
        getAmount = input('Please enter Amount')
        list1=[]
        list1.append(getAmount)
        myDictionary[getStock]=list1
        print(myDictionary)



