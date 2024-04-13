from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys

# Получаем открытый текст в качестве аргумента командной строки
plain_text = sys.argv[1]

# Длина ключа должна быть 16 (AES-128), 24 (AES-192) или 32 (AES-256) байт.
key = b'this is a 16 key'

# Генерируем неповторяемый вектор ключа с длиной,
# равной размеру блока AES
iv = Random.new().read(AES.block_size)

# Инициализируем объект AES с помощью ключа и iv, используя режим MODE_CFB
mycipher = AES.new(key, AES.MODE_CFB, iv)

# Добавляем iv (вектор ключа) в начало зашифрованного шифротекста
# и передаем его вместе
ciphertext = iv + mycipher.encrypt(plain_text.encode())

# Для расшифровки используйте ключ и iv для создания нового объекта AES
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])

# Используйте freshly generated AES объект для расшифровки зашифрованного шифротекста
decrypttext = mydecrypt.decrypt(ciphertext[16:])

# Вывод
file_out = open("encrypted.bin", "wb")
file_out.write(ciphertext[16:])
file_out.close()

print("Ключ k: ", key)
print("iv: ", b2a_hex(ciphertext)[:16])
print("Зашифрованные данные: ", b2a_hex(ciphertext)[16:])
print("Расшифрованные данные: ", decrypttext.decode())