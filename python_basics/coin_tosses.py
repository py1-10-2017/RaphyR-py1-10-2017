import random

def headOrTail(max):
    head = False
    tail = False
    headCount = 0
    tailCount = 0
    for num in range(1, max):
        coin = random.randint(0, 1)
        isHead = ""
        isTail = ""
        if coin == 0:
            head = True
            tail = False
            isHead = "It's a head!"
            headCount+=1
            print "Attempt #{} Throwing a coin... {} ... Got {} heads so far and {} tails so far".format(num, isHead, headCount, tailCount)
        elif coin == 1:
            head = False
            tail = True
            isTail = "It's a tail!"
            tailCount+=1
            print "Attempt #{} Throwing a coin... {} ... Got {} heads so far and {} tails so far".format(num, isTail, headCount, tailCount)

headOrTail(5001)
