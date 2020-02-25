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

ctr = 0

for name in agents:
    print (ctr), (name)
    ctr = ctr + 1

extensionNumber = input("\n Please Enter An Agents extension Number   : ")
print("---------------------------------------\n")
print(agents[extensionNumber] + " -- " +roles[extensionNumber])
print("\n---------------------------------------\n")