from pyAesCrypt import *

password = input('Задайте пароль: ')

encryptFile('123.txt', '123.txt.aes', password)

#decryptFile('123.txt.aes', '123.txt', password)

