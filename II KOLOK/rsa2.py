# Za RSA enkripciju su dati:
# modul # n = 209
# javni ključ e = 7
# šifrat c = 46

# Odrediti privatni ključ d, 
# kojim se pravilno dešifruje vreme m u poruci između Alice i Bob: 
# 'Zadatak mora biti obavljen najviše za ',m,'h.'

import gmpy2

# c = m^e (mod n)  # šifrovanje
# m = c^d (mod n)  # dešifrovanje

p = 11
q = 19
n = 209
e = 7
c = 46

d = gmpy2.invert(e, (p-1)*(q-1))
print(d)

poruka = gmpy2.powmod(c,d,n)
print(poruka)