street="34/9"
city="Mirigama"
country="Sri Lanka"

address =street+" "+city+ " "+country
print(address)
print(f'{street}, {city}, {country}')

text=f''' my street is: {street}
my city is :{city}
my country is {country}'''

print(text)



setString ='Earth revolves around the sun.'
print(setString[6:14])
print(setString[-5:-1])


vegetables = 30
fruits=50
print(f'I eat {vegetables} veggies and {fruits} fruits daily')

s='maine 200 banana khaye'
newString ='maine 10 samosa khaye'
print(s.replace('200','10').replace('banana','samosa'))
print(s.replace('200 banana','10 samosa'))