


from encryptor import RotEncryptor

rot_encryptor = RotEncryptor(8)

print(rot_encryptor.get_rotation_amount()) # 8

text = 'hello world!'
encrypted_text = rot_encryptor.encrypt(text)
print(encrypted_text)

original_text = rot_encryptor.decrypt(encrypted_text)
print(original_text)




