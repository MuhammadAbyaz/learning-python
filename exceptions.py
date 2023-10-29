try:
    int("a")
except ValueError:
    print("Oops you cant do that")

print("End of first try-except")


try:
    int("Hello")
    # we can also catch exceptions in a variable
except ValueError as e:
    print(e)

print("End of second try-except")
