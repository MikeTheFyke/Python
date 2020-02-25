agents = [
    "Operator",
    "Malory Archer",
    "Sterling Archer",
    "Lawna Kane",
    "Cyril Figgis",
    "Ray Gillette",
    "Pam Poovey",
    "Dr. Krieger",
    "Barry Dillon"
]

roles = [
    "Cheryl Tunt - Your Not My Supervisor",
    "Agency Head",
    "Agent In Command - He Said Commandingly",
    "Agent In Command - She Said Commandingly",
    "Sub Agent - Suppressing Fire",
    "Sub Agent - Half Freaking Robot",
    "Sub Agent - Strong/Big As An Ox",
    "Scientist - Might Be A Clone Of Adolf Hitler",
    "Target Practice - World Record Ricochette"
]

print ("\n--- Welcome To The Figgis Agency ---" + "\n---    List Of Active Agents     ---\n")

# Created Counter Variable to access the above lists
ctr = 0

for name in agents:
    print (ctr), (name)
    ctr = ctr + 1

# input method instead of raw_input for the integer to be used for index
extensionNumber = input("\n Please Enter An Agents extension Number   : ")
print("---------------------------------------\n")
print(agents[extensionNumber] + " -- " +roles[extensionNumber])
print("\n---------------------------------------\n")

## Other Methods

# DISPLAY List Using the range method 
print("\n----------RangeMethod------------------\n")
for index in range(0, len(agents)):
    print(agents[index])
    print(roles[index])

# DISPLAY List Using the enumerate method 
print("\n----------EnumerateMethod--------------\n")
for index, agent in enumerate(agents):
    print(agents)
    print(roles[index])

# Display Using Refacturing

agentsRoles = [
    ["Operator","Cheryl Tunt - Your Not My Supervisor"],
    ["Malory Archer", "Agency Head"],
    ["Sterling Archer", "Agent In Command - He Said Commandingly"],
    ["Lawna Kane", "Agent In Command - She Said Commandingly"],
    ["Cyril Figgis", "Sub Agent - Suppressing Fire"],
    ["Ray Gillette", "Sub Agent - Half Freaking Robot"],
    ["Pam Poovey", "Sub Agent - Strong/Big As An Ox"],
    ["Dr. Krieger", "Scientist - Might Be A Clone Of Adolf Hitler"],
    ["Barry Dillon", "Target Practice - World Record Ricochette"]
]


print ("\nRefactured List AGENTS/ROLES\n")
for agentRole in agentsRoles:
    agent01 = agentRole[0]
    role01 = agentRole[1]
    print(agent01 + " - " + role01)

print("\n")