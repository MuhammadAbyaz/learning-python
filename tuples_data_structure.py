# tuples
# they are immutable
# parenthesis are not necessary we can just use commas
a = ()

# for one item tuple we have to add a trailing comma
c = (1,)

# Example
student = ("Abyaz", 8, "History", 3.5)

# tuples unpacking
# number of variables must be equal to the number of item in tuple
# if we dont want to save certain value we can use underscore
name, age, subject, gpa = student

# Example of returning tuple from a function


def http_status_code():
    return 200, "OK"


print(http_status_code())

# for checking element we can use
# .index(item) or we can use 'in' keyword
