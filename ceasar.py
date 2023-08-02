def caesar_cipher_encrypt(plaintext, shift):
    encrypted_message = ""
    for char in plaintext:
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_message = ""
    for char in ciphertext:
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")
    if choice.lower() == 'e':
        plaintext = input("Enter the plaintext message: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher_encrypt(plaintext, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.lower() == 'd':
        ciphertext = input("Enter the ciphertext message: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
