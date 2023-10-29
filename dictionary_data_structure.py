# stores data in key value pairs
# perfect for working with json data
# dictionary are themselves mutable but the keys are immutable
# keys under the hood uses hash function

# only immutable data types can be used as a key
# keys are in insertion order but we cant access them by index
# values in dictionary can be of different data tyoe
number_dictionary = {"one": 1, "two": 2, "three": 3}

# accessing the values
print(number_dictionary["one"])

# we can return a default value if the key is not present
print(number_dictionary.get("four", "default value"))
# to access the value we can aslo use it will not give error if the key is not present
print(number_dictionary.get("one"))
# .discard() to remove if it is present and will not give error if it is not present

# we can add new key and value in dictionary as follows
# it will override if you assign new value to the key
number_dictionary["four"] = 4

# we can use 'in' operator to check if certain key is present or not
"five" in number_dictionary

# combining two dictionaries
rainbow = {"r": "Red", "g": "Green", "v": "Violet"}
colors = {"i": "indigo", "b": "Blue"}
rainbow.update(colors)

# mutable data types can be used as a values in dictionaries

vegetables = {"Green": ["Spinach", "Corriander"],
              "Red": ["Tomato", "Red chilli"]}

vegetables["Green"].append("Mint")


# to access all the keys we use keys() method
print(vegetables.keys())
# to access all the values we use values() method
print(vegetables.values())
# to access both key-value pair we use items() method
print(type(vegetables.items()))
