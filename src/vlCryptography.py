#(c) Mircea Andrecut,  mircea.andrecut@gmail.com (2022)
class vlCryptography(object):
    def __init__(self, key):
        if len(key) < 9: raise ValueError("Key length must be minimum 9 characters.")
        self._key = key.encode()

    def crypt(self,x):
        if len(x) == 0: raise ValueError("Empty source.")
        key,x,M,N = bytearray(self._key),bytearray(x),len(self._key),len(x)
        for J in range(M,N):
            key = [(key[m-2] + key[m-2] + key[m-1]) % 256 for m in range(J)]
            key.append(sum(key) % 256)
        return bytes([key[n]^x[n] for n in range(N)])