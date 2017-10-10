users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#  for value in data:
for group in users:
    print group
    for index, name in enumerate(users[group]):
        first_name = name["first_name"]
        last_name = name["last_name"]
        print "{} - {} {} - {}".format(index + 1, first_name, last_name, len(first_name + last_name))
    # print i, group



    #      print value["first_name"] + " " + value["last_name"]
