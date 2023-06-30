exp=['20121','23131','45454','433443']
totalEx=0
for y in range(len(exp)):
    print(f'expenses of month {y+1} is {exp[y]}')
    #print('expenses of month {} is {}'.format(y+1,exp[y]))
    totalEx=totalEx+int(exp[y])
print(totalEx)
