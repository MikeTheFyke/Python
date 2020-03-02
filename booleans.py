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

print ( "TheBoys Boolean     : " + str(theBoysBoolean) + "\n")
print ( "OtherBoys Boolean   : " + str(otherBoysBoolean) + "\n")
print ( "ShortSpeech Boolean : " + str(speechBoolean) + "\n")
print ( "LongSpeech Boolean  : " + str(longSpeechBoolean) + "\n")