import random
number_dict = {num: num * num for num in range(11)}
print(number_dict.items())


players = ["Rooney", "Henry", "Zidane", "Ronaldinho"]
goals = [20, 45, 37, 43]


for item in zip(players, goals):
    print(item)


for name, score in zip(players, goals):
    print(f"Name: {name} and Score: {score}")

# we can pass zip function in other data structures like generators
my_list = list(zip(players, goals))
print(my_list)


# the number of items in both list must be same otherwise min length of list is obtained
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list(zip(list1, list2)))

# we can also pass zip function in a dictionary to get the dictionary
print(dict(zip(players, goals)))


# Exercise

name_list = ["Abyaz", "Hasham", "Khalid"]
score_list = [random.randint(0, 100) for name in name_list]


for name, score in zip(name_list, score_list):
    print(f"{name} got {score} score")

# once the zip is used it becomes empty
# they are of one time use
