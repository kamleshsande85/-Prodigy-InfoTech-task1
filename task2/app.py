from PIL import Image
import random

# Function to encrypt the image
def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size
    
    # Shuffle pixel positions
    random.shuffle(pixels)
    
    # Create a new image and put the shuffled pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(pixels)
    encrypted_img.save(output_path)
    
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image (assuming we know the original pixel order)
def decrypt_image(encrypted_image_path, original_image_path, output_path):
    encrypted_img = Image.open(encrypted_image_path)
    original_img = Image.open(original_image_path)
    
    # Get pixels of the original image
    original_pixels = list(original_img.getdata())
    encrypted_pixels = list(encrypted_img.getdata())
    
    # Sort the encrypted pixels to match the original image pixels
    decrypted_pixels = [None] * len(original_pixels)
    for i, pixel in enumerate(original_pixels):
        index = encrypted_pixels.index(pixel)
        decrypted_pixels[index] = pixel
        encrypted_pixels[index] = None  # Mark as used
    
    # Create a new image and put the decrypted pixels
    decrypted_img = Image.new(encrypted_img.mode, encrypted_img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    
    print(f"Image decrypted and saved as {output_path}")

# Example usage
# encrypt_image("input_image.png", "encrypted_image.png")
decrypt_image("encrypted_image.png", "input_image.png", "decrypted_image.png")
