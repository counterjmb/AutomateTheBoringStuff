exampleList = ['cat', 'dog', 'fish', 'bird', 'small humans']
#lists are just arrays

print(exampleList[1]) #dog

#lists of lists
list_of_lists = [['1','2'],['a','b']]
print(list_of_lists[0]) #['1', '2']
#send mulitple indexes to get values
print(list_of_lists[0] [1]) #2

#negative indexes get last elements
print(exampleList[-1]) #small humans
print(exampleList[-2]) #bird

#Slices: getting several values form a list
print(exampleList[1:3]) #['dog', 'fish']