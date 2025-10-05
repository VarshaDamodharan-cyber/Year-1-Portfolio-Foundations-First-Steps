import itertools

def brute_force(target):
    chars = "abc123"
    for length in range(1, 5):
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            if guess == target:
                return guess
    return None

password = "b2"
print("Cracked Password:", brute_force(password))
