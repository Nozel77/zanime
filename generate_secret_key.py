# generate_secret_key.py
import secrets

# Menghasilkan kunci hex 64 karakter
secret_key = secrets.token_hex(32)
print(f"Generated Secret Key: {secret_key}")
