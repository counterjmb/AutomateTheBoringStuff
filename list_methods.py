spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hi'))

#Adding values
spam.append('hallo')
print(spam)

spam.insert(1, 'Tag')
print(spam)

#these methods return a None Value so don't do the following: 
test_spam = spam
test_spam.append("test")
print(test_spam) #output is none


remove_list = spam
remove_list.remove('heyas')
print(remove_list)

numbers_list = [1,55,11,17.1,336,114.2,-99]
numbers_list.sort()
print(numbers_list)

#capital letters are sorted before lowercase
words_list = ['Ant', 'aardvark', 'cat', 'Zebra', 'bat']
words_list.sort()
print(words_list)