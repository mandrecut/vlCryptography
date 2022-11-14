#(c) Mircea Andrecut,  mircea.andrecut@gmail.com (2022)
import lorem
import base64
from vlCryptography import vlCryptography

key = lorem.sentence()
print("Key:")
print(key,"\n")

vlC = vlCryptography(key)

plain_text = lorem.paragraph()
print("Plain text:")
print(plain_text,"\n")

cipher_text = vlC.crypt(plain_text.encode())
print("Cipher text:")
print(base64.urlsafe_b64encode(cipher_text).decode(),"\n")

print("Plain text:")
plain_text = vlC.crypt(cipher_text)
print(plain_text.decode())


