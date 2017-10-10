# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makeTuple(dict):
    new_list = []
    for key,data in dict.iteritems():
        #name_and_number = (key, data)
        new_list.append((key,data))
    print new_list

makeTuple(my_dict)

#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
