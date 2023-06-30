result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
headCount=0
tailCount=0
for i in result:
    if i=="heads":
        headCount=headCount+1
    elif i=="tails":
        tailCount=tailCount+1
    else:
        print('wrong input')
print(f'head count is {headCount}')
print(f'tail count is {tailCount}')

for i in range(1,11):
    if i%2 == 0:
        continue
    else:
        print(i**2)



expense_list = [2340, 2500, 2100, 3100, 2980]
expense_month=['january','february','march','april','may']
getExpenses=input('get Expenses ')
getExpenses=int(getExpenses)
for i in range(len(expense_list)):
    if getExpenses==expense_list[i]:
        print(f'This is expenses of {expense_month[i]}')
        break
    else:
        print('Expenses not match the month')

i=0
distance=5
while(i<distance):
    i=i+1
    getMessage=input('Are you tierd?')
    if getMessage=='yes':
        print("you didn't finish the rance")
        break
    elif getMessage=='no':
        continue
    else:
        print('you type wrong information')
if i==distance:
    print('congratulation')