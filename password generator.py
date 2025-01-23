import random
import string

def generate_password(length, use_special_chars=True, use_digits=True):
    # Base character set
    characters = string.ascii_letters
    if use_special_chars:
        characters += string.punctuation
    if use_digits:
        characters += string.digits

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) < 12:
        return "Medium"
    else:
        return "Strong"

def main():
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    # Prompt user for special characters and digits options
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'

    # Generate password with the user settings
    password = generate_password(length, use_special_chars, use_digits)
    strength = check_password_strength(password)
    
    print(f"Generated Password: {password}")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()