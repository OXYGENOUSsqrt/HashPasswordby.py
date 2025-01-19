import hashlib

def MyHash (text):
      return hashlib.sha512(text.encode()).hexdigest()

hash_password = '99f22ff27d35a4cc4a9638c0f0e4fbcbc6cd30216042ed6bc0ac6adda283ea8920cf5a4f5e0e144f7125b34f336e75008f2baea9025bd5a1cdf862205306e71a' #password 1929
print('')
input_password = input('Пароль: ')
hash_input_password = MyHash(input_password)

if hash_password == hash_input_password:
    print ('Вы успешно авторизовались! ')
else:
    print ('Хм... Пароль не верный! ')