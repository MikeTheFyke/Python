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