rockosML = [
    "Rocko Rama",
    "Spunky",
    "Heffer Wolfe",
    "Ed BigHead",
    "Bev BigHead",
    "Filburt Turtle",
    "Earl The Dog",
    "Paula Hutchison"
]

print("\n--This is the start of the list--")
# Indenting in Python can define end points for for loops.
for name in rockosML:
    print name
print("---This is the end of the list---\n")

# Mass Uppercasing by using The Append method to save changed data into new Array
print("\nThe same list but all in CAPS\n")
upperNames = []
for name in rockosML:
    name = name.upper()
    upperNames.append(name)

print(upperNames)
print("\n ---The End Is Here--- \n")


# Directions Loop

print("\nLet's Get You Moving\n")

directions = [
    "turn left",
    "go straight",
    "turn right",
    "keep going until you see the dog statue",
    "turn right",
    "turn right again",
    "park right on the sidewalk"
]

instructions = "First "

for nextDirection in directions:
    instructions = instructions + nextDirection + ", then \n"

print(instructions + "\nYou Have Arrived :)\n")


# Bacteria Loop using the range method, 10 iterations in my example
# using time.sleep method to create a pause between iterations.
print("\nWelcome to The Bacteria Zone\n")

# imported time method
import time

bacteria = "&"
generations = 10

for generation in range(0, generations):
    # bacteria = bacteria + bacteria - replaced to show strings can be mulitplied
    bacteria = bacteria * 2
    print(bacteria)
    time.sleep(0.5)

print("\nThank You Come Again\n")