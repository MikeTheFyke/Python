
usernameInput = raw_input("\nPlease enter your Username : ")
passwordInput = input("\nPlease enter you Password : ")
passwordVerInput = input("\nPlease re-enter you Password : ")


if passwordInput == passwordVerInput and username == usernameInput:
    print ("\n Congratualtions account created :) \n")
else:
    print ("\n Sorry passwords did not match :( )\n")