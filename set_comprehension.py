import random
print({num * num for num in range(11)})

names = ["Abyaz", "Hasham", "Abyaz"]
print(set([len(name) for name in names]))


my_dict = {num: random.randint(0, 100) for num in range(0, 100)}
print(my_dict)
print(set(my_dict.values()))
print({num for num in my_dict.values()})
