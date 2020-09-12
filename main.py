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

def rleMenu(): # Function for decompression function and menu
    """
    ENTER COMPRESSED DATA TO DECOMPRESS
    """
    needToBreak = True # Preset variables
    rleLinesTrue = False # Preset variables
    while not rleLinesTrue: # While user is entering amount of lines,
        needToBreak = True # Reset variable
        rleLinesTrue = False # Reset variable
        try:
            rleLines = input("How many lines of RLE compressed data would you like to enter?\n>>> ") # Ask for user input
        except KeyboardInterrupt: # If user pressed C^c,
            print("\nError: There was a keyboard interrupt!\nThank you for using!\n") # Display an exit message
            quit() # Quit the program
        except: # If there was an error with the input,
            print("\nError: Sorry, that is not a valid number.\nPlease try again with a recognised option - e.g. `2` or `6`\n") # Give an error
            needToBreak = False # Set variable
        finally: # If there was no errors,
            if needToBreak: # Check if it is ok to break the loop
                rleLinesTrue = True # Set variable
                break # Break out of loop
    if str(type(rleLines)) != "<type 'int'>": # Check if the rleLines is not an integer
        print("\nError: Sorry, that is not a valid number.\nPlease try again with a recognised option - e.g. `2` or `6`\n") # Give an error
        rleMenu() # Call the rleMenu function to restart the RLE decompression menu and function
    else: # If the rleLines is an integer,
        pass # Continue
    if rleLines <= 2: # Check how many lines the user wants to enter. If rleLines is smaller than 3,
        print("\nError: Sorry, that is not long enough.\nPlease try again with a value greater than `2`\n") # Give an error
        rleMenu() # Call the rleMenu function to restart the RLE decompression menu and function
    else: # If rleLines in above 2,
        pass # Continue
    for i in range(1,rleLines+1): # Repeat for the amount of lines that the user wants to enter
        globals()["rleLine" +str(i)] = str(raw_input("\nPlease input a line of RLE encoded data.\n>>> ")) # Set variable with RLE encoded data
    print("\nYou have entered:") # Recall data to show to user
    for i in range(1,rleLines+1): # Repeat for amount of lines of encoded data entered
        print(globals()["rleLine" +str(i)]) # Print the encoded data
    menuOption = raw_input("\nIs this correct? [Y/N]\n>>> ") # Ask for user input to confirm if data is correct
    menuOption = str(menuOption) # Convert to string
    menuOption = menuOption.lower() # Convert to lower-case
    while True: # Repeat until broken
        if menuOption == "y": # If user input is yes,
            break # Break out of loop
        elif menuOption == "n": # Is user input is no,
            print("") # Print an empty line
            rleMenu() # Call the rleMenu function to restart the RLE decompression menu and function
        else: # If the user input is neither,
            print("\nError: That was not understood.\nPlease try again with a recognised option - e.g. `y` or `n`\n") # Give an error
    print("") # Print an empty line
    for i in range(1,rleLines+1): # For the amount of lines that the user inputted,
        rleDecode(globals()["rleLine" +str(i)]) # Call the rleDecode function to decode the encoded data
    print("") # Print an empty line
    menu() # Call the menu function to show the main function

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
