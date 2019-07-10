
class RotEncryptor:
    def __init__(self, n=13):
        self.__n = n
    
    def encrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        output = ''
        for char in text:
            index = alphabet.find(char)
            if index == -1:
                output += char
            else:
                output += alphabet[(index+self.__n)%len(alphabet)]
        return output
    
    def decrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        output = ''
        for char in text:
            index = alphabet.find(char)
            if index == -1:
                output += char
            else:
                output += alphabet[(index-self.__n)%len(alphabet)]
        return output
        
    def get_rotation_amount(self):
        return self.__n