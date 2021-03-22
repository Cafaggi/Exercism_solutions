"""
Perform Run Length Encoding compression on a string.
"""


def insert_dash(string, index):
    return string[:index] + '-' + string[index:]

def compress(raw: str) -> bytes:
    """
    Compress the raw string to bytes using RLE.
    """
    compressed_string = ''
    counter = 0
    counter_2 = 0
    current_letter = ''
    occurences = 0

    if not raw:
        return b''

    for letter in raw:
        if not counter:
            current_letter = letter
        if not letter == current_letter:
            raw = insert_dash(raw, counter + counter_2)
            counter_2 += 1
        counter +=  1
        current_letter = letter

    spited_list = raw.split('-')

    for group in spited_list:
        if len(group) < 9:
            occurences = '0{}'.format(len(group))
        else:
            occurences =str(len(group))

        compressed_string += r'{0}{1}'.format(occurences,group[0])  
        compressed_string = bytes(compressed_string,'utf-8')
        
    return bytes(spited_list, 'utf-8')

print(compress('aa'))