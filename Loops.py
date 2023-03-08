total = 0
for num in range(101): 
    total = total + num
print('For Total: ' + str(total))

whileTotal = 0
i = 0
while i < 101:
    whileTotal = whileTotal + i
    i = i + 1
print('While Total: '+ str(whileTotal))

##Different For range (start, end, increment)
for y in range(20,2,-4):
    print(y)