india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input('Please enter city')
if city in india:
    print('indian')
elif city in pakistan:
    print('pakistan')
elif city in bangladesh:
    print('bangaladesh')
else:
    print('country not listed')



city1= input('please enter city 1 ')
city2= input('please enter city 2 ')
if city1 in india and city2 in india :
    print('both cities in india')
elif city1 in bangladesh and city2 in bangladesh:
    print('both cities in bangaladesh')
elif city1 in pakistan and city2 in pakistan:
    print('both cities in pakistan')
else:
    print('both cities not in same country')


sugarLevel=input('Enter your sugar level')
sugarLevel=int(sugarLevel)
if 80<sugarLevel<100:
    print('sugar level normal')
elif sugarLevel<80:
    print('sugar level low')
elif sugarLevel>100:
    print('sugar level high')
else:
    print('enter wrong input')