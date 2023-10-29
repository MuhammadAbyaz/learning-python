# to define a set we want to explicity type set()
# {} they used to represent empty dictionary
# if we want to add item we can use {item} to define a set with one item

# it dont contain duplicates
names = {"Abyaz", "Hasham", "Abyaz"}

# it is fast for searching because it uses hash algorithms

# hash() can only apply on immutable types
# sets can contain only immutable type
print(hash("Abyaz"))

# we can convert a list/tuples of dulpicate values into a set to get unique items
print(set(names))

# sets have length and they are mutable
# there is no order in set
# there is not postioning in sets so we cant access value by index
random_set = {"Abyaz", 123, True, 56.8}

# adding and removing from a set
colors = {"Red", "Green", "Yellow", "Orange"}
colors.add("Indigo")

colors.discard("Green")
# it will give no error when the value to be removed is not present
colors.discard("White")

# we can also use remove method on sets to remove element it will give error when the value to be removed is not present
colors.remove("Red")

# combining a set .update(sequence) is used to do this
numbers = {1, 23, 45, 67, 8798}
colors.update(numbers)

# sets operations
# .union() or we can use '|' creates a new sets with combined element of both sets
even = {0, 2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9, 11}
integers = even.union(odd)

# .intersection() or we can use '&' creates a new sets with elements that are common in both the sets
whole_number = {0, 1, 2, 3, 4, 5, 6, 7, 8}
natural_number = {1, 2, 3, 4, 5, 6, 7, 8}
real_numbers = whole_number.intersection(natural_number)

# .difference() or we can use '^' creates a new set with elements that are in first set and not in second set

first_set = {1, 5, 6, 8}
second_set = {2, 5, 7, 9, 1}
difference = first_set.difference(second_set)

# there is a immutable type of set in python
my_set = frozenset(["Abyaz", "Hasham"])
# we cant add new values in it
# we can use .copy() to make a new copy of a set
new_set = my_set.copy()
