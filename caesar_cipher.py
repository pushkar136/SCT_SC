def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\nChoose an option:")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")

if choice == "1":
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)
elif choice == "2":
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)
else:
    print("Invalid choice")
