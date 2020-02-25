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


# Bacteria Loop using the range method
print("\nWelcome to The Bacteria Zone\n")

bacteria = "&"

for generation in range(0, 20):
    bacteria = bacteria + bacteria

print(bacteria)
print("\nThank You Come Again\n")