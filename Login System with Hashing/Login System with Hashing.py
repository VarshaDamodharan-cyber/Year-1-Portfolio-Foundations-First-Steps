import hashlib

users = {}

def signup(username, password):
    users[username] = hashlib.sha256(password.encode()).hexdigest()
    print("User registered ✅")

def login(username, password):
    if username in users and users[username] == hashlib.sha256(password.encode()).hexdigest():
        print("Login Successful ✅")
    else:
        print("Login Failed ❌")

signup("alice", "mypassword")
login("alice", "mypassword")   # Success
login("alice", "wrongpass")    # Fail
