import sys

arguments = sys.argv

# it cannot be empty it always takes the name of the first argument or file name
print(f"we received these arguments: {arguments}")

print(f"We are currently running on a {sys.platform} machine")
