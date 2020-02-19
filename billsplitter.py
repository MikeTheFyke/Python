print("")
print("_____Welcome To Python Bill Plitter_____")
print("____________& Tip Calculator____________")
print("")
# input function displays message and receives an input after the enter button is entered
subtotal = input("Please enter your subtotal : $")
tip = input("Please enter a tip         : %")
numPeople = input("Please enter # of people   :  ")
print("")
tip = tip * .010
tax = subtotal * .13
total = subtotal + tax
tipTotal =  total * tip
# '${:0,.2f}'.format(_____) converts and displays in a currency friendly format
print("Your Tip total equals        = " + '${:0,.2f}'.format(tipTotal))
print("Your Total tax equals        = " +  '${:0,.2f}'.format(tax))
print("")
print("Your Total with tax equals   = " +  '${:0,.2f}'.format(total))
print("")
total = (total + tipTotal)
perPeople = (total / numPeople)
print("Your Total per Person equals = " +  '${:0,.2f}'.format(perPeople))
print("Your Total with tip equals   = " +  '${:0,.2f}'.format(total))
print("")
print("__________Okay Thank You__________")
print("")