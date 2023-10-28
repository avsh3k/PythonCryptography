from cryptography.fernet import Fernet

# Generate a random encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    encrypted_data = cipher_suite.encrypt(plaintext)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f'File "{input_file}" encrypted and saved as "{output_file}".')

def decrypt_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    print(f'File "{input_file}" decrypted and saved as "{output_file}".')

# Example usage
encrypt_file('plaintext.txt', 'encrypted.txt')
decrypt_file('encrypted.txt', 'decrypted.txt')
