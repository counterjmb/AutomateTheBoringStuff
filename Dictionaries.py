#dictionary datatype is just a list of values and a key pair
myCat = {
    'size':'fat',
    'color': 'black',
    'name': 'dracula'
}

print(myCat['name'])

#there is no index like a list

#when comparing dictionaries, the key value pairs dont need to be in order
pet_1 = {'name': 'Tally', 'species': 'cat', 'age': 8}
pet_2 = {'species': 'cat', 'age': 8, 'name': 'Tally'}
pet_3 = {'species': 'dog', 'age': 8, 'name': 'Bruno'}
print(pet_1 == pet_2)
print(pet_1 == pet_3)


#check if key exists
print('name' in pet_1)
print('name' not in pet_1)

#dictionaries are mutable

#key method prints all keys, no values 
print(pet_1.keys())

#values method prints all values, no keys
print(pet_1.values())

#items method prints keys and values
print(pet_1.items())

for k,v in pet_2.items():
    print(k,v)

for i in pet_3.items(): 
    print(i)

#check if values exists
print('cat' in pet_2.values())

#get method to check if key exists (key to get, default value)
print(pet_2.get('age',0))
print(pet_2.get('date','today'))

picnicItems = {'apples': 2, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins')

#creating default value for pair
pens = {'width': .5, 'type': 'gel'}
print(pens)
pens.setdefault('ink_color', 'black')
print(pens)
pens.setdefault('ink_color', 'blue')
print(pens) #color already exists as black so not 
