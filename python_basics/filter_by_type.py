sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def isTypeOf(variable):
    if isinstance(variable, int):
        if variable < 100:
            print "That's a small number!"
        else:
            print "That's a big number!"
    elif isinstance(variable, str):
        if len(variable) > 50:
            print "Long sentence"
        else:
            print "Short sentence"
    elif isinstance(variable, list):
        if len(variable) > 10:
            print "Big list!"
        else:
            print "Short list!"

isTypeOf(sI)
isTypeOf(mI)
isTypeOf(bI)
isTypeOf(sS)
isTypeOf(mS)
isTypeOf(bS)
isTypeOf(aL)
isTypeOf(lL)
isTypeOf(spL)
