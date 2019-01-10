zoo = ("elephant", "lion", "bear")
print("animal", zoo[1])
print("does an elephant exist?", "elephant" in zoo)

#Create a variable for each of the animals in your tuple with
# this cool feature of Python.
(lizard, fox, mammoth) = zoo
print("lizard is ", lizard)

my_newlist = list(zoo)
print("what type is the zoo now", type(my_newlist))
new_animals = ["monkey", "zebra", "flamingo"]
my_newlist.extend(new_animals)
print("all the animals", my_newlist)
tuple_list = tuple(my_newlist)
print("what type is the zoo now 2", type(tuple_list))
print("final tuple", tuple_list)
