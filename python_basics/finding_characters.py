new_list = []
def findtheChar(list, char):
    for word in list:
        if char in word:
            new_list.append(word)
    print new_list

findtheChar(['hello','world','my','name','is','Anna'], 'o')
