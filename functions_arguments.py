def say_greeting(greeting, name):
    print(f"{greeting}, {name}")


# arguments with default value in a function always comes in last
def say_greeting(name, greeting="Hello"):
    print(f"{greeting}, {name}")


def create_query(language="JavaScript", num_stars=50, sort="desc"):
    return f"laguage: {language}, number of stars: {num_stars}, order: {sort}"


def foo(a, b=34):
    return a + b


# we can use named arguments so that we dont have to care about the order of thr arguments
print(foo(b=6, a=3))
print(foo(3, b=5))


# dont do this thing because the list is created only once the fucntion is called and the same list is called when the function is called again
def bar(a, b=[]):
    b.append(a)
    return b


print(bar(5))
print(bar(6))


# == checks the equality
# is it checks if they points to same thing in memory
