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
print("The Middle Man Of The Screaming Evils " + str(screamingEvils[middlePlayer - 1]))

# Display 2 above and 2 below the middle player
# Above
print("2 Above : " + str(screamingEvils[middlePlayer - 3: middlePlayer - 1]))
# Below 
print("2 Below" + str(screamingEvils[middlePlayer: middlePlayer + 2]))