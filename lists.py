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

#Changing items in a list
modifiable_list = [10,20,30,40]
print(modifiable_list)
modifiable_list[1] = 21
print(modifiable_list)
modifiable_list[1:3] = [23,31]
print(modifiable_list)
modifiable_list[:2] = [15,25]
print(modifiable_list)
modifiable_list[2:] = [36,41]
print(modifiable_list)

del modifiable_list[2]
print(modifiable_list)

str_to_list = list('Hello')
print(str_to_list)

print(25 in [13,14,66,47,25,33])
