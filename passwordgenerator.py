import random
import string
import pyperclip

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Please choose at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    print("Generated Password:", password)
    print("Copied to clipboard!")

def main():
    print("Password Generator")
    print("------------------")
    length = int(input("Enter the length of the password: "))
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special)

if __name__ == '__main__':
    main()
