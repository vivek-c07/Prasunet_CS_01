# Encryption Function
def encrypt(plain_text, shift):
    encrypted_message = ""

    #Perform the movement for each character
    for char in plain_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Decryption Function
def decrypt(encrypted_message, shift):
    decrypted_message = ""

    #Undo Movement for each character
    for char in encrypted_message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

if __name__ == '__main__':
    # Provide Prompts for user input
    print("Enter 1 for Encryption\nEnter 2 for Decryption")
    x = int(input("Enter Option : "))

    # Perform Encryption/Decryption based on user Input
    if x == 1:
        message = input("Message : ")
        shift = int(input("Enter Shift Value : "))
        print("Encrypting Message...")
        print("Encrypted Message :", encrypt(message, shift))
    else:
        message = input("Message : ")
        shift = int(input("Enter Shift Value : "))
        print("Decrypting Message...")
        print("Decrypted Message :", decrypt(message, shift))
