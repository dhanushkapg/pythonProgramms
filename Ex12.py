keyLocation='chair'
homeLocations=['Room1','Kitchen','Closet','Living Room','Bath Room','chair']
for i in homeLocations:
    print(f'search on {i}')
    if i== keyLocation:
        print('key is in the {}'.format(i))
        break
    else:
        print(f'key is not in the {i}')
        continue

for i in range(0,6):
    if i%2==0:
        continue
    else:
        print(i**2)
