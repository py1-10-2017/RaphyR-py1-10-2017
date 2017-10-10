
myInfo = {
"name" : "Raphy",
"age"  : "24",
"country" : "USA",
"language" : "Python"
}

print "My name is " + myInfo["name"] + "\nMy age is " + myInfo["age"] + "\nMy country of birth is " + myInfo["country"] + "\nMy favorite language is " + myInfo["language"]

def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)
