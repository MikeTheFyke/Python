username = "Joe"
password = 1234

usernameInput = raw_input("\nPlease enter your Username : ")
passwordInput = input("\nPlease enter your Password : ")

if password == passwordInput and username == usernameInput:
    print ("\n That is the correct password :) \n")
else:
    print ("\n Sorry wrong password :( )\n")