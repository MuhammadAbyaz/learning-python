names = ["Abyaz", "Hasham", "Khalid", "Abyaz"]

# these are called generator expression
# in generator the value is generated when we loop over it
print(type(len(name) for name in names))
names_length_set = set(len(name) for name in names)


my_gen = (num * num for num in range(6))
# we cant access value by index we have to loop over it to get the value
for num in my_gen:
    print(num)
