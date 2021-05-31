import hashlib
import os
#prazanHash = hashlib.md5()
#print('md5 prazan hash:', prazanHash.hexdigest())

#MD5
hashJovan = hashlib.md5(b'jovan').hexdigest()
print('hash od jovan:',hashJovan)

#UPDATE
upd=hashlib.md5()
upd.update(b'j')
upd.update(b'o')
upd.update(b'v')
upd.update(b'a')
upd.update(b'n')
print('Update:',upd.hexdigest())

#SHA
sha1Jovan = hashlib.sha1(b'jovan').hexdigest()
print('SHA1:',sha1Jovan)
sha256Jovan = hashlib.sha256(b'jovan').hexdigest()
print('SHA256:',sha256Jovan)
sha3_512Jovan = hashlib.sha3_512(b'jovan').hexdigest()
print('SHA3_512:', sha3_512Jovan)

#SALTED
salt = os.urandom(16)
print(salt)

hashJovanS= b'jovan'
jovanSalted = hashJovanS + salt

print('SALTEDJOVAN:',hashlib.md5(jovanSalted).hexdigest())

