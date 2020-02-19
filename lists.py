# An array of people
people = [
    "Ricky",
    "Julian",
    "Bubbles",
    "Mr.Lahey",
    "Randy",
]

# First Access Method
print("\n")
print(people[0])
print(people[2])
print(people[4])
print("\n")
print("Last Position Is " + str(people[-1]))

# Second Access Method
print("Julian is #" + str(people.index("Julian")))
print("\n")

# Third Access Method
print("The Top 3 are " + str(people[0:3]))
print("\n")
print("The Bottom 2 are " + str(people[-2:]))
print("\n")