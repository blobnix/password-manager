from encryption import encrypt_pass, decrypt_pass, create_vault, unlock_vault
from urllib.parse import urlparse
from getpass import getpass
import pyperclip
import os
import json

def main():
    os.system("cls" if os.name == "nt" else "clear")
    if os.path.exists("vault.json"):
        key = unlock_vault()
    else:
        key = create_vault()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("===== PASSWORD MANAGER =====")
        print("1. Add account")
        print("2. View accounts")
        print("3. Edit account")
        print("4. View password")
        print("5. Delete account")
        print("0. Exit")
        option = input("\nSelect an option: ")

        if option == "0":
            break
        
        elif option == "1":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("===== ADD ACCOUNT =====")

                while True:
                    website = input("Website: ").strip()

                    if not website.startswith(("http://", "https://")):
                        website = "https://" + website

                    parsed = urlparse(website)

                    if parsed.scheme in ["http", "https"] and parsed.hostname and "." in parsed.hostname:
                        w = parsed.hostname.removeprefix("www.")
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== ADD ACCOUNT =====")
                        print("Website: " + w)
                        break

                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== ADD ACCOUNT =====")
                    print("URL is not valid")

                while True:
                    u = input("Username: ").strip()

                    if u != "":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== ADD ACCOUNT =====")
                        print("Website: " + w)
                        print("Username: " + u)
                        break

                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== ADD ACCOUNT =====")
                    print("Username can't be empty")
                    print("Website: " + w)

                while True:
                    p = getpass("Password: ", echo_char="*")

                    if p != "":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("===== ADD ACCOUNT =====")
                        print("Website: " + w)
                        print("Username: " + u)
                        print("Password: " + len(p) * "*")
                        break

                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== ADD ACCOUNT =====")
                    print("Password can't be empty")
                    print("Website: " + w)
                    print("Username: " + u)

                
                cp = getpass("Confirm password: ", echo_char="*")

                if cp != p:
                    print("Confirm password doesn't match")
                    input("\nPress Enter to return to main menu...")
                    break

                os.system("cls" if os.name == "nt" else "clear")
                print("===== ADD ACCOUNT =====")
                print("Website: " + w)
                print("Username: " + u)
                print("Password: " + len(p) * "*")
                print("Confirm password: " + len(cp) * "*")

                confirm_save = input("\nSave this account? (y/n): ")

                if confirm_save.lower() in ["y", "yes"]:
                    store_account(w, u, p, key)
                    print("Account saved successfully!")
                    input("\nPress Enter to continue...")
                    break
                else:
                    print("Account was not saved.")
                    input("\nPress Enter to continue...")
                    break
           
        
        elif option == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("===== ACCOUNT LIST =====")
            view_list()
            input("\nPress Enter to continue...")
        
        elif option == "3":
            while True:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== EDIT ACCOUNT =====")
                    view_list()
                    try:
                        account_number = int(input("Enter account number to edit (0 to quit): "))
                        break
                    except ValueError:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Please enter a valid number.")

                if account_number == 0:
                    break

                else:
                    with open("vault.json", "r") as file:
                        data = json.load(file)
                    if 1 <= account_number <= len(data["accounts"]):
                        os.system("cls" if os.name == "nt" else "clear")
                        print(f"===== EDIT ACCOUNT ({account_number}) =====")
                        print("Keep it empty if you don't want to change")
                        while True:
                            website = input("Website: ").strip()

                            if website == "":
                                w = website
                                os.system("cls" if os.name == "nt" else "clear")
                                print(f"===== EDIT ACCOUNT ({account_number}) =====")
                                print("Keep it empty if you don't want to change")
                                print("Website: " + w)
                                break
                            
                            if not website.startswith(("http://", "https://")):
                                website = "https://" + website

                            parsed = urlparse(website)

                            if parsed.scheme in ["http", "https"] and parsed.hostname and "." in parsed.hostname:
                                domain = parsed.hostname.removeprefix("www.")
                                w = domain
                                os.system("cls" if os.name == "nt" else "clear")
                                print(f"===== EDIT ACCOUNT ({account_number}) =====")
                                print("Keep it empty if you don't want to change")
                                print("Website: " + w)
                                break
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"===== EDIT ACCOUNT ({account_number}) =====")
                            print("Keep it empty if you don't want to change")
                            print("Url is not valid")
                            continue

                        u = input("Username: ").strip()
                        p = getpass("Password: ", echo_char="*")
                        cp = getpass("Confirm Password: ", echo_char="*")

                        if p != cp:
                            print("Confirm password doesn't match")
                            input("\nPress Enter to continue...")
                            continue                            
                        
                        confirm_edit = input("Are you sure you want to edit this account? (y/n): ")
                        if confirm_edit.lower() in ["y", "yes"]:
                            edit_account(account_number, w, u, p, key)
                            print("Account edition successfully!")
                            input("\nPress Enter to continue...")
                        else:
                            print("Account edition cancelled.")
                            input("\nPress Enter to continue...")

                    else:
                        print("Invalid account number.")
                        input("\nPress Enter to continue...")
                    



        elif option == "4":
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                while True:
                    try:
                        print("===== VIEW PASSWORD =====")
                        view_list()
                        account_number = int(input("\nAccount number (0 to quit): "))
                        break
                    except ValueError:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Please enter a valid number.")

                if account_number == 0:
                    break

                password = view_pass(account_number, key)
                if password is None:
                    print("Invalid account number.")
                    input("\nPress Enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue
                show_pass = False
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== VIEW PASSWORD =====")
                    print(view_account(account_number))
                    if show_pass:
                        print(f"Password: {password}")
                        print("1. Hide password")
                    else:
                        print("Password: ********")
                        print("1. Show password")
                    print("2. Copy password")
                    print("0. Back to main menu")
                    option_pass = input("\nSelect an option: ")
                    if option_pass == "1":
                        show_pass = not show_pass
                    elif option_pass == "2":
                        if password is not None:
                            pyperclip.copy(password)
                            print("Password copied to clipboard!")
                        else:
                            print("Unable to retrieve password.")
                        input("\nPress Enter to continue...")
                    elif option_pass == "0":
                        os.system("cls" if os.name == "nt" else "clear")
                        break

        elif option == "5":
            while True:
                while True:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("===== DELETE ACCOUNT =====")
                    view_list()
                    try:
                        account_number = int(input("Enter account number to delete (0 to quit): "))
                        break
                    except ValueError:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Please enter a valid number.")

                if account_number == 0:
                    break
                else:
                    with open("vault.json", "r") as file:
                        data = json.load(file)


                    if 1 <= account_number <= len(data["accounts"]):
                        confirm_delete = input("Are you sure you want to delete this account? (y/n): ")
                        if confirm_delete.lower() in ["y", "yes"]:
                            delete_account(account_number)
                            print("Account deleted successfully!")
                            input("\nPress Enter to continue...")
                        else:
                            print("Account deletion cancelled.")
                            input("\nPress Enter to continue...")
                    else:
                        print("Invalid account number.")
                        input("\nPress Enter to continue...")
    
        else:
            print("Invalid Option")



def store_account(w, u, p, key):
    with open("vault.json", "r") as file:
        data = json.load(file)

    p = encrypt_pass(p, key)
    
    account = {"website": w, "username":u, "password":p}
    data["accounts"].append(account)

    with open("vault.json", "w") as file:
        json.dump(data, file, indent=4)


def view_pass(n, key):
    with open("vault.json", "r") as file:
        data = json.load(file)

    if 1 <= n <= len(data["accounts"]):
        account = data["accounts"][n-1]
        return decrypt_pass(account["password"], key)
    else:
        return None
        

def view_account(n):
    with open("vault.json", "r") as file:
        data = json.load(file)
    if 1 <= n <= len(data["accounts"]):
        account = data["accounts"][n-1]
        return f"Website: {account["website"]}\nUsername: {account["username"]}"
    else:
        return "Invalid account number."
        

def view_list():
    with open("vault.json", "r") as file:
        data = json.load(file)

    if not data["accounts"]:
        print("No account saved yet.")
        return
    
    for j, account in enumerate(data["accounts"], start=1):
        print(f"{j} {account["website"]} ({account["username"]})")


def delete_account(n):
    with open("vault.json", "r") as file:
        data = json.load(file)

    if 1 <= n <= len(data["accounts"]):
        data["accounts"].pop(n - 1)
    else:
        return False

    with open("vault.json", "w") as file:
        json.dump(data, file, indent=4)
    return True

def edit_account(n, w, u, p, key):
    
    with open("vault.json", "r") as file:
        data = json.load(file)

    if not 1 <= n <= len(data["accounts"]):
        print("Invalid account number.")
        return

    account = data["accounts"][n-1]

    if w == "":
        w = account["website"]
    if u == "":
        u = account["username"]
    if p == "":
        p = account["password"]
    else:
        p = encrypt_pass(p, key)

    account = {"website": w, "username": u, "password": p}
    
    data["accounts"][n-1] = account
    
    with open("vault.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()