import bcrypt

# Suppose you have a previously hashed password (e.g., from a database)
stored_hashed_password = b'$2b$12$XC27svjYb09OePQ.I6RBJOtsGnXwitdTU1hcyg8WojbHx3y24S8/m'  # Example hash

# Input password from user
password = input("Enter password to verify: ")

# Convert the password to bytes
password_bytes = password.encode('utf-8')

# Verify if the entered password matches the stored hash
if bcrypt.checkpw(password_bytes, stored_hashed_password):
    print("Password is correct!")
else:
    failed_hash = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    print("Password is incorrect!")
    # Show the failed password attempt (in byte format)
    print("Entered password (in bytes):", failed_hash)
