import re
def decode(string):
    if string == '':
        return ''
    multiplier = 1
    count = 0
    rle_decoding = []
                          
    rle_encoding = []
    rle_encoding = re.findall(r'[A-Za-z]|-?\d+\.\d+|\d+|[\w\s]', string) 
    for item in rle_encoding:
        if item.isdigit():
            multiplier = int(item)
        elif item.isalpha() or item.isspace():
            while count < multiplier:
                rle_decoding.append('{0}'.format(item))
                count += 1
            multiplier = 1
            count = 0 
    return(''.join(rle_decoding))

def encode(string):
    if string == '':
        return ''
    i = 0
    count = 0
    letter = string[i]
    rle = []
    while i <= len(string) - 1:        
        while string[i] == letter:
            i+= 1
            count +=1
            if i > len(string) - 1:
                break
        if count == 1:
            rle.append('{0}'.format(letter))
        else:
            rle.append('{0}{1}'.format(count, letter))
        if i > len(string) - 1:
            break
        letter = string[i]
        count = 0
    final = ''.join(rle)
    return final

        
decode('2 hs2q q2w2 ')
#encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')
