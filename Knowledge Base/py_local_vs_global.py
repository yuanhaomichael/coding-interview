myGlobal = 5

def func1():
    # to modify a global variable, must reference it with global keyword
    global myGlobal 
    myGlobal+=1
    print(myGlobal)

def func2():
    print(myGlobal) # to read a global variable, no need to use global keyword
func1()
