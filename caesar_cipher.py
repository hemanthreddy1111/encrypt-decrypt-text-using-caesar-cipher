def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabet characters remain unchanged
    
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption and Decryption")

    choice = input("Choose (E)ncrypt or (D)ecrypt: ").upper()
    
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))  # Ensure the user inputs an integer

    if choice == 'E':
        encrypted_message = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted_message)
    elif choice == 'D':
        decrypted_message = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted_message)
    else:
        print("Invalid choice. Please select either E or D.")

if __name__ == "__main__":
    main()
