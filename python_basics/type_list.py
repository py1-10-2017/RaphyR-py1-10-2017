def typeList(list):
    newString = ' '
    newNum = 0
    if all(isinstance(x, int) for x in list):
        print "The list you entered is of integer type"
        print "Sum: ", sum(list)
    elif all(isinstance(x, str) for x in list):
        print "The list you entered is of string type"
        print "String: ", newString.join(list)
    else:
        print "The list you entered is of mixed type"
        for element in list:
            if type(element) == str:
                newString+= element
            elif type(element) == int:
                newNum += element
        print "String: ", newString
        print "Sum: " + str(newNum)


typeList(["Hello",2,3,"World",5,6])
