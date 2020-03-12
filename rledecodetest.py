def rle_decode(data):
    decode = ''
    count = ''
    current = 0
    for char in data:
        if char.isdigit() and current <= 2:
            count += char
            current = current+1
        else:
            decode += char * int(count)
            count = ''
    return decode
