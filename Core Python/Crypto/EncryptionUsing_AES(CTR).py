from Crypto.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import os
# Inputs
key = bytes.fromhex("4e3ebf5b7e5c6d8a9f0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2")
iv = bytes.fromhex("1234567890abcdef1234567890abcdef")
message = b"This is a secret message!"

# Encryption
cipher = AES.new(key, AES.MODE_CTR, nonce=iv[:8], initial_value=iv[8:])
ciphertext = cipher.encrypt(message)

print(f"Ciphertext: {ciphertext.hex()}")

