userString = raw_input("\nPlease enter a word of sentence for me to count :) \n")

for index, letter in enumerate(userString):
    print (letter + " is the " + str(index + 1) + " th letter of the String.")
   
length = str(len(userString))
print("Your Word of sentence is " + length + " characters long.")