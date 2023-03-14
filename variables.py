def localValues():
    global eggs
    eggs = 'changed in local'
    print(eggs)

eggs = 42
print(eggs)
localValues()
print(eggs)