import logging

#configure level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#disable debug statements
#logging.disable(logging.CRITICAL)


logging.debug('Start program')

def factorial(n):
    total = 1
    for i in range(1,n + 1): 
        total *= i
        logging.debug('i: %s, total: %s' % (i, total))
    return total


print(factorial(5))

logging.debug('End program')