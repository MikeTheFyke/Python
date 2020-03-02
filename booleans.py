# This will equate to true
theBoys = ['Wayne','Squirrelly Dan','Daryl','Katy']
theBoysBoolean = bool(theBoys)

# This will equate to False
theOtherBoys = []
otherBoysBoolean = bool(theOtherBoys)


# This will equate to true
shortSpeech = ("\nYou knew your pal had come into money when he started throwing out \nperfectly good pistachios like he was above cracking em open with a\nbox cutter like the rest of us\n")
print(shortSpeech)
speechBoolean = bool(shortSpeech)

# This will equate to false
longSpeech = ''
longSpeechBoolean = bool(longSpeech)

# This will equate to true
numberOfHijinx = 32456
numberHijinxBoolean = bool(numberOfHijinx)


# This will equate to false
numberOfYimYam = 0
yimYamBoolean = bool(numberOfYimYam)

# This will equate to true
truther = True
trutherBoolean = bool(truther)

# This will equate to false
denier = False
denierBoolean = bool(denier)

# This will equate to true
roomHeight = 10
myHeight = 6
extraHeightBoolean = bool(roomHeight > myHeight)

# This will equate to false
giraffeHeight = 21
giraffeHeightBoolean = bool(roomHeight > giraffeHeight)

# This will equate to false
boysSearchBoolean = bool('John' in theBoys)

print ( "TheBoys Boolean        : " + str(theBoysBoolean) + "\n")
print ( "OtherBoys Boolean      : " + str(otherBoysBoolean) + "\n")
print ( "ShortSpeech Boolean    : " + str(speechBoolean) + "\n")
print ( "LongSpeech Boolean     : " + str(longSpeechBoolean) + "\n")
print ( "HijinxNumber Boolean   : " + str(numberHijinxBoolean) + "\n")
print ( "YimYamNumber Boolean   : " + str(yimYamBoolean) + "\n")
print ( "Truther Boolean        : " + str(trutherBoolean) + "\n")
print ( "Denier Boolean         : " + str(denierBoolean) + "\n")
print ( "Extra Height Boolean   : " + str(extraHeightBoolean) + "\n")
print ( "Giraffe Height Boolean : " + str(giraffeHeightBoolean) + "\n")
print ( "TheBoys Search Boolean : " + str(boysSearchBoolean) + "\n")