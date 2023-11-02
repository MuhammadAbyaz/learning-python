# Lists
print(type([]))

# Since everything in python is object we can make list by calling list()
names = list()
names = ["Abyaz", "Khalid", "Hasham"]
# accessing an item in a list
print(names[0])

# gives the length of the list
print(len(names))

# sorting the list
# there are two ways of sorting a list
numbers = [1, 65, 643, 24, 6, 8, 10]
# it will return a new sorted list and the old list will remain the same
sorted(numbers, reverse=True)

# it will not return a new sorted list
numbers.sort()

# adding to list
# .append() and insert(pos,value)
names.append("Ambreen")
numbers.insert(1, 5)

# combine two lists
# .extend()
color = ["red", "orange", "yellow"]
rainbow = ["violet", "indigo", "blue"]
color.extend(rainbow)

# check for certain value in a list
print("green" in rainbow)

# finds the index of certain value
# it gives the index of first value it finds
print(names.index("Abyaz"))

# how man time an item appear in a list we will use count method
print(names.count("red"))

# removing item from the list
# .remove() only removes the first value it finds
# .pop() to remove the last item in the list
# or we can give it an idex to remove that element
names.remove("Abyaz")
numbers.pop()
numbers.pop(0)

# list can contain value of different data types
random_list = ["Abyaz", 32, 18.0, True, None]

# delete item from list
del numbers[0]

# we can access multiple items together
numbers[0:3]

# we can also leave the first value if we want to start from the begining
numbers[:3]

# negative indexing is also available
numbers[-1]


# any() checks in the list if there is any true value
# all() checks all the value True or not
