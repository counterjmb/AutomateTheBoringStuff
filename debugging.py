#raise exceptions
#raise Exception('The Error message')

import traceback

def boxPrint(symbol, width, height): 
    if len(symbol) != 1: 
        raise Exception('"Symbol" parameter too large')
    if(width < 2) or (height < 2):
        raise Exception('"Width" or "Height" parametters are too small')
    print(symbol * width)
    for i in range(height - 2): 
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('*', 10, 5)

#print log file
try: 
    raise Exception('Exception without breaking')
except:
    errorFile = open('error.log', 'a')
    #errorFile.write(traceback.format_exc())
    errorFile.close()


#assertions: will crash. used for logic testing
test = 10;
assert test > 15



