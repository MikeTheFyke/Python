screamingEvils = [
    "Bones Jackson",
    "Madman",
    "Madboy",
    "KT Slayer",
    "Malicious Malone",
    "Slick Toxin",
    "Spewter",
    "Mo"
]

Derangers = [
    "Razor Kidd",
    "Darkstar",
    "Thrasher",
    "Cannonball",
    "Jackie LaGrunge",
    "Joe Magician",
    "Grim McSlam",
    "Liquid Lazer"
]

# Find the middle player
middlePlayer = ((len(screamingEvils)) / 2)
print("\nThe Middle Man Of The Screaming Evils " + str(screamingEvils[middlePlayer - 1]))

# Display 2 above and 2 below the middle player
# Above
print("2 Above : " + str(screamingEvils[middlePlayer - 3: middlePlayer - 1]))
# Below 
print("2 Below" + str(screamingEvils[middlePlayer: middlePlayer + 2]))

# Inserting An Average Player To Represent the middle player on the team
screamingEvils.insert(middlePlayer,"Average Johnson")
print("Your New Screaming Evils \n" + str(screamingEvils) + "\n")

# Replace Average Player To AVERAGE PLAYER
screamingEvils[middlePlayer] = "AVERAGE PLAYER"
print("Your New New Screaming Evils \n" + str(screamingEvils) + "\n")

# Consolidate Teams
ScreamingDerangers = screamingEvils + Derangers
print("Your New Screaming Derangers \n" + str(ScreamingDerangers) + "\n")

# del and re adjust Average Player
del ScreamingDerangers[middlePlayer]
ScreamingDerangers.insert( (len(ScreamingDerangers)/2), "New Average Johnson")
print("Your New Screaming Derangers - New Middle Player \n" + str(ScreamingDerangers) + "\n")