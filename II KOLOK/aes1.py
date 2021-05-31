from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

salt = os.urandom(32)

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                length=32,
                salt = salt,
                iterations=100000,
                backend=default_backend())

kljuc = kdf.derive(b'OktoRok20')

kdf2 = PBKDF2HMAC(algorithm=hashes.SHA256(),
                length=16,
                salt=salt,
                iterations=100000,
                backend=default_backend())
inicvektor = kdf2.derive(b'ZP202o')

sifObjekat = Cipher(algorithms.AES(kljuc),
            modes.CBC(inicvektor),
            backend = default_backend())

sifrator = sifObjekat.encryptor()
desifrator = sifObjekat.decryptor()

poruka = b'Ova_poruka_ce_se_samounistiti_za_5_sekundi'

print(poruka)

poruka += b"E" * (-len(poruka) % 16)

sifra = sifrator.update(poruka)
original = desifrator.update(sifra)

print('SIFRA:',sifra)
print('ORIGINAL:',original)

if(poruka == original):
    print('jeste')
else:
    print('nije')