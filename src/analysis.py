#(c) Mircea Andrecut,  mircea.andrecut@gmail.com (2022)
import math
import bz2
import lzma
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def runCA(C,L):
    C,M,Q = bytearray(C.encode()),len(C), np.zeros((L,L))
    for J in range(M,L):
        C = [(C[n-2] + C[n-1] + C[n]) % 256 for n in range(J)]
        C.append(sum(C) % 256)
        Q[J,0:J+1] = C
    return 255-Q

def entropy(C):
    p, lns = Counter(C), float(len(C))
    return -sum(count/lns * math.log(count/lns, 256) for count in p.values())

if __name__== "__main__":
    C = "abcdefghijklmnop"
    C = runCA(C,32768)
    F = np.fft.fft(C[-1]-np.mean(C[-1]))[:len(C)//2]

    fig = plt.figure(figsize=(10,10))
    plt.imshow(C[0:1024,0:1024].T, cmap='gray',interpolation=None)
    plt.xlabel('t'); plt.ylabel('C(t)')
    plt.xlim([0, 1024]); plt.ylim([0, 1024])
    fig.savefig("fig1.pdf",bbox_inches="tight")

    fig = plt.figure(figsize=(10,6))
    plt.hist(C[-1],256, facecolor='gray', density=True)
    plt.xlim([0, 256]);plt.ylim([0, 0.02])
    plt.xlabel('s'); plt.ylabel('p(s)')
    fig.savefig("fig2.pdf",bbox_inches="tight")

    fig = plt.figure(figsize=(8,4))
    plt.plot(np.arange(len(F)),np.abs(F),linewidth=0.1,color="gray")
    plt.xlim([0, len(F)]); plt.ylim([0, 1.1*np.max(np.abs(F))])
    plt.xlabel('$f$'); plt.ylabel('$|F(f)|$')
    fig.savefig("fig3a.pdf",bbox_inches="tight")

    fig = plt.figure(figsize=(8,4))
    plt.hist(np.abs(F),256, facecolor="gray", density=True)
    plt.xlim([0, np.max(np.abs(F))])
    plt.xlabel('$|F(f)|$'); plt.ylabel('$p(|F(f)|)$')
    fig.savefig("fig3b.pdf",bbox_inches="tight")

    fig = plt.figure(figsize=(8,4))
    plt.hist(np.angle(F),256, facecolor="gray", density=True)
    plt.xlim([np.min(np.angle(F)),np.max(np.angle(F))])
    plt.xlabel(r'$\varphi$'); plt.ylabel(r'$p(\varphi)$')
    fig.savefig("fig3c.pdf",bbox_inches="tight")

    H = entropy(bytes(C[-1]))
    Z = lzma.compress(bytes(C[-1]))
    print("Entropy = ", H)
    print("LZMA compression ratio = ", len(Z)/len(C[-1]))
    Z = bz2.compress(bytes(C[-1]))
    print("BZIP2 compression ratio = ", len(Z)/len(C[-1]))
