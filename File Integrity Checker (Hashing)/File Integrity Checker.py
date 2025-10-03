import hashlib

def hash_file(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as f:
        chunk = f.read(1024)
        while chunk:
            h.update(chunk)
            chunk = f.read(1024)
    return h.hexdigest()

file = input("Enter file name: ")
print("SHA256 Hash:", hash_file(file))
