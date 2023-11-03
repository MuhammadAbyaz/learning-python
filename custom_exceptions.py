try:
    int("a")
    # if error occur on this line it will go to the except block without running next line code
    print("Thats a great number")

    # we can also pass tuple of errors
    # we can also give names to exception if we want to do something with the exception
    # we can also use multiple except clause but we have to catch sepecific exception first otherwise we will swallowed the specific exception
except ValueError:
    print("Thats not a number!")

# custom exception


class MyCustonException(Exception):
    pass


class IncorrectValueException(Exception):
    def __init__(self, value):
        message = f"Got a bad value: {value}"
        super().__init__(message)


raise MyCustonException()
