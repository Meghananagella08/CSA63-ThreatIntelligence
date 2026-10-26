def xor_cipher(data, key):
    result = []

    for i in range(len(data)):
        encrypted_byte = data[i] ^ key[i % len(key)]
        result.append(encrypted_byte)

    return bytes(result)


# Shared secret key for demonstration
key = b"SECURE"

# Original message
message = b"Transfer 500 dollars"

# Sender encrypts the message
encrypted_data = xor_cipher(message, key)

print("Original Message:", message.decode())
print("Captured Encrypted Data:", encrypted_data.hex())

# Receiver decrypts using the correct key
decrypted_data = xor_cipher(encrypted_data, key)
print("Decrypted with Correct Key:", decrypted_data.decode())

# Try decrypting with a wrong key
wrong_key = b"WRONG!"
wrong_data = xor_cipher(encrypted_data, wrong_key)

print("Decrypted with Wrong Key:", wrong_data)