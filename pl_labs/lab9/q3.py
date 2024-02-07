user_input = input("Enter your favourite dishes: ").split(" ")
dishes = set(user_input)

while len(dishes) > 0:
    print(dishes.pop())
