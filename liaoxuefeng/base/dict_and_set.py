
# dict and set
# Just like C++

# dict and set uses hash algorithm
# dict --> hash_map
# set --> hash_set

# They act almost the same

# Examples about dict

dict_names = dict({"20190001":"Tom", "20190002":"Jerry"})

print (dict_names)

for key in dict_names:
    print ("id=%s,name=%s" % (key,dict_names[key]))

other_name = "20190003"
if (dict_names.get(other_name) == None):
    print ("name <%s> not exist" % (other_name))

# How to modify ?

 # Examples about set

set_id = set(["X", "Y", "A"])

print (set_id)

set_id.add("B")

print (set_id)