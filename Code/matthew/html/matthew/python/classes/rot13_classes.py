

# rotate_amount = 13
#
# def encode(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     r = ''
#     for char in text:
#         index = alphabet.find(char)
#         index += rotate_amount
#         index %= len(alphabet)
#         r += alphabet[index]
#     return r
#
# print(encode('hello'))





class RotEncoder:

    def __init__(self, rotate_amount):
        self.rotate_amount = rotate_amount

    def encode(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        r = ''
        for char in text:
            index = alphabet.find(char)
            index += self.rotate_amount
            index %= len(alphabet)
            r += alphabet[index]
        return r



if __name__ == '__main__':
    # nums = list()
    # nums.append(5)

    rot_encoder = RotEncoder(13)

    # don't do this
    # rot_encoder.favorite_fruit = 'kiwi'
    # print(rot_encoder.favorite_fruit)

    encoded_str = rot_encoder.encode('hello')
    print(encoded_str)
