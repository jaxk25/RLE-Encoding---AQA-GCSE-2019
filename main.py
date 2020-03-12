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
        rleMain() # START RLEMAIN
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

def rleMain():
    """
    ENTER COMPRESSED DATA TO UNCOMPRESS
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
        rleMain()
    else:
        pass
    if rleLines <= 2:
        print("\nError: Sorry, that is not long enough.\nPlease try again with a value greater than `2`\n")
        rleMain()
    else:
        pass
    for i in range(1,rleLines+1):
        globals()["rleLine" +str(i)] = str(raw_input("\nPlease input a line of RLE encoded data.\n>>> "))
    print("\nYou have entered:")
    for i in range(1,rleLines+1):
        print(globals()["rleLine" +str(i)])

def displayArtMain():
    """
    ENTER DATA AND DISPLAY AS ASCII ART
    """
    print("DEBUG: OPTION 2 COMING SOON")
    menu()

def convertArtMain():
    """
    ENTER COMPRESSED DATA AND CONVERT TO ASCII ART
    """
    print("DEBUG: OPTION 3 COMING SOON")
    menu()

def convertRleMain():
    """
    ENTER DATA TO COMPRESS TO RLE
    """
    print("DEBUG: OPTION 4 COMING SOON")
    menu()

#MAIN
print("Programming Project Task - Jack Greenacre\n")
try:
    menu()
except KeyboardInterrupt:
    print("Thank you for using!")
    quit()
