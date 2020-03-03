
usernameInput = raw_input("\nPlease enter your Username : ")
passwordInput = input("\nPlease enter you Password (8 Characters Please) : ")
passwordVerInput = input("\nPlease re-enter you Password (8 Characters Please) : ")
passwordLength = len(str(passwordInput))


if passwordInput == passwordVerInput and passwordLength >= 8:
    print ("\n Congratualtions" + usernameInput + "account created :) \n")
else:
    print ("\n Sorry passwords did not match :( \n")