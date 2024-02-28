import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def generate_key(passphrase, salt=None):
    if salt is None:
        salt = os.urandom(16)
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode())), salt

def encrypt_data(data, passphrase):
    salt = os.urandom(16)
    key, _ = generate_key(passphrase, salt)
    encrypted = Fernet(key).encrypt(data.encode())
    return salt + encrypted

def decrypt_data(encrypted_data, passphrase):
    salt, data = encrypted_data[:16], encrypted_data[16:]
    key, _ = generate_key(passphrase, salt)
    return Fernet(key).decrypt(data).decode()
