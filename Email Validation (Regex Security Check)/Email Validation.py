import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

email = input("Enter email: ")
if is_valid_email(email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")
