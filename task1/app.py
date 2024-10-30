def encrypt(text, shift):
    # Initialize an empty string to store the encrypted text
    encrypted_text = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is a letter (either uppercase or lowercase)
        if char.isalpha():
            # Determine the ASCII base value: 65 for uppercase ('A'), 97 for lowercase ('a')
            shift_base = 65 if char.isupper() else 97
            
            # Encrypt the character by shifting it in the alphabet by the given shift value
            # The formula ensures the shift wraps around within the alphabet (mod 26)
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # If the character is not a letter (e.g., space, punctuation), add it unchanged
            encrypted_text += char
    
    # Return the final encrypted text
    return encrypted_text

def decrypt(text, shift):
    # Decrypt the text by reusing the encrypt function with a negative shift value
    return encrypt(text, -shift)

# Example usage: Ask the user to input a message and a shift value
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt the message using the provided shift value
encrypted_message = encrypt(message, shift_value)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message to verify it matches the original input
decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted Message: {decrypted_message}")
