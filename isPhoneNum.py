import re

phoneNumReg = re.compile(r'(\d{1,3})?-(\d\d\d-\d\d\d\d)')

match = phoneNumReg.findall('My phone number is 201-270-8615 and 201-675-8535')
print(match)
#print(match.groups())
print(phoneNumReg.search('hello'))

