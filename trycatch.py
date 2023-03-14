def divideBy(x):
    try:
        return 42 / x
    except ZeroDivisionError as e:
        print('error: Divided by 0')
    except ValueError as d: 
        print('error: Not a number')


print(divideBy(4))
print(divideBy(42))
print(divideBy(0))
#TODO: research muliple line exceptions
#print(divideBy('cc'))