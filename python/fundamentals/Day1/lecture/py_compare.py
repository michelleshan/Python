
def return_a_variable():
    strAndNum = 'Day' + str(1)
    myVariable = 10
    return myVariable
print(return_a_variable())

def ifStatement():
    myVariable = 50
    bool = False
    if(myVariable==99999 and True):
        myVariable -= 1
        print("To infinity")
    elif(myVariable==50):
        myVariable += 1
        print("And beyond")
    else:
        print("YOU. ARE. A. TOY!")
    return myVariable
print(ifStatement())

def forLoops(arr):
    arr.pop()
    arr.append(6)
    for i in range(0,len(arr),1):
        print(arr[i])
    for i in arr:
        print(i)
forLoops([3,7,2,9])