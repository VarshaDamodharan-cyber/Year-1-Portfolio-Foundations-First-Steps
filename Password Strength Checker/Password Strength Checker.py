import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&#]", password):
        strength += 1
    
    if strength == 5:
        return "Strong Password ✅"
    elif strength >= 3:
        return "Moderate Password ⚠️"
    else:
        return "Weak Password ❌"

pwd = input("Enter password: ")
print(check_password_strength(pwd))
