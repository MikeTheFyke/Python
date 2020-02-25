agents = [
    "0 - Operator",
    "1 - Malory Archer",
    "2 - Sterling Archer",
    "3 - Lawna Kane",
    "4 - Cyril Figgis",
    "5 - Ray Gillette",
    "6 - Pam Poovey",
    "7 - Dr. Krieger",
    "8 - Barry Dillon"
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
    print (ctr)
    print name
    ctr = ctr + 1

extensionNumber = input("\n Please Enter An Agents extension Number   : ")
print("---------------------------------------\n")
print(agents[extensionNumber] + " -- " +roles[extensionNumber])
print("\n---------------------------------------\n")