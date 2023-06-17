import sqlite3
from getpass import getpass

# Database initialization
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

# Create the passwords table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Function to encrypt the password (example, should use more secure methods)
def encrypt_password(password):
    return password[::-1]

# Function to decrypt the password (example, should use more secure methods)
def decrypt_password(encrypted_password):
    return encrypted_password[::-1]

# Function to add a new password
def add_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = getpass("Enter the password: ")
    encrypted_password = encrypt_password(password)

    # Insert the password into the database
    cursor.execute('''
        INSERT INTO passwords (website, username, password)
        VALUES (?, ?, ?)
    ''', (website, username, encrypted_password))
    conn.commit()

    print("Password added successfully.")

# Function to retrieve a password
def retrieve_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")

    # Retrieve the password from the database
    cursor.execute('''
        SELECT password FROM passwords
        WHERE website = ? AND username = ?
    ''', (website, username))
    result = cursor.fetchone()

    if result:
        encrypted_password = result[0]
        password = decrypt_password(encrypted_password)
        print("Password:", password)
    else:
        print("Password not found.")

# Main menu loop
while True:
    print("Password Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        retrieve_password()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
