#(c) Mircea Andrecut,  mircea.andrecut@gmail.com (2022)
class vlCryptography(object):
    def __init__(self):
        self._alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    def crypt(self,pswd,txt):
        if len(pswd) < 9:
            raise ValueError("Password must be minimum 9 characters length.")
        K,M,N = len(self._alphabet),len(pswd),len(txt)
        pswd = [self._alphabet.index(q) for q in pswd]
        for J in range(N):
            if J < M: # mixing
                pswd = [(pswd[m-2] + pswd[m-1] + pswd[m]) % K for m in range(M)]
            else: # mixing & growing
                pswd = [(pswd[m-2] + pswd[m-1] + pswd[m]) % K for m in range(J)]
                pswd.append(sum(pswd) % K)
        return "".join([self._alphabet[(pswd[n] - self._alphabet.index(txt[n]))%K] for n in range(N)])
