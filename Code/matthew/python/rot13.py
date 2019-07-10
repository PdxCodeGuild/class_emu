
def rot13_1(input_text):
    output = ''
    for char in input_text:
        if char == 'a':
            output += 'n'
        elif char == 'b':
            output += 'o'
        elif char == 'c':
            output += 'p'
        elif char == 'd':
            output += 'q'
        # ...
        else:
            output += char
    return output

# print(rot13('hello world'))


def rot13_2(input_text):
    output = ''
    alphabet =         'abcdefghijklmnopqrstuvwxyz !#'
    rotated_alphabet = 'nopqrstuvwxyzabcdefghijklm !#'
    for input_char in input_text:
        found_char = False
        for i in range(len(alphabet)):
            if input_char == alphabet[i]:
                output += rotated_alphabet[i]
                found_char = True
                break
        if not found_char:
            output += input_char
    return alphabet

def rot13_3(input_text):
    output = ''
    alphabet =         'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = 'nopqrstuvwxyzabcdefghijklm'
    for input_char in input_text:
        index = alphabet.find(input_char)
        if index == -1:
            output += input_char
        else:
            output += rotated_alphabet[index]
    return output


# print(rot13_3('hello world!'))


def rotn(input_text, n):
    output = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for input_char in input_text:
        index = alphabet.find(input_char)
        if index == -1:
            output += input_char
        else:
            index += n
            index %= 26
            # while index > 26:
            #     index -= 26
            output += alphabet[index]
    return output



# ord('a') == 97
# chr(97) == 'a'

def rotn_2(input_text, n):
    output = ''
    for input_char in input_text:
        ascii_code = ord(input_char)
        ascii_code -= ord('a')
        ascii_code += n
        ascii_code %= 26
        ascii_code += ord('a')
        output += chr(ascii_code)
    return output

