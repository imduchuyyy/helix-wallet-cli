from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

class Cryptography:
    @staticmethod
    def encrypt_mnemonic(mnemonic, password):
        salt = b'\x00' * 16  # Use a random salt in a real-world scenario

        # Derive a key using PBKDF2HMAC
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        # Pad the mnemonic to be a multiple of 16 (AES block size)
        padded_mnemonic = mnemonic.ljust((len(mnemonic) // 16 + 1) * 16)

        # Create an AES cipher with the derived key and a random IV
        cipher = Cipher(algorithms.AES(key), modes.CFB(b'\x00' * 16), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt the padded mnemonic
        ciphertext = encryptor.update(padded_mnemonic.encode()) + encryptor.finalize()

        # Combine the salt and ciphertext for storage
        encrypted_data = salt + ciphertext

        # Return the base64-encoded result
        return base64.b64encode(encrypted_data).decode()

    @staticmethod
    def decrypt_mnemonic(encrypted_data, password):
        # Decode the base64-encoded input
        encrypted_data = base64.b64decode(encrypted_data)

        # Extract the salt and ciphertext
        salt = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        # Derive the key using the provided password and salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        # Create an AES cipher with the derived key and a random IV
        cipher = Cipher(algorithms.AES(key), modes.CFB(b'\x00' * 16), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt the ciphertext
        decrypted_mnemonic = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove any trailing padding and return the result
        return decrypted_mnemonic.rstrip(b'\x00').decode()

# Example usage:
mnemonic = "example mnemonic wordsweet"
password = "your_password"

encrypted_data = Cryptography.encrypt_mnemonic(mnemonic, password)
print("Encrypted Data:", encrypted_data)

decrypted_mnemonic = Cryptography.decrypt_mnemonic(encrypted_data, password)
print("Decrypted Mnemonic:", decrypted_mnemonic)
