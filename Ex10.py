exp=['20121','23131','45454','433443']
totalExp=0
for i in exp:
    totalExp=totalExp+int(i)

print(totalExp)


for i in range(1,10):
    print(i)
    print(i*i)
print('-----')
totalEx=0
for y in range(len(exp)):
    print(f'expenses of month {y+1} is {exp[y]}')
    #print('expenses of month {} is {}'.format(y+1,exp[y]))
    totalEx=totalEx+exp[y]
