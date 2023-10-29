def upper_case_name(name):
    return name.upper()


# it will also print the print statements that is written in name_lib
name = "Abyaz"
name_upper = upper_case_name(name)
print(name_upper)

# to avoid this we will use main method
# __<function_name>__ are called dunders

# now this code will not run when we import something from this file
if __name__ == "__main__":
    name = "Abyaz"
    name_upper = upper_case_name(name)
    print(name_upper)
