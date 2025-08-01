import hashlib

password = "admin"
md5_hash = hashlib.md5(password.encode()).hexdigest()
print(f"MD5 hash of '{password}' is: {md5_hash}")
