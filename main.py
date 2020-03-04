# Programming Project Task - Jack Greenacre

def menu():
    """
    MAIN MENU FUNCTION
    """
    menuOption = raw_input("1. Enter RLE\n2. Display ASCII Art\n3. Convert to ASCII Art\n4. Convert to RLE\n5. Quit\n>>> ")
    print("")
    inputType = 0
    #Check input
    if menuOption.islower():
        inputType = 1
        print("DEBUG: 1")
    elif menuOption.isupper():
        inputType = 2
        print("DEBUG: 2")
    else:
        inputType = 3
        print("DEBUG: 3")
    #Convert to lower-case string
    if inputType == 1:
        menuOption.lower()
    elif inputType == 2:
        menuOption.lower()
        inputType = 1
    elif inputType == 3:
        try:
            menuOption = str(int(menuOption))
        except ValueError:
            print("Error: Unable to detect type of input.\nPlease try again\n")
            menu()
    else:
        print("Error: Unable to detect type of input.\nPlease try again\n")
        menu()
        

#MAIN
print("Programming Project Task - Jack Greenacre\n")
menu()
