countryPopulation={'China':143,'India':136,'USA':32,'Pakistan':21}
print(countryPopulation)
print(countryPopulation['China'])
userCommand=input('Enter the command')

if userCommand=='print':
    #for k,v in countryPopulation.items():  #both dictionary iteration is true
    for k in countryPopulation:
        #print(k)
        #print(v)
        print(k,'====>',countryPopulation[k])

elif userCommand=='add':
    getCountry=input('Please enter country')
    flag = 0
    for p in countryPopulation:
        if getCountry==p:
            print('country is exist')
            flag=1
            break
        else:
            flag=0

    if flag==0:
        print('country is not exist')
        getPopulation=input('get Population')
        countryPopulation[getCountry]=getPopulation
    print(countryPopulation)


