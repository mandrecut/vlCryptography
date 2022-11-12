# Very Light Cryptography

This is a "very light" encryption/decryption method, without any dependencies, just plain vanilla Python. 

Warning, "do it yourself encryption" is not encouraged, better use an existing validated approach. The method described here was developed only for educational purposes, it is not fully tested and validated, in practice use it at your own risk. 

## Basic usage

```python
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
print("Cypher text")
print(cypher_text,"\n")

print("Plain text:")
plain_text = vlC.crypt(pswd,cypher_text)
print(plain_text)
```

Output example:

```
Pswd:
Dolorem est est dolore sed. 

Plain text:
Adipisci est voluptatem sit etincidunt. Sit etincidunt quiquia est. Sit est adipisci eius sed est etincidunt. Quaerat consectetur eius modi modi eius. Dolorem consectetur numquam sed dolore. Amet modi numquam dolore sit modi. Quisquam non eius voluptatem labore. Aliquam dolore dolorem etincidunt etincidunt. 

Cypher text
dZ:j&O2_'AKK2:5I%MO*Ay~>n n/_-PH4lv05]`)Qugv`Vs%qA;R__CJ.B =k/sdbHF|^& V0V.28Z6rVu`kM[l&KK.|bP9"Y]^1gX/l0p ~JQq*+.ipzN[/pIu}v,AN[r'to&h.Z-#p_.}L5gJs0)-m/d>yXm1cYk&4++GPELIO5[coa<tZ.c|=Hu>dM9/:oNp*"_!IFmA8}P$K$B"7X<S:5yu')p5[YDUo.4znE@NpA_jO\fA%@`p~`vsox@\RjenNe06vb.KEx):,XM.Nz`[Y6`aaZUs4SvpBf|{3P0(JL@U:3&y_ 

Plain text:
Adipisci est voluptatem sit etincidunt. Sit etincidunt quiquia est. Sit est adipisci eius sed est etincidunt. Quaerat consectetur eius modi modi eius. Dolorem consectetur numquam sed dolore. Amet modi numquam dolore sit modi. Quisquam non eius voluptatem labore. Aliquam dolore dolorem etincidunt etincidunt.
```
