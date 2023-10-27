# Helper functions
type(4)
# to show all the methods available
dir(int)
# prints the documentations
help(int.real)

print(type(42))
print(type(int('7')))
print(type(3/4))
print(type("Abyaz"))


# amount of rent program
rent = 479
# // converts the float value to an integer
per_day = rent // 12
print(per_day)

# String formatting
# 1 str.format()
name = "Abyaz"
print("Hello my name is %s" % name)
# 2 f strings
print(f"Hello my name is {name}")
# 3 with ,
print("Hello my name is", name)
