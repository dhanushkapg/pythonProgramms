name = input('please enter your name ')

print("My Name is : {}".format(name))

age=input('please enter your age')
age=int(age)
print(age)
print(type(age))


def toSecond(hours,minues,seconds):
    return(hours*3600+minues*60+seconds)

getHours=int(input('please enter hours'))
getMinutes=int(input('please enter minues'))
getSeconds=int(input('please enter seconds'))

print(toSecond(getHours,getMinutes,getSeconds))


import os
print(os.environ.get('HOME'))
