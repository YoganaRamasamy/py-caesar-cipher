def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = encrypt(message, shift)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)
