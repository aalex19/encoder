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


def password_decoder(new_password):
    old_password = ''
    for i in new_password:
        old_char = str((int(i)-3) % 10)
        old_password += old_char
    return old_password


while True:
    menu()
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded_password = encode(password)
        print("Your password has been encoded and stored!")

    if option == 2:
        decoded_password = password_decoder(str(encoded_password))
    print(f"The encoded password is {encoded_password}, and the original password is {password}.")
    program_on = True

    if option == 3:               #quit program
        quit()
