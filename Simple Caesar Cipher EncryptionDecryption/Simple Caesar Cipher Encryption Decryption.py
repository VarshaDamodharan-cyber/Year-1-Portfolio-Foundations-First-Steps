def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

msg = "HELLO CYBER WORLD"
enc = caesar_cipher(msg, 3)
dec = caesar_cipher(enc, 3, "decrypt")

print("Encrypted:", enc)
print("Decrypted:", dec)
