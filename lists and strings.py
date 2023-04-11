import copy

#many list funtions work on strings as well
name = "James"
print(name[0])
print(name[1:3])
print('es' in name)
print('ZZ' in name)
for letter in name:
    print(letter)

#Stings are immutable 
#you'd need to create a new string or overwrite

#strings work on variable references
list1 = [0,1,2,3,4,5]
list2 = list1
list2[1] = 'hello'
print(list2)
print(list1)

#bug example
def eggs(passed_paremeter): 
    passed_paremeter.append('Hello')


spam = [1,2,3]
eggs(spam)
print(spam)
#end bug example


#deep copy function to copy lists
list_a = [1,2,3,4,5,6,7,8,9]
list_b = copy.deepcopy(list_a)
list_b[1] = 'Two'
print(list_a)
print(list_b)