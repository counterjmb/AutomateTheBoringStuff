import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-6999'

#create object for pattern
#use raw strings since \ are commin in regex 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#create match object
mo = phoneNumRegex.search(message)
#prints 1st occurance 
print(mo.group())

print(phoneNumRegex.findall(message))

#strip out parts with groups
phoneNumRegexStrip = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegexStrip.search(message)
#does not start with 0
print(mo.group(1))

#pipes
batRegex = re.compile(r'Bat(man|mobile|coptor|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())

#repitition matches
# ? 0 or 1 time
batRegex2 = re.compile(r'Bat(wo)?man')
mo1 = batRegex2.search('The Adventures of Batman') #match
mo2 = batRegex2.search('The Adventures of Batwoman') #match
print(mo1.group())
print(mo2.group())


#python does a greedy match, meaning it tries to find the longest value
search_numbers = '1234567890'
greedyDigitRegex = re.compile(r'(\d){3,5}')
print(greedyDigitRegex.search(search_numbers))
nonGreedyDigitRegex = re.compile(r'(\d){3,5}?')
print(nonGreedyDigitRegex.search(search_numbers))