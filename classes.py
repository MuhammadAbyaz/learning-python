# we dont need a getter and setter to change the value
class Car:
    runs: bool = True
    number_of_wheels = 4

    def __init__(self, name: str) -> None:
        print("new car!")
        self.name = name
        print(f"Does run? {self.runs}")

    def __str__(self) -> str:
        return f"My car the {self.name} currently {self.runs}"

    def __repr__(self) -> str:
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"Car is broken")

# they are used in special cases
    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


# few instances method
# isinstance(value, class) returns True or False
# issubclass(str, object)

# str() returns a human readable form
# repr() returns what arguments we need to create a new instance
