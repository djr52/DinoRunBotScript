import pyperclip, re, time

phoneNumRegex = re.compile(r"""
((\d?)? #Country code
( |-|\.)? #Seperator
(\d{3}|\(\d{3}\))? #Area code
( |-|\.)? #Seperator
(\d{3}) #First 3 digits
( |-|\.)? #Seperator
(\d{4}) #Last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? #Extension code
)""", re.VERBOSE)
#USA numbers


emailRegex = re.compile(r"""(
[a-zA-Z0-9_\-\.]+ #email username
@[a-zA-Z0-9_\-\.]+ #@ root domain name
\.([a-zA-Z]{2,5})) # must end with top level domain (dot-something)
""", re.VERBOSE)

text = str(pyperclip.paste())
startTime = time.time()
print(phoneNumRegex.findall(text))
print(emailRegex.findall(text))
matches = []


for groups in phoneNumRegex.findall(text):
        phoneNum = ''
        if groups[1] != '':
            phoneNum += '-'.join([groups[1], groups[3], groups[5], groups[7]])
        else:
            phoneNum += '-'.join([groups[3], groups[5], groups[7]])
    
        if groups[10] != '':
            phoneNum += ' x' + groups[10]
        matches.append(phoneNum)

for groups in emailRegex.findall(text):
        matches.append(groups[0])

    #return matches

#matches = findMatches(matches, phoneNumRegex, emailRegex)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard.")
    print("\n".join(matches))
else:
    print("No matches found...")



print("--- %s seconds ---" % (time.time() - startTime))

