"""
EUDP 1.0.0
A module for encrypted UDP connections.
"""

import rsa
import base64
import string
import socket
import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class EUDPServer:
    def __init__(self, IP, Port, AES_KEY):

        self.AES_KEY = Utils().password_to_key(AES_KEY)
        self.DEFAULT_BUFFER_SIZE = 1024*4

        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((IP, Port))

    def send(self, ADDR, data):
        self.server.sendto(Fernet(self.AES_KEY).encrypt(data.encode()), ADDR)

    def recv(self):
        try:
            MSG, ADDR = self.server.recvfrom(self.DEFAULT_BUFFER_SIZE)
            return Fernet(self.AES_KEY).decrypt(MSG).decode(), ADDR
        except:
            return None
        
    def close(self):
        self.server.close()


class EUDPClient:
    def __init__(self, IP, Port, AES_KEY):

        self.DEFAULT_BUFFER_SIZE = 1024 * 4
        self.AES_KEY = Utils().password_to_key(AES_KEY)

        self.Server = (IP, Port)

        self.Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data):
        self.Client.sendto(Fernet(self.AES_KEY).encrypt(data.encode()), self.Server)

    def recv(self):
        try:
            while True:
                DATA, ADDR = self.Client.recvfrom(self.DEFAULT_BUFFER_SIZE)
                if ADDR == self.Server:
                    return Fernet(self.AES_KEY).decrypt(DATA)
        except:
            return None

    def close(self):
        self.Client.close()


class Utils:

    def generate_keys_save(self):
        pubkey,privkey = rsa.newkeys(1024)
        with open("pubkey.pem","wb") as f:
            f.write(pubkey.save_pkcs1("PEM"))
            f.close()
        with open("privkey.pem", "wb") as f:
            f.write(privkey.save_pkcs1("PEM"))
            f.close()


    def generate_keys(self):
        pubkey,privkey = rsa.newkeys(1024)
        return pubkey,privkey



    def load_keys(self):
        with open("pubkey.pem", "rb") as f:
            raw_pub = f.read()
            f.close()
        with open("privkey.pem", "rb") as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read())
            f.close()
        return raw_pub , privkey



    def encrypt_rsa(self,data,pubkey):
        pubkey = rsa.PublicKey.load_pkcs1(pubkey)
        return rsa.encrypt(data.encode("ascii"),pubkey)


    def decrypt_rsa(self,data,privkey):
        try:
            return rsa.decrypt(data,privkey).decode("ascii")
        except:
            return False

    def password_to_key(self,password):
        salt = b'.-Kh)ura/)\xcef\xc8\x88u\xc2'
        password = password.encode()
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def make_random_pass(self):
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=35))
        return res

