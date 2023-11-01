my_string = "Hello, World!"

print(my_string[0])
print(my_string[-1])
print(my_string[:5])
print(my_string[-10:-4])

names = ["Abyaz", "Hasham", "Khalid", "Abyaz"]

print(names[0])
print(names[-1])
print(names[:3])
print(names[2:])

# copy of a list

new_names = names[:]
new_names.append("Ahmed")
print(new_names)
print(names)


# first and second arguments are range and third is step
number_list = list(range(10))
print(number_list[1:7:2])
reversed_list = number_list[::-1]
print(reversed_list)
# we can do slicing only on ordered data structure


# Exercise
list_of_numbers = list(range(0, 100))
print(list_of_numbers[30:70])

# returned a copy of list in reverse order
print(list_of_numbers[::-1])

# it will return list sorted in reverse in place
print(list_of_numbers.reverse())
