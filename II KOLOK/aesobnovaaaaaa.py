from cryptography.hazmat.primitives.kdf import pbkdf2
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

salt = os.urandom(32)

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

kljuc = kdf.derive(b'JunRok2021')

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=16, salt=salt, iterations=100000, backend=default_backend())

inicvektor = kdf.derive(b'Zpod2021')

sifraObjekat = Cipher(algorithms.AES(kljuc), modes.CBC(inicvektor), backend=default_backend())

sifrator = sifraObjekat.encryptor()
desifrator = sifraObjekat.decryptor()

poruka = b'Jovan Govedarica'
poruka += b"E" * (-len(poruka) % 16)

sifra = sifrator.update(poruka)
original = desifrator.update(sifra)


print(sifra)
print(original)
