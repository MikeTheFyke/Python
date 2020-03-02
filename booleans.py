# This will equate to true determining this is a populated list
theBoys = ['Wayne','Squirrelly Dan','Daryl','Katy']
theBoysBoolean = bool(theBoys)

# This will equate to False determining this is not a populated list
theOtherBoys = []
otherBoysBoolean = bool(theOtherBoys)


# This will equate to true determining this is a populated string
shortSpeech = ("\nYou knew your pal had come into money when he started throwing out \nperfectly good pistachios like he was above cracking em open with a\nbox cutter like the rest of us\n")
print(shortSpeech)
speechBoolean = bool(shortSpeech)

# This will equate to false determining this is not a populated string
longSpeech = ''
longSpeechBoolean = bool(longSpeech)

# This will equate to true determining if a value is a true number
numberOfHijinx = 32456
numberHijinxBoolean = bool(numberOfHijinx)

# This will equate to false determining if a value is a true number
numberOfYimYam = 0
yimYamBoolean = bool(numberOfYimYam)

# This will equate to true determining if a value is a true number
numberOfZip = -500
zipBoolean = bool(numberOfZip)

# This will equate to true using boolean identifiers
truther = True
trutherBoolean = bool(truther)

# This will equate to false using boolean identifiers
denier = False
denierBoolean = bool(denier)

# This will equate to true using comparisons
roomHeight = 10
myHeight = 6
extraHeightBoolean = bool(roomHeight > myHeight)

# This will equate to false using comparisons
giraffeHeight = 21
giraffeHeightBoolean = bool(roomHeight > giraffeHeight)

# This will equate to false using the 'in' operator
boysSearchBoolean = bool('John' in theBoys)

# This will equate to false using the 'is' operator
bestBoy = theBoys[0]
bestBoyBoolean = bool('john' is bestBoy)

# This Will equate to True the weather using the 'and' operator
outsideTemperature = 28
sunny = True
cloudy = False
idealWeatherBoolean = bool(outsideTemperature > 25 and sunny)
# This Will equate to False the weather using the 'and' operator
notIdealWeatherBoolean = bool(outsideTemperature < 25 and cloudy)

# using the 'or' operator
hasCoffee = True
hasBeer = True
drinkBoolean = bool(hasCoffee or hasBeer)


print ( "TheBoys Boolean               : " + str(theBoysBoolean) + "\n")
print ( "OtherBoys Boolean             : " + str(otherBoysBoolean) + "\n")
print ( "ShortSpeech Boolean           : " + str(speechBoolean) + "\n")
print ( "LongSpeech Boolean            : " + str(longSpeechBoolean) + "\n")
print ( "HijinxNumber Boolean          : " + str(numberHijinxBoolean) + "\n")
print ( "YimYamNumber Boolean          : " + str(yimYamBoolean) + "\n")
print ( "-Zip Number Boolean           : " + str(zipBoolean) + "\n")
print ( "Truther Boolean               : " + str(trutherBoolean) + "\n")
print ( "Denier Boolean                : " + str(denierBoolean) + "\n")
print ( "Extra > Height Boolean        : " + str(extraHeightBoolean) + "\n")
print ( "Giraffe > Height Boolean      : " + str(giraffeHeightBoolean) + "\n")
print ( "TheBoys IN Search Boolean     : " + str(boysSearchBoolean) + "\n")
print ( "TheBoys IS BestBoy Boolean    : " + str(bestBoyBoolean) + "\n")
print ( "Ideal AND Weather Boolean     : " + str(idealWeatherBoolean) + "\n")
print ( "Not Ideal AND Weather Boolean : " + str(notIdealWeatherBoolean) + "\n")
print ( "Beer OR Coffee Boolean        : " + str(drinkBoolean) + "\n")