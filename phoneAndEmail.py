#! python3
# python -m pip install pyperclip
import re, pyperclip


#phonenumber regex in varying formats
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000
(                               # make everything one large group for print
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)                          # first seperator
\d\d\d                          # first 3 digits
-                               # seperator
\d\d\d\d                        # last 4 digits
(
    ((ext(\.)?\s) |x )          # word ext
(\d{d,5}))?                     # extension number (optional)
)
''', re.VERBOSE)


#regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+                # first half
@                              # @ symbol
[a-zA-Z0-9_.+]+                # domain
''', re.VERBOSE)

#Get text from clipboard
text = pyperclip.paste()

#Extract the emails and phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

#first group in phone number has whole value, the each group. we just need the first one
allPhoneNumbers = []
for phoneNumber in extractedPhone: 
    allPhoneNumbers.append(phoneNumber[0])

#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(results)
#pyperclip.copy(results)