#Aleena Alex

def menu():              #prints menu
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit" )

def encode(password):         #encodes user input by adding 3 to each value of password
    encode = ""
    for pas in password:
        pas = int(pas) + 3
        encode += str(pas)
    return encode

while True:
    menu()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")

    #if option == 2:

    if option == 3:               #quit program
        quit()
