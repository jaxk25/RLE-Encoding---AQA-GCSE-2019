# Programming Project Task - Jack Greenacre
# ~ Python 2.7 ~

def menu():
    """
    MAIN MENU FUNCTION
    """
    menuOption = raw_input("1. Enter RLE\n2. Display ASCII Art\n3. Convert to ASCII Art\n4. Convert to RLE\n5. Quit\n>>> ")
    print("")
    menuOption = str(menuOption)
    menuOption = menuOption.lower()
    if menuOption == "1" or menuOption == "1. enter rle" or menuOption == "enter rle":
        rle()
    elif menuOption == "2" or menuOption == "2. display ascii art" or menuOption == "display ascii art":
        displayArt()
    elif menuOption == "3" or menuOption == "3. convert to ascii art" or menuOption == "convert to ascii art":
        convertArt()
    elif menuOption == "4" or menuOption == "4. convert to rle" or menuOption == "convert to rle":
        convertRle()
    elif menuOption == "5" or menuOption == "5. quit" or menuOption == "quit" or menuOption == "exit":
        print("Thank you for using!")
        quit()
    else:
        print("Error: Input could not be recognised.\nPlease try a recognised option - e.g. `1` or `Enter RLE`\n")
        menu()


def rle():
    """
    ENTER COMPRESSED DATA TO UNCOMPRESS
    """
    print("DEBUG: OPTION 1 COMING SOON")

def displayArt():
    """
    ENTER DATA AND DISPLAY AS ASCII ART
    """
    print("DEBUG: OPTION 2 COMING SOON")

def convertArt():
    """
    ENTER COMPRESSED DATA AND CONVERT TO ASCII ART
    """
    print("DEBUG: OPTION 3 COMING SOON")

def convertRle():
    """
    ENTER DATA TO COMPRESS TO RLE
    """
    print("DEBUG: OPTION 4 COMING SOON")

#MAIN
print("Programming Project Task - Jack Greenacre\n")
menu()
