# Programming Project Task - Jack Greenacre
# ~ Python 2.7 ~

def menu():
    """
    MAIN MENU FUNCTION
    """
    menuOption = raw_input("1. Enter RLE\n2. Display ASCII Art\n3. Convert to ASCII Art\n4. Convert to RLE\n5. Quit\n>>> ") # ASK FOT INPUT
    print("")
    menuOption = str(menuOption) # CONVERT TO STRING
    menuOption = menuOption.lower() # CONVERT TO LOWER CASE
    if menuOption == "1" or menuOption == "1. enter rle" or menuOption == "enter rle": # IF THE FIRST OPTION WAS PICKED
        rleMenu() # START RLEMENU
    elif menuOption == "2" or menuOption == "2. display ascii art" or menuOption == "display ascii art": # IF THE SECOND OPTION WAS PICKED
        displayArtMain() # START DISPLAYARTMAIN
    elif menuOption == "3" or menuOption == "3. convert to ascii art" or menuOption == "convert to ascii art": # IF THE THRID OPTION WAS PICKED
        convertArtMain() # START CONVERTARTMAIN
    elif menuOption == "4" or menuOption == "4. convert to rle" or menuOption == "convert to rle": # IF THE FOURTH OPTION WAS PICKED
        convertRleMain() # START CONVERTRLEMAIN
    elif menuOption == "5" or menuOption == "5. quit" or menuOption == "quit" or menuOption == "exit": # IF THE FITH OPTION WAS PICKED
        print("Thank you for using!") # DISPLAY EXIT MESSAGE
        quit() # QUIT
    else:
        print("Error: Input could not be recognised.\nPlease try a recognised option - e.g. `1` or `Enter RLE`\n") # IF INPUT WAS NOT VALID DISPLAY ERROR MESSAGE
        menu() # START MENU

def rleMenu():
    """
    ENTER COMPRESSED DATA TO DECOMPRESS
    """
    needToBreak = True
    rleLinesTrue = False
    while not rleLinesTrue:
        needToBreak = True
        rleLinesTrue = False
        try:
            rleLines = input("How many lines of RLE compressed data would you like to enter?\n>>> ")
        except KeyboardInterrupt:
            print("\nError: There was a keyboard interrupt!\nThank you for using!\n")
            quit()
        except:
            print("\nError: Sorry, that is not a valid number.\nPlease try again with a recognised option - e.g. `2` or `6`\n")
            needToBreak = False
        finally:
            if needToBreak:
                rleLinesTrue = True
                break
    if str(type(rleLines)) != "<type 'int'>":
        print("\nError: Sorry, that is not a valid number.\nPlease try again with a recognised option - e.g. `2` or `6`\n")
        rleMenu()
    else:
        pass
    if rleLines <= 2:
        print("\nError: Sorry, that is not long enough.\nPlease try again with a value greater than `2`\n")
        rleMenu()
    else:
        pass
    for i in range(1,rleLines+1):
        globals()["rleLine" +str(i)] = str(raw_input("\nPlease input a line of RLE encoded data.\n>>> "))
    print("\nYou have entered:")
    for i in range(1,rleLines+1):
        print(globals()["rleLine" +str(i)])
    menuOption = raw_input("\nIs this correct? [Y/N]\n>>> ")
    menuOption = str(menuOption)
    menuOption = menuOption.lower()
    while True:
        if menuOption == "y":
            break
        elif menuOption == "n":
            print("")
            rleMenu()
        else:
            print("\nError: That was not understood.\nPlease try again with a recognised option - e.g. `y` or `n`\n")
    print("")
    for i in range(1,rleLines+1):
        rleDecode(globals()["rleLine" +str(i)])
    print("")
    menu()

def rleDecode(stringToDecode):
    """
    DECOMPRESS RLE DATA FROM RLEMENU
    """
    listToDecode = list(stringToDecode)
    count = ''
    char = ''
    current = 0
    for item in listToDecode:
        if current < 2:
            count += item
            current = current+1
        else:
            times = int(count)
            for i in range(times):
                char += item
            count = ''
            current = 0
    print(char)

def displayArtMain():
    """
    ENTER DATA AND DISPLAY AS ASCII ART
    """
    fileToDisplay = raw_input("What is the name of the file you would like to display?\n>>> ")
    try:
        f = open(fileToDisplay, "r")
    except IOError:
        print("\nError: That file does not exist.\nPlease try again with another file - e.g. `ASCIIArt.txt`\n")
        menu()
    if f.mode == 'r':
        contents = f.read()
        print("")
        print(contents)
        print("")
    menu()

def convertArtMain():
    """
    ENTER COMPRESSED FILE AND CONVERT TO ASCII ART
    """
    fileToConvert = raw_input("What is the name of the file you would like to convert?\n>>> ")
    try:
        f = open(fileToConvert, "r")
    except IOError:
        print("\nError: That file does not exist.\nPlease try again with another file - e.g. `ASCIIArtRle.txt`\n")
        menu()
    f1 = f.readlines()
    print("")
    try:
        for x in f1:
            rleDecode(x)
    except ValueError:
        print("Error: That is not an RLE encoded file.\nPlease try again with an RLE encoded file.\n")
        menu()
    print("")
    menu()

def convertRleMain():
    """
    ENTER DATA TO COMPRESS TO RLE
    """
    print("\nDEBUG: OPTION 4 COMING SOON\n")
    menu()

#MAIN
print("Programming Project Task - Jack Greenacre\n")
try:
    menu()
except KeyboardInterrupt:
    print("Thank you for using!")
    quit()
except:
    print("Fatal Error: An unknown error occurred!\nExiting...\nThank you for using!")
    quit()
