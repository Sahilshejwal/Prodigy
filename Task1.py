def caesar_cipher(text, shift, mode):
    result = ""

   
    if mode.lower() == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            
            result += char

    return result


print("===== Caesar Cipher =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    encrypted = caesar_cipher(message, shift, "encrypt")
    print("\nEncrypted Message:", encrypted)

elif choice == "2":
    decrypted = caesar_cipher(message, shift, "decrypt")
    print("\nDecrypted Message:", decrypted)

else:
    print("Invalid choice!")
