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

# Append method
people.append("Crazy Dan")
print(people[-1])
print("Your New List\n" + str(people)+"\n")

# Insert method - Keeping the above Append in last place just for fun.
people.insert(-1,"Scary Terry")
print("Your New New List\n" + str(people)+"\n")

# Change a value in a list
people[-1] = "Squirelly Dan"
print("Your New New New List\n" + str(people)+"\n")

# Delete an Item
del people[4]
print("What happened to Randy?\n" + str(people)+"\n")

# Concatenate Two List Together
peopleNew = [
    "Barrada",
    "Nikto",
    "Kalaatu"
]

newList = people + peopleNew
print("Two Lists Become One  \n" + str(newList)+"\n")