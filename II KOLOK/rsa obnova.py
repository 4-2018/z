#sifrovanje m^e mod n
#desifrovanje c^d mod n

import gmpy2
 
p = 11
q = 19
c = 46
e = 7
n = p*q

d = gmpy2.invert(e,(p-1)*(q-1))
print(d)

original = gmpy2.powmod(c,d,n)
print(original)


poruke = [9, 14, 21, 0, 13] # j o v a n 
sifrati = []
originali = []

for m in poruke:
    sifrati.append(gmpy2.powmod(m,e,n))
print('SIFRATI:', sifrati)

for i in sifrati:
    originali.append(gmpy2.powmod(i,d,n))
print('ORIGINALI:', originali)