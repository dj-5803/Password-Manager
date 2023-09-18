import getpass
import hashlib
import json
import pyfiglet

def display_banner():
    banner = pyfiglet.figlet_format("Password Manager")
    print(banner)

# A dictionary to store passwords
passwords = {}

# Function to create a new password entry
def create_password():
    website = input("Enter the website or service name: ")
    username = input("Enter your username: ")
    master_password = getpass.getpass("Enter your master password: ")

    # Hash the master password for added security
    hashed_master_password = hashlib.sha256(master_password.encode()).hexdigest()

    password = getpass.getpass("Enter the password: ")

    # Store the password securely, e.g., in memory (for simplicity)
    passwords[website] = {
        "username": username,
        "password": password,
        "master_password": hashed_master_password,
    }
    print("Password entry created successfully!")

# Function to retrieve a password
def get_password():
    website = input("Enter the website or service name: ")

    if website in passwords:
        master_password = getpass.getpass("Enter your master password: ")
        hashed_master_password = hashlib.sha256(master_password.encode()).hexdigest()

        # Check if the master password matches
        if hashed_master_password == passwords[website]["master_password"]:
            print(f"Username: {passwords[website]['username']}")
            print(f"Password: {passwords[website]['password']}")
        else:
            print("Master password incorrect. Access denied.")
    else:
        print("Website not found in the password manager.")

# Function to backup passwords to a JSON file
def backup_passwords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)
    print("Passwords backed up to 'passwords.json'")

# Function to restore passwords from a JSON file
def restore_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords.update(json.load(file))
        print("Passwords restored from 'passwords.json'")
    except FileNotFoundError:
        print("No backup file found.")

# Main loop
while True:
    display_banner()
    print("\nOptions:")
    print("1. Create a new password entry")
    print("2. Retrieve a password")
    print("3. Backup passwords")
    print("4. Restore passwords")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        backup_passwords()
    elif choice == "4":
        restore_passwords()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
