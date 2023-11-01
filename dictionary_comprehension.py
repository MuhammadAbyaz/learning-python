import random
print({num: num * num for num in range(11)})

random_dict = {num: random.randint(0, 100) for num in range(0, 100)}
print(random_dict)
