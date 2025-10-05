from PIL import Image

def encode_message(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for n in range(3):
                if index < len(message):
                    pixel[n] = pixel[n] & ~1 | int(message[index])
                    index += 1
            encoded.putpixel((col, row), tuple(pixel))
    encoded.save(output_path)
    print("Message encoded in", output_path)

# Example (convert text to binary before hiding)
secret = ''.join(format(ord(i), '08b') for i in "HELLO")
encode_message("input.png", secret, "output.png")
