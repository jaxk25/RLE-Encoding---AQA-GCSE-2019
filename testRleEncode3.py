def encode(stringToEncode):
    count = 0
    chatacter = ''
    previous_char = stringToEncode[0]
    result = ''
    length = len(stringToEncode) 
    i = 0
    while (i != length ):
        chatacter = stringToEncode[i]
        if previous_char == chatacter :
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
encoded_message=encode("AAAAAAAAAABBBBCCCCCCCCAB/__")
print(encoded_message)
