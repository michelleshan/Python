import random
def randInt(min=0, max=100):
    if(min > max or max < 0):
        return False
    else:
        num = round(random.random()*(max-min)+min)
        return num
print(randInt(min=10,max=20))

