# Programming Project Task - Jack Greenacre

def menu():
    """
    MAIN MENU FUNCTION
    """
    menuOption = raw_input("1. Enter RLE\n2. Display ASCII Art\n3. Convert to ASCII Art\n4. Convert to RLE\n5. Quit\n>>> ")
    print("")
    menuOption = str(menuOption)
    menuOption = menuOption.lower()
    if menuOption == "1" or menuOption == "1. enter rle" or menuOption == "enter rle":
        print("DEBUG RLE")
    elif menuOption == "2" or menuOption == "2. display ascii art" or menuOption == "display ascii art":
        print("DEBUG DISPLAY ASCII")
    elif menuOption == "3" or menuOption == "3. convert to ascii art" or menuOption == "convert to ascii art":
        print("DEBUG CONVERT ASCII ART")
    elif menuOption == "4" or menuOption == "4. convert to rle" or menuOption == "convert to rle":
        print("DEBUG CONVERT RLE")
    elif menuOption == "5" or menuOption == "5. quit" or menuOption == "quit" or menuOption == "exit":
        print("DEBUG EXIT")
    else:
        print("DEBUG ERROR")
        

#MAIN
print("Programming Project Task - Jack Greenacre\n")
menu()
