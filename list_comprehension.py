names = ["Abyaz", "Hasham", "Khalid"]

upper_name = []

# This is common way of doing loop to make new list
# for name in names:
#     upper_name.append(name.upper())


# Handy shortcut
print([name.upper() for name in names])

# list of numbers using list comprehension
print([num * num for num in range(6)])


# list of tuples
print([("length:", len(name)) for name in names])

# Example
print(",".join([f"Name is: {name}"for name in names]))

# One more Example for printing square of number that are even
print([num * num for num in range(11) if num % 2 == 0])

# printing csv of values of square of even number
even_number = [num * num for num in range(11) if num % 2 == 0]
print(",\n".join([f"Number is: {num}"for num in even_number]))

# list operations
# sum of all values in a list
sum(even_number)

# min of all value in a list it takes the list of integer
min(even_number)

# max of all value in a list it takes the list of integer
max(even_number)

lottery_numbers_string = "4, 5, 134, 20"

lottery_list = lottery_numbers_string.split(", ")

print(max([int(num) for num in lottery_list]))
