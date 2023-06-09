from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import base64

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decode base64-encoded data
    encrypted_data = base64.b64decode(encrypted_data)

    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    # Decrypt data
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return decrypted_data.decode()

if __name__ == '__main__':
    # Example usage
    file_path = "path/to/encrypted_file.txt"
    key = b'0123456789ABCDEF'  # Replace with your actual key

    decrypted_text = decrypt_file(file_path, key)
    print(decrypted_text)
