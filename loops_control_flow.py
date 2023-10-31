colors = ["Red", "Orange", "Yellow", "Blue"]

# for loops
for color in colors:
    print(f"Your color is: {color}")
# the variable will be assigned with the last value and its not remain in scope only
print(color)

for num in range(5):
    print(num)

for num in range(1, 7, 2):
    print(num)

if 3 > 5:
    print("Hello")

# it also works on truthy value
abyaz = []
if abyaz:
    print("Hello")

if 3 > 5:
    print("Hello")
else:
    print("In else")

if 3 > 5:
    print("In if")
elif 3 < 5:
    print("In elif")
else:
    print("In else")


# while loops
counter = 0
max = 4
while counter != max:
    print(counter)
    counter = counter + 1

# Break
names = ["Hasham", "Khalid", "Abyaz"]

for name in names:
    if name == "Khalid":
        break
    else:
        print(name)

for name in names:
    if name != "Abyaz":
        continue
    else:
        print(f"Hello, {name}")
# In nested for loops if you break through inner loop outer loop will not break

count = 0
while True:
    if count == 5:
        break
    count += 1


# return statement

def find_target_name(names):
    for name in names:
        print(name)
        if name == "Abyaz":
            return "found the special case"
