from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from getpass import getpass
import os
import json
import secrets
import base64


def generate_key(master_password, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**15,
        r=8,
        p=1
    )

    key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(key)


def encrypt_pass(password, key):
    encrypted = Fernet(key).encrypt(password.encode())
    return encrypted.decode()


def decrypt_pass(encry_pass, key):
    try:
        return Fernet(key).decrypt(encry_pass.encode()).decode()
    except InvalidToken:
        return None


def create_vault():
    while True:
        master_pass = getpass("Create master password: ", echo_char="*")
        c_master_pass = getpass("Confirm master password: ", echo_char="*")
        os.system("cls" if os.name == "nt" else "clear")

        if not master_pass:
            print("Master password cannot be empty.")
            continue
        
        if master_pass == c_master_pass:
            salt = secrets.token_bytes(16)
            key = generate_key(master_pass, salt)
            data = {"salt": base64.b64encode(salt).decode(), "verification_token": Fernet(key).encrypt(b"vault_verified").decode(), "accounts":[]}
            with open("vault.json", "w") as file:
                json.dump(data, file, indent=4)
            return key
        
        print("Confirm passwords don't match. Try again.")


def unlock_vault():
    while True:
        master_pass = getpass("Master password: ", echo_char="*")
        os.system("cls" if os.name == "nt" else "clear")

        with open("vault.json", "r") as file:
            data = json.load(file)

        if not master_pass:
            print("Master password cannot be empty.")
            continue

        key = generate_key(master_pass, base64.b64decode(data["salt"]))

        try:
            verification_string = Fernet(key).decrypt(data["verification_token"].encode()).decode()

            if verification_string == "vault_verified":
                return key

            print("Unable to unlock vault. Vault data may be corrupted.")

        except InvalidToken:
            print("Incorrect master password or vault data is corrupted.")

