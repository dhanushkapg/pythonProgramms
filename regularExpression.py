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

print('Group ')
#CAPTURING GROUPS

result= re.search(r'(\w*),(\w*),(\w*)','test,mess,test3')
result1=re.search(r'[A-Za-z].*,[A-Za-z].*','test1_222,test2')
result2=re.search(r'[a-zA-Z]+','test1_222,test2')
print(result)
print(result.groups())
print(result1)
print(result1.groups())
print(result2)
print(result2.groups())
print(result[2])


def reExpress(name):
    result=re.search(r'^(\w*),(\w),(\w*)$',name)
    print(type(result))
    print(result)
    print(result[3])
    return 'name is {} {} {}'.format(result[1],result[2],result[3])
print(reExpress('Dhanushka,9,Gunasinghe'))

#repeating qualifiers
print('repeating qualifiers ')
print(re.search(r'[a-zA-z]{5}','a man is on the tables'))
print(re.findall(r'[a-zA-Z]{5}','ghost a fashio the table')) #find all return all the matching results as a list

print(re.findall(r'\b[a-zA-Z0-9]{3}\b','cat mat hat sat soon pan fan 501 2001')) #\b search words with three characters
#['cat', 'mat', 'hat', 'sat', 'pan', 'fan', '501']
print(re.findall(r'\b\w{3}\b','sat mat process fat 001')) #another way--> we can use \w{3} for find alfanumeric characters
#['sat', 'mat', 'fat', '001']
print(re.findall(r'\b\w{1,3}\b','the man san fan a an four fiive'))#in this case i used \b(word counter begining and end).so only
#return 3 letter characters['the', 'man', 'san', 'fan', 'a', 'an']
print(re.findall(r'\w{1,3}','the man san fan a an four fiive'))# in this case i used w{1,3} alfanumeric words letter between 1 to 3
# this will return divided any one into three characters ['the', 'man', 'san', 'fan', 'a', 'an', 'fou', 'r', 'fii', 've']
print(re.findall(r'\w{3,10}','test 12345678942')) #find all more than 3 characters and less than 10 characters
print(re.findall(r'\b\w{3,5}\b','te2ww'))#in this case i used /b start and end, Then it return words exsactly equal to give number
#of characters in here {3,5}
print(re.findall(r's\w{,20}','i really like sun strawberries')) # in here find all that start with s and character count 0 to 20

#search process id from log file
print(re.findall(r'[0-9]+','est sts s [12454]')) # this returns numberical values in the string...+ means continuesly return
# numbers til end
print(re.findall(r'\[(\d+)\]','dasdsd[12312]')) #this \d returns 0-9 with \[ means  wild card
result=re.findall(r'\[(\d+)\]','this is my number [12333] fdjff [33323333]')
print(result[0])
print(result[1])
print(re.findall(r'\[\d+\]','dasdsd[12312]'))

def getPid(log_line):
    regEXFun=r'\[(\d+)\]'
    result=re.findall(regEXFun,log_line)
    if result is None:
        return ''
    return result[0]
print(getPid('this is log line[4333]'))


#regEXFun1=
result=re.search(r'\[(\d+)\]: [A-Z]*','July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade')
print(result[0])
print(result[0].split(":"))
test=result[0].split(":")

print('{} ({})'.format(test[0][1:-1],test[1].strip()))

# split regular expression (we use regex instead of delimeter to split the string
print(re.split(r',','Dhanushka,Prasanna,Gunasinghe'))
print(re.split(r'([,/])','Dhanushka,Prasanna/Gunasinghe')) #return split string and delimeters use to split
print(re.split(r'[(,/)]','Dhanushka,Prasanna/Gunasinghe'))

#sub regular expression
print(re.sub(r'[\w.%+-]+@[\w.-]+','test','this email is send from dhanushkapg@slt.com.lk'))# sub funtion replace test in to search result
print(re.findall(r'[\w.*]+@[\w.*]+','this email is send from dhanushkapg@slt.com.lk')) #both are return same string set
print(re.findall(r'[\w.%+-]+@[\w.-]+','this email is send from dhanushkapg@slt.com.lk'))#
print(re.sub(r'[\w*]+@[\w*]+','test','this is my email from dhanushkapg@slt.com.lk'))
print(re.sub(r'[\w*]+@[\w*]+','test','this is my email from dhanushkapg@slt.lk'))

print(re.findall(r'[\w]*,[\w]*',"Lovelace,Ada"))
result=re.findall(r'[\w]*,[\w]*',"Lovelace,Ada")

print(re.split(r" the ", "One sentence. Another one? And the last one!"))

print(re.sub(r'([\w.*]),([\w.*])','\2\1','test1,test2'))

print(re.findall(r'\d+-\d+-\d+','Sabrina Green,802-867-5309,System Administrator'))
getTelNumber=re.findall(r'\d+-\d+-\d+|\d+-\d+','Eli Jones,684-3481127,IT specialist')
print(getTelNumber)
telNum=getTelNumber[0]
print(telNum)
telNum="+1-"+telNum
print(telNum)
print(re.sub(r'\d+-\d+-\d+|\d+-\d+',telNum,'Eli Jones,684-3481127,IT specialist'))


#print(re.findall(r'[aeiou][a-z]*','courageous'))
print(re.findall(r'\w*[a|e|i|o|u]{3}[a-z]\w*','The rambunctious children had to sit quietly and await their delicious dinner.'))


print(re.findall(r'[#]{1,}','### Start of program'))

print(re.sub(r'[#]{1,}','//','### Start of program'))
print(re.findall(r'(\d+)-...','My number is 212-345-9999.'))

telPart=re.findall(r'(\d+)-...','My number is 212-345-9999.')
print(telPart[0])
print(telPart)
telPart1=telPart[0]
telPart='('+telPart1+')'
print(re.sub(telPart1,telPart,'My number is 212-345-9999.'))
import string
lastDigits=re.findall(r'(\d+).?$','My number is 212-345-9999.')
print(lastDigits)
lastDigitasString=lastDigits[0]
print(lastDigitasString)

print(len(lastDigitasString))

print('****************************************')
import re
def convert_phone_number(phone):
  firstPart=re.findall(r'(\d+)-...',phone)
  if(len(firstPart)<=0):
    return phone
  else:
    strFirstPart=firstPart[0]
    lastPart=re.findall(r'(\d+).?$',phone)
    if(len(lastPart)<=0):
      return phone
    else:
      strLastPart=lastPart[0]
      if len(strLastPart)!=4:
        return phone
      else:
        setStrFirst='('+strFirstPart+')'
        result=re.sub(strFirstPart+'-',' '+setStrFirst,phone)
        return result




print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



def checkEmail(emailAddress):
    print(re.findall(r'^[a-z]*',emailAddress))
    strList=re.findall(r'^[a-z]*',emailAddress)
    strURL=strList[0]
    print(strURL)
    result=re.sub(strURL,'xyz',emailAddress)
    return result

emailList=['abc.edu','pqr.edu','saman.com']
getCount=0
for i in emailList:
    if i =='abc.edu':
        emailList[getCount]=checkEmail(i)

getCount=getCount+1




print(emailList)
emailList.sort()
print(emailList)