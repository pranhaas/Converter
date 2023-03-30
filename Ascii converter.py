def menu():
    choice = int(input("""Please select the corrisponding number. Please note that the program will not work if you do not select a number.
    1 - Convert to Ascii
    2 - Convert to binary
    3 - Convert to Hexadecimal
    4 - convert to decimal
    5 - exit
    """))
    if choice == 1:
        ascii()
    elif choice == 2:
        binary()
    elif choice == 3:
        hexadecimal()
    elif choice == 4:
        decimal()
    elif choice == 5:
        exit()
    else:
        print("❌ Please select a number between 1 and 6")
        menu()
def ascii():
    choice = int(input("""Please select the corrisponding number. Please note that the program will not work if you do not select a number.
    1 - Convert from text to ascii
    2 - Convert from ascii to text
    """))
    if choice == 1:
        print("Welcome to my ascii converter!!")
        text = input("Please enter the text you want to convert to ascii\n")
        asciList = []
        for i in text:
            a = ord(i)
            asciList.append(a)
            print(a)
        print(f"The total list is {asciList} for the word {text}")
    elif choice == 2:
        print("Please enter the ascii code you want to convert to text. Please only enter one number at a time as the programe is going to itterate back.")
        ammount = int(input("Please enter how many numbers you want to convert to text\n"))
        asciiList = []
        for i in range (ammount):
            asciiNum = int(input("Please enter the ascii number."))
            b = chr(asciiNum)
            asciiList.append(b)
            print(b)
        print(asciiList)
    print("The function you requested is now complete. Returning you back to the menu.")
    menu()

menu()