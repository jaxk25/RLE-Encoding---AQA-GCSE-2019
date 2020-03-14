def rleEncode(stringToEncode):
    """
    ENCODE ASCII DATA FROM CONVERTRLEMAIN
    """
    listToEncode = list(stringToEncode)
    count = 0
    char = ''
    string = ''
    endString = ''
    timesRepeated = 0
    for item in listToEncode:
        if item == char:
            string += item
            char = item
        elif item != char:
            count = len(string)
            if count <= 9:
                count = str(count)
                count = "0" +str(count)
            endString += str(count)
            endString += char
            char = item
            string = ''
            string += item
            timesRepeated = timesRepeated+1
    count = len(string)
    if timesRepeated >= 2:
        if count < 10 :
            count = str(count)
            count = "0" +str(count)
        endString += str(count)
        endString += char
        char = item
    string = ''
    endString = list(endString)
    del endString[0]
    del endString[1]
    string = endString
    endString = ''
    for i in range(len(string)):
        endString += string[i]
    return endString
