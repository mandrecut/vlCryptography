#(c) Mircea Andrecut,  mircea.andrecut@gmail.com (2022)
import lorem
from vlCryptography import vlCryptography

pswd = lorem.sentence()
print("Pswd:")
print(pswd,"\n")

plain_text = lorem.paragraph()
print("Plain text:")
print(plain_text,"\n")

vlC = vlCryptography()

cypher_text = vlC.crypt(pswd,plain_text)
print("Cypher text:")
print(cypher_text,"\n")

print("Plain text:")
plain_text = vlC.crypt(pswd,cypher_text)
print(plain_text)


