# Very Light Cryptography

This is a "very light" encryption/decryption method, without any dependencies, just plain vanilla Python. 

Warning, "do it yourself encryption" is not encouraged, better use an existing validated approach. The method described here was developed only for educational purposes, it is not fully tested and validated, in practice use at your own risk. 

## Basic usage

```python
import lorem
from vlCryptography import vlCryptography

pswd = lorem.sentence()
print("Pswd:")
print(pswd,"\n")

plain_text = lorem.paragraph() + " " + lorem.paragraph()
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

output 

```
Pswd:
Quiquia adipisci ut porro quisquam quisquam. 

Plain text:
Labore adipisci modi porro adipisci quiquia. Labore aliquam quaerat dolore neque. Tempora consectetur consectetur dolore. Modi quisquam numquam eius ipsum modi sed. Est est sit porro dolor sit. Numquam tempora amet labore non neque consectetur numquam. Consectetur ut aliquam non aliquam quisquam ut. Adipisci magnam numquam sed non aliquam. Etincidunt dolore magnam voluptatem non porro. Magnam quaerat magnam tempora voluptatem adipisci. Velit dolor eius porro aliquam adipisci. 

Cypher text
<UHbCTd!SnWAOv%0G=X2X&;l:^P2R/"X$wIOEOg5$KlzNxD?4}% -S>{|*:J_x%64t3v}Wbh!Cor",$sxqC1lq[P{MjZ#)7:c9Cg8,%g9@.='Muk1xt5[Q",me%,zh4t?7{<B".b&Cotk0%1GgCXpe61wWURX>FaR}?E\3;$C^.k0NA<El}sD."[wxv-pQh~EwzYo,p.Q{Uf`WF=6h3&xoY7!Yc\6EUnkqMiL05Nr/8+l!|4ZoIUF`)LC|[Q1&zWrK9*6qR!5s<yTk<Mg4$3?EgUX[L&0.t[(sxdRU:Z}Z/WX)rJCuWAy2MB>shdk&DUVM^%Y#S&tJ,cmy>`V~jB^S}1tL-mb5V=~JC3/tWGtA|"*gtVt-<.-%H6{a8Xib{{VZ9h%%<ru}^qSSyc,;+N<#O#9nUJc4g~k`DiI#aTTbC}TA`0O5=C&,qgEVz~_BG~JW8GqFjmMVQuWSF^H[VAK3NL@;Qp_i[G 

Plain text:
Labore adipisci modi porro adipisci quiquia. Labore aliquam quaerat dolore neque. Tempora consectetur consectetur dolore. Modi quisquam numquam eius ipsum modi sed. Est est sit porro dolor sit. Numquam tempora amet labore non neque consectetur numquam. Consectetur ut aliquam non aliquam quisquam ut. Adipisci magnam numquam sed non aliquam. Etincidunt dolore magnam voluptatem non porro. Magnam quaerat magnam tempora voluptatem adipisci. Velit dolor eius porro aliquam adipisci.
```
