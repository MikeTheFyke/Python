print("")
print("_____Welcome To Python Tax Calculator_____")
print("")
subtotal = input("Please enter your subtotal : $")
tax = subtotal * .13
total = subtotal + tax
# '${:0,.2f}'.format(_____) converts and displays in a currency friendly format
print("Your Total tax equals      = " +  '${:0,.2f}'.format(tax))
print("Your Total with tax equals = " +  '${:0,.2f}'.format(total))
print("")
print("__________Okay Thank You__________")
print("")