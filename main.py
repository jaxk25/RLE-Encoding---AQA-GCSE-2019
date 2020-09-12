# AQA GCSE NEA 2019-2020 - Jack Greenacre
# ~ Python 2.7 ~

def menu(): # Function for the main menu
    """
    MAIN MENU FUNCTION
    """
    menuOption = raw_input("1. Enter RLE\n2. Display ASCII Art\n3. Convert to ASCII Art\n4. Convert to RLE\n5. Quit\n>>> ") # Ask for user input
    print("")
    menuOption = str(menuOption) # Convert to string
    menuOption = menuOption.lower() # Convert to lower case
    if menuOption == "1" or menuOption == "1. enter rle" or menuOption == "enter rle": # If the first option was picked,
        rleMenu() # Call the rleMenu function
    elif menuOption == "2" or menuOption == "2. display ascii art" or menuOption == "display ascii art": # If the second option was picked,
        displayArtMain() # Call the displayArtMain function
    elif menuOption == "3" or menuOption == "3. convert to ascii art" or menuOption == "convert to ascii art": # If the third option was picked,
        convertArtMain() # Call the convertArtMain function
    elif menuOption == "4" or menuOption == "4. convert to rle" or menuOption == "convert to rle": # If the fourth option was picked,
        convertRleMain() # Call the convertRleMain function
    elif menuOption == "5" or menuOption == "5. quit" or menuOption == "quit" or menuOption == "exit": # If the fifth option was picked,
        print("Thank you for using!") # Display an exit message
        quit() # Quit the program
    else: # If other option was picked,
        print("Error: Input could not be recognised.\nPlease try a recognised option - e.g. `1` or `Enter RLE`\n") # Give an error
        menu() # Call the menu function to allow user to pick again

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
    if ".encoded.txt" in fileToConvert:
        try:
            for x in f1:
                rleDecodeFromPy(x)
        except ValueError:
            print("Error: That is not an RLE encoded file.\nPlease try again with an RLE encoded file.\n")
            menu()
        print("")
    else:
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
    fileToConvert = raw_input("What is the name of the file you would like to convert?\n>>> ")
    try:
        f = open(fileToConvert, "r")
    except IOError:
        print("\nError: That file does not exist.\nPlease try again with another file - e.g. `ASCIIArtRle.txt`\n")
        menu()
    f1 = f.readlines()
    print("")
    numberOfLines = 0
    for x in f1:
        globals()["encoded" +str(numberOfLines)] = rleEncode(x)
        numberOfLines = numberOfLines+1
    f.close()
    fileToWrite = fileToConvert +".encoded.txt"
    try:
        f = open(fileToWrite, "w+")
    except IOError:
        print("\nError: Unable to open file.\nPlease try again\n")
        menu()
    for i in range(1,numberOfLines+1):
        f.write(globals()["encoded" +str(i-1)])
    f.close()
    print("The new file is: " +fileToWrite +"\n")
    try:
        f = open(fileToConvert, "r")
    except IOError:
        print("\nError: Unable to open file.\nPlease try again\n")
        menu()
    if f.mode == "r":
        contents = f.read()
    lenOfFirst = len(contents)
    f.close()
    try:
        f = open(fileToWrite, "r")
    except IOError:
        print("\nError: Unable to open file.\nPlease try again\n")
        menu()
    if f.mode == "r":
        contents = f.read()
    lenOfSecond = len(contents)
    f.close()
    totalSaved = lenOfFirst-lenOfSecond
    print("The total amount of charcters saved is: " +str(totalSaved) +" characters.\n")
    menu()

def rleEncode(stringToEncode):
    count = 0
    chatacter = ''
    previous_char = stringToEncode[0]
    result = ''
    length = len(stringToEncode) 
    i = 0
    while (i != length ):
        chatacter = stringToEncode[i]
        if previous_char == chatacter:
            count = count + 1
        else :
            countToReturn = str(count)
            if int(countToReturn) < 10:
                countToReturn = "0" +str(countToReturn)
            result = result + str(countToReturn) + previous_char
            count = 1
        previous_char = chatacter
        i = i + 1
    countToReturn = str(count)
    if int(countToReturn) < 10:
        countToReturn = "0" +str(countToReturn)
    return result + str(countToReturn) + str(previous_char)

def rleDecodeFromPy(stringToDecode):
    """
    DECOMPRESS RLE DATA FROM FILE THAT WAS ENCODED WITH RLEENCODE
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
    print char,

#MAIN
if __name__ == "__main__":
    print("Programming Project Task - Jack Greenacre\n")
    try:
        menu()
    except KeyboardInterrupt:
        print("Thank you for using!")
        quit()
    except:
        print("Fatal Error: An unknown error occurred!\nExiting...\nThank you for using!")
        quit()
