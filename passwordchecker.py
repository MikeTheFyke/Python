username = "Joe"
password = 1234

usernameInput = raw_input("\nPlease enter you Username : ")
passwordInput = input("\nPlease enter you Password : ")

if password == passwordInput and username == usernameInput:
    print ("\n That is the correct password :) \n")
else:
    print ("\n Sorry wrong password :( )\n")