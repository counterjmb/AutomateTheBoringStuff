print('cat','dog','horse')
print('cat','dog','horse', sep=', ')


#printing long strings
print('Four score and seven ' + \
      'years ago....')

#strings are not mutable

#escape characters
string_with_no_char = 'This is a cat'
string_with_one_char = 'This is Brandon\'s cat'
string_with_double_quotes = "This is Brandon's cat"
#raw string
r'This is carol\'s cat'
multi_line_string = '''
This is line 1
this is line 2
this is line 3
'''

## Methods
# methods return a new string since strings are immutable
test = 'Test string'
print(test.upper())
print(test.lower())
print(test.isupper())
print(test.islower())
print(test.upper().isupper())
#lots of other methods

print(','.join(['cats', 'dogs', 'sheep']))
print('my name is james'.split())
print('my name is james'.split('m'))

#adds spaces to get to 10 characters
print('hello'.rjust(10)) 
#specify padding
print('hello'.rjust(10,'_'))

print('    Hello'.strip())
print(' x  '.rstrip())
print(' x  '.lstrip())
print('spamSpamspma'.strip('s'))
print('Hello'.replace('e','eeee'))

#pyperclip module can manipulate clipboard methods