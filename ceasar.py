def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        # Check if the character is an uppercase letter
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        encrypted_message += encrypted_char
    return encrypted_message

# Example usage:
plaintext = input()
shift = 3
encrypted_message = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted message:", encrypted_message)
