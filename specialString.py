userString = raw_input("\nPlease enter a word of sentence for me to count :) \n")
print("\n")

for index, letter in enumerate(userString):
    print (letter + " is the " + str(index + 1) + " th letter of the String.")
   
length = str(len(userString))
print("\nYour Word or sentence is " + length + " characters long.")

# Vowel removal/replacment
vowels = 'aeiou'
unVoweled = str(userString)

for vowel in vowels:
    unVoweled = unVoweled.replace(vowel, '')

print ("\nHere is your submission without vowels : " + unVoweled + ".")


# Vowel Counter

vowelCtr =  len(userString) - len(unVoweled)
print ("\nYour submission had " + str(vowelCtr) + " vowels within it.\n")