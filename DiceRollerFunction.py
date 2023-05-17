from random import *



#input 8d6
def dice_roller(input):
    print('Rolling.... ' + input)

    #split number of dice and dice
    splitInput = input.split("d")

    number_of_dice = int(splitInput[0])
    dice_type = int(splitInput[1])

    result = 0
    
    for dice in range(number_of_dice):
        dice_result = randint(1,dice_type)
        print('dice #' + str(dice) + ' was a ' + str(dice_result))
        result = result + dice_result;
    print(result)


dice_roller('8d6')
