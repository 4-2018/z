from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import gmpy2, os, binascii

# c = m^e mod n sifrovanje
# m = c^d mod n desifrovanje

p = 11
q = 19
n = p*q
e = 7

poruke = [17,19,21,23]
sifrati = []
originali = []


d = gmpy2.invert(e, (p-1)*(q-1))
print(d)

#sifrovanje
for m in poruke:
    sifrati.append(gmpy2.powmod(m, e, n))
print('Sifrati:', sifrati)

#desifrovanje
for m in sifrati:
    originali.append(gmpy2.powmod(m,d,n))
print('Original:', originali)