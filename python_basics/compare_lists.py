list_one = [1,2,5,6,2]
list_two = [1,2,5,6,5,3]

def compare(a, b):
    if set(a) == set(b):
        print "The lists are the same"
    else:
        print "The lists are not the same"

compare(list_one, list_two)
