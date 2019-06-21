user_Input = input("Give me a string and I will encode it for you: \n")
user_Input_Lower = user_Input.lower()
input_len = len(user_Input)
encoding_pointer = 0

while encoding_pointer != input_len:
    print(f"Letter {encoding_pointer + 1}:", user_Input_Lower[encoding_pointer])
    encoded_letter_number = ord(user_Input_Lower[encoding_pointer]) +13
    if encoded_letter_number >= ord('z'):
        encoded_letter_number -= 26
    encoded_letter = chr(encoded_letter_number)
    print(encoded_letter)
    encoding_pointer +=1

