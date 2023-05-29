#traditional way to search string take resources

text="This is my sample list ['Dhanushka','Prasanna','Gunasinghe']"
getIndexStart = text.index("[")
getIndexEnd=text.index("]")
print(getIndexStart)
print(getIndexEnd)
print(text[23+1:59])

#regex re.search function can easy

import re
print(re.search("[a-z]",text))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

print(re.search(r'est',"test"))    # return start to end position of the matching part of the string
print(re.search(r'ep',"hair"))  # return none no match there
print(re.search(r'^xe','xeonon')) # return matching positions from start
print(re.search(r'y$','sseeey  daddy'))# return matching position from end of the line

print(re.search(r'd.g','doggy')) # return position of  any string for .
print(re.search(r'^F','fFdfDFDf',re.IGNORECASE)) #ignore case and return search which is starting line


print(re.search(r'^[Dd]','Dhanushka'))
print('***')
s='saman perera from who born in 19830614'
#print(re.match('[0-9A-Z]',s))  # return first match
print(re.search(r'[0-9][0-9][0-9][0-9]....',s)) # search first match
#print(re.findall('[0-9A-Z]',s)) # find all matches as a list

print(re.search(r'could[0-9]','could8'))
print(re.search(r'cloud[A-Z]','cloudE'))# search

# seach not in the given patten
print(re.search(r'[^a-e]','afddfdwedf'))
print(re.search(r'[^a-z ]','ddddsadasd .')) # return not match character to given se arch cretiria by ^
print(re.search(r'cat|dog','dog c at is fast')) # OR | if there are two matches only get the first one
print(re.findall(r'cat|dog','dog and cat are very innocent ')) # to match more than one search result need to use findall
print(re.search(r'.*ale','sale kale nale, wall')) # * repeated more time ,* any character any time
print(re.search(r'py.*n','python')) #return any number
print(re.search(r'py.*n','python programming')) # in this case search will return any characters any character any number
# of occurance until last character 'n'
print(re.search(r'py.*n ','python programming'))# in this case python search any number of characters
    # only upto ' ' character.
print(re.search(r'py[a-z]*n','python programming')) # replace any character . with [a-z]
print(re.search(r'a+l','all')) #match two or more characters combined search
print(re.search(r'w?game','pgame')) # i here character before ? is optionally match, that must or must not
print(re.search(r'\.com',"my.com")) #escape character use to escape not insert characters that have different meaning.
# in this case . can use to represent any character, but when we use .com we have to use \ before special character
print(re.search(r'\w\s',"&*^&_ ")) # matches alfa numeric and white spaces both
print(re.search(r'A.*','Argentina')) #matches word starting with A any letters next to A
print(re.search(r'A.*','Argentina')) #matches word starting with A any letters next to A
print(re.findall(r'A.*','Argentina')) #matches word starting with A<<
print(re.search(r'A.*a','Argentina')) #matches word starting with A any letters next to A and end with letter n
print(re.search(r'A.*a','Azabaijan')) # this return incomplete string because of word not end with a
#to retreive string patten we must as below
print(re.search(r'^A.*a$','Azabaijan'))
print(re.search(r'^[a-zA-Z_ ][a-zA-Z0-9_ ]*$','wwwee3432sad323E')) #^search alfanumeric(numbers,alphabet) begining and $ search
#alphanumeric end of the string #return True only alphanumenric on the string
print(re.search(r'(1[0-2]|0?[1-9]):[0-5][0-9]\s?[APap][Mm]$','1:00pm'))
#[0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]]
print(re.search(r's?wgame','wgame'))
print('*****')
def check_time(text):
  pattern =r'(1[0-2]|0?[1-9]):[0-5][0-9]\s?[APap][Mm]$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02pm"))