print("")
print("_____Welcome To Python Bill Plitter_____")
print("____________& Tip Calculator____________")
print("")
subtotal = input("Please enter your subtotal : $")
tip = input("Please enter a tip      : %")
tip = tip * .010
numPeople = input("Please enter # of people  :  ")
tax = subtotal * .13
total = subtotal + tax
tipTotal =  total * tip
print("Your Tip total equals      = " + '${:0,.2f}'.format(tipTotal))
print("Your Total tax equals      = " +  '${:0,.2f}'.format(tax))
print("Your Total with tax equals = " +  '${:0,.2f}'.format(total))
print("")
print("__________Okay Thank You__________")
print("")