# Password Manager

## Introduction

The Password Manager is a command-line interface (CLI) application developed using Python. Its main purpose is to provide users with a simple and secure way to store and manage their passwords in one place. With the increasing number of online accounts people use every day, remembering unique and strong passwords for every website can become difficult. This application aims to solve that problem by allowing users to securely store their account credentials and access them whenever needed.

## Features

- **Master Password Protection:** Users create a master password that acts as the primary key to access their password vault.
- **Password Encryption:** Stored passwords are encrypted using the Fernet encryption method provided by the Python Cryptography library.
- **Add Accounts:** Users can add new accounts by entering the website, username, and password.
- **View Accounts:** Users can view their saved accounts and identify them through their associated websites and usernames.
- **Clipboard Integration:** Uses Pyperclip to make copying passwords to the clipboard easier.
- **Simple Interface:** A menu-driven command-line interface allows users to navigate between different operations.

## Technologies Used

- **Python:** The primary programming language used to develop the application.
- **Cryptography (Fernet):** Used for encrypting and decrypting stored passwords.
- **JSON:** Used to store account information in a structured format.
- **Getpass:** Used to accept sensitive input without displaying password characters in the terminal.
- **Pyperclip:** Used for clipboard functionality.
- **OS:** Used for operating-system-related operations, such as clearing the terminal.

## Security

Security is one of the main considerations of this project. Instead of storing passwords as plain text, the application encrypts them before saving them to the vault. Access to the vault is protected by a master password, which is used as part of the encryption and decryption process.

The application uses Fernet symmetric encryption, meaning the same secret key is required to encrypt and decrypt the stored data. This helps prevent unauthorized users from directly reading the passwords stored in the JSON file.

## Conclusion

This project was developed to understand the practical implementation of Python concepts such as file handling, JSON data management, functions, loops, exception handling, and third-party libraries. It also provided an opportunity to explore fundamental cybersecurity concepts, particularly encryption, key management, and password security.

The Password Manager combines practical programming with an important real-world use case. It can be expanded in the future with additional features such as password generation, search functionality, account editing, and a graphical user interface.