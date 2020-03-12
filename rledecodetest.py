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
    return char

print(rleDecode("02a01d06810 06802b01e"))
print(rleDecode("12c"))
