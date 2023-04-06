test_list = [1,5,47,44,55,66,33,22]
for item in test_list: 
    print(item)


#Populate list: range(start, end, incriment by)
generated_list = list(range(0,100,2))
print(generated_list)

for i in range(len(generated_list)):
    print('Index ' + str(i) + ': ' + str(generated_list[i]))


#get variables. multiple assignment 
item_sword = ['sword','1d8', 'bludgeoning']
item_name = item_sword[0]
item_damage_dice = item_sword[1]
item_damage_type = item_sword[2]
print('A ' + item_name + ' does '+ item_damage_dice + ' ' + item_damage_type)

item_whip = ['whip','1d4', 'slashing']
item_name, item_damage_dice, item_damage_type = item_whip
print('A ' + item_name + ' does '+ item_damage_dice + ' ' + item_damage_type)

item_name, item_damage_dice, item_damage_type = 'lance', '2d6', 'piercing'
print('A ' + item_name + ' does '+ item_damage_dice + ' ' + item_damage_type)

#swap
a = 'aaaa'
b = 'bbbb'
print(a + b)
a, b = b, a
print(a + b)

#increment
counter = 1
counter += counter
print(counter)