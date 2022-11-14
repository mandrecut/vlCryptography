# Very Light Cryptography

This is a "very light" encryption/decryption method, without any dependencies, just plain vanilla Python. 

Warning, "do it yourself encryption" is not encouraged, better use an existing validated approach. The method described here was developed only for educational purposes, it is not fully tested and validated, in practice use it at your own risk. 

## Basic usage

```python
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
```

Output example:

```
Key:
Eius ut adipisci amet. 

Plain text:
Eius ipsum ut voluptatem ut magnam eius. Amet consectetur quiquia dolorem. Non modi neque adipisci velit voluptatem labore adipisci. Tempora eius porro tempora quisquam. Consectetur dolor consectetur est. Quiquia quaerat porro sit. Sed velit quisquam sit sed magnam. Sed non quisquam consectetur porro aliquam aliquam sit. 

Cipher text:
KREZK-yRPIuZNQzt-Bj618DtHCwtDKkVTK3YOGHZa1ZNdcy9pY0_1swZQf34GO_XwusJOzgduA0e-N1tZcl5UU04iLeglz6dgXYM1uNWrNXD_AV4Ih29DQn4zXxlyGVLT3HMrqmUJYzMLkP0-Uj42dj9AXggGa4XHr2MeWjRfFFfe4X27KwplZw3XvmsXeXN37gcNz4Ko1gYvcFoY8ptGF1thau9jS2Vwnhv9-JL6dvY_RgtPlioFwC33jhv12JLSXuYvbiNPtiJK1i2rGn50d3tBTlsCbkZCarNbCzIY0ped8yrpYxi2L89SLj6XeDR2LgdLSULvQ0NtYxrZcwsS0l8zLWtnyKZgXYMy-lcrNbD9kwpORG_CRm5wThv12JLSXuYvThNXiiUM1i40gFU30nsCdkMTDDkiNqWSE15hvxALg== 

Plain text:
Eius ipsum ut voluptatem ut magnam eius. Amet consectetur quiquia dolorem. Non modi neque adipisci velit voluptatem labore adipisci. Tempora eius porro tempora quisquam. Consectetur dolor consectetur est. Quiquia quaerat porro sit. Sed velit quisquam sit sed magnam. Sed non quisquam consectetur porro aliquam aliquam sit.
```
